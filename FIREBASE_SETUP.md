# Firebase setup (one-time, ~10 minutes)

The app's Firebase option appears greyed out until you paste a web config into
`FIREBASE_CONFIG` in `index.html` (tapping it explains the setup isn't done yet). One Firebase project serves every user of
the app — each browser signs in anonymously and gets a private data silo, so
no per-user setup is needed.

## Console steps

1. Go to https://console.firebase.google.com → **Add project**. Name it
   (e.g. `expense-tracker`), disable Analytics, Create.
2. **Build → Firestore Database → Create database** → Start in **production
   mode** → pick a region → Enable.
3. **Firestore Database → Rules** → replace with the rules below → Publish.
4. **Build → Authentication → Sign-in method** → enable **Anonymous**,
   **Email/Password**, and **Google** → Save each. (Anonymous gives instant
   private storage; email/Google enable cross-device sync.)
5. **Project overview → Add app → Web (`</>`)** → register (no hosting) →
   copy the `firebaseConfig` object.
6. In `index.html`, replace `var FIREBASE_CONFIG = null;` with your config:
   ```js
   var FIREBASE_CONFIG = {
     apiKey: "AIza…",
     authDomain: "your-project.firebaseapp.com",
     projectId: "your-project",
     storageBucket: "your-project.appspot.com",
     messagingSenderId: "123456789",
     appId: "1:123456789:web:abc…"
   };
   ```
7. Commit and push. The 🔥 Firebase option now appears in the first-launch
   picker and under Setup → Data storage.

## Firestore rules

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId}/{document=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

Each anonymous user can only read/write their own `users/{uid}` subtree.

## Firebase Storage (keeps original statement files)

The import log can keep the original PDF/CSV so statements can be reopened
later from the log. This needs Firebase Storage enabled once:

1. **Build → Storage → Get started** → Start in **production mode** → pick
   the same region as Firestore → Done.
2. **Storage → Rules** → replace with the rules below → Publish.

```
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{userId}/{allPaths=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

Each file is stored under `users/{uid}/statements/` in the user's own silo.
Until Storage is enabled, imports still work — transactions are saved and the
log is recorded, just without the original file attached (the log entry gets
no View button).

## Notes

- The `apiKey` in the web config is a public identifier, not a secret — it is
  safe to ship in the page. Security comes from the rules above plus Auth.
- Anonymous sign-in gives each *browser* its own UID. Linking an email or
  Google account in the app (Setup → Data storage → Sync across devices)
  keeps the same UID, so data carries over and syncs to every device signed
  in to that account. Two people sharing one login share one dataset.
- Firestore is pay-as-you-go but the free Spark quota (50k reads / 20k
  writes / 1 GiB per day) comfortably covers a personal finance app.
