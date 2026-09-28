/**
 * Expense Tracker backend — Google Apps Script Web App.
 *
 * Tracks income AND expenses, personal AND business, for one or more users
 * (e.g. Dave and Nancy) sharing the same Google Sheet.
 *
 * SETUP:
 * 1. Open your "Expense Tracker" Google Sheet.
 * 2. Extensions → Apps Script. Delete any code in Code.gs, paste this file.
 * 3. Deploy → New deployment → type "Web app".
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 4. Copy the Web app URL and paste it into the Expense Tracker web app's
 *    Settings screen.
 *
 * Keep the Web app URL private — anyone with it can read/write this sheet.
 */

var TABS = {
  Transactions: ['id', 'date', 'merchant', 'description', 'amount', 'txn_type',
                 'category', 'tax_category', 'business_personal',
                 'payment_method', 'notes', 'entered_by', 'created_at'],
  Budgets:      ['category', 'month', 'amount', 'updated_at'],
  Categories:   ['name', 'kind', 'tax_category']
  // txn_type: "income" | "expense" | "transfer"
  // business_personal: "Business" | "Personal"
};

function getSheet_(tab) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(tab);
  if (!sheet) {
    sheet = ss.insertSheet(tab);
  }
  if (sheet.getLastRow() === 0) {
    sheet.getRange(1, 1, 1, TABS[tab].length).setValues([TABS[tab]]);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function fmtDate_(v) {
  if (v instanceof Date) {
    return Utilities.formatDate(v, Session.getScriptTimeZone(), 'yyyy-MM-dd');
  }
  return v;
}

function rowsToObjects_(sheet) {
  var values = sheet.getDataRange().getValues();
  if (values.length < 2) return [];
  var headers = values[0];
  var out = [];
  for (var r = 1; r < values.length; r++) {
    var obj = {};
    var empty = true;
    for (var c = 0; c < headers.length; c++) {
      var v = values[r][c];
      obj[headers[c]] = fmtDate_(v);
      if (v !== '' && v !== null) empty = false;
    }
    if (!empty) out.push(obj);
  }
  return out;
}

function findRowById_(sheet, id) {
  var values = sheet.getDataRange().getValues();
  for (var r = 1; r < values.length; r++) {
    if (String(values[r][0]) === String(id)) return r + 1; // 1-based row
  }
  return -1;
}

function jsonOut_(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function stampId_(row) {
  if (!row.id) {
    row.id = 'x' + new Date().getTime().toString(36) +
             Math.floor(Math.random() * 1e6).toString(36);
  }
  return row.id;
}

function stampCreated_(row, headers) {
  if (!row.created_at && headers.indexOf('created_at') !== -1) {
    row.created_at = Utilities.formatDate(new Date(),
      Session.getScriptTimeZone(), 'yyyy-MM-dd HH:mm');
  }
}

function doGet(e) {
  try {
    var action = (e.parameter.action || 'ping');
    if (action === 'ping') {
      return jsonOut_({ ok: true, tabs: Object.keys(TABS) });
    }
    if (action === 'list') {
      var tab = e.parameter.tab;
      if (!TABS[tab]) return jsonOut_({ ok: false, error: 'Unknown tab: ' + tab });
      return jsonOut_({ ok: true, rows: rowsToObjects_(getSheet_(tab)) });
    }
    return jsonOut_({ ok: false, error: 'Unknown action: ' + action });
  } catch (err) {
    return jsonOut_({ ok: false, error: String(err) });
  }
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    var body = JSON.parse(e.postData.contents);
    var action = body.action;

    if (action === 'append' || action === 'appendMany') {
      var tab = body.tab;
      if (!TABS[tab]) return jsonOut_({ ok: false, error: 'Unknown tab: ' + tab });
      var sheet = getSheet_(tab);
      var headers = TABS[tab];
      var rows = action === 'appendMany' ? (body.rows || []) : [body.row || {}];
      var ids = [];
      var values = rows.map(function (row) {
        stampId_(row);
        stampCreated_(row, headers);
        ids.push(row.id);
        return headers.map(function (h) { return row[h] !== undefined ? row[h] : ''; });
      });
      if (values.length > 0) {
        sheet.getRange(sheet.getLastRow() + 1, 1, values.length, headers.length)
             .setValues(values);
      }
      return jsonOut_({ ok: true, ids: ids });
    }

    if (action === 'update') {
      var sheetU = getSheet_(body.tab);
      var rowNum = findRowById_(sheetU, body.id);
      if (rowNum === -1) return jsonOut_({ ok: false, error: 'Row not found: ' + body.id });
      var headersU = TABS[body.tab];
      var newRow = body.row || {};
      newRow.id = body.id;
      var vals = headersU.map(function (h) { return newRow[h] !== undefined ? newRow[h] : ''; });
      sheetU.getRange(rowNum, 1, 1, headersU.length).setValues([vals]);
      return jsonOut_({ ok: true });
    }

    if (action === 'delete') {
      var sheetD = getSheet_(body.tab);
      var rowNumD = findRowById_(sheetD, body.id);
      if (rowNumD === -1) return jsonOut_({ ok: false, error: 'Row not found: ' + body.id });
      sheetD.deleteRow(rowNumD);
      return jsonOut_({ ok: true });
    }

    if (action === 'setBudget') {
      // Upsert: one row per (category, month). Budgets tab has no id column,
      // so match the row by (category, month) position.
      var sheetB = getSheet_('Budgets');
      var now = Utilities.formatDate(new Date(),
        Session.getScriptTimeZone(), 'yyyy-MM-dd HH:mm');
      var rn = -1;
      var all = sheetB.getDataRange().getValues();
      for (var r = 1; r < all.length; r++) {
        if (String(all[r][0]) === String(body.category) &&
            String(all[r][1]) === String(body.month)) { rn = r + 1; break; }
      }
      if (rn !== -1) {
        sheetB.getRange(rn, 1, 1, 4)
              .setValues([[body.category, body.month, Number(body.amount), now]]);
      } else {
        sheetB.appendRow([body.category, body.month, Number(body.amount), now]);
      }
      return jsonOut_({ ok: true });
    }

    return jsonOut_({ ok: false, error: 'Unknown action: ' + action });
  } catch (err) {
    return jsonOut_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}
