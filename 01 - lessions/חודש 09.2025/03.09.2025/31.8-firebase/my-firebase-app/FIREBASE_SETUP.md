# Firebase Setup Guide

## Environment Variables Configuration

This project uses environment variables to securely store Firebase configuration. Follow these steps to set up your environment:

### 1. Create Environment File

Copy the `firebase.env` file to `.env.local` in your project root:

```bash
cp firebase.env .env.local
```

### 2. Update Firebase Configuration

The `src/firebase.js` file has been updated to use environment variables instead of hardcoded values.

### 3. Environment Variables Used

The following environment variables are required:

- `VITE_FIREBASE_API_KEY` - Your Firebase API key
- `VITE_FIREBASE_AUTH_DOMAIN` - Your Firebase auth domain
- `VITE_FIREBASE_PROJECT_ID` - Your Firebase project ID
- `VITE_FIREBASE_STORAGE_BUCKET` - Your Firebase storage bucket
- `VITE_FIREBASE_MESSAGING_SENDER_ID` - Your Firebase messaging sender ID
- `VITE_FIREBASE_APP_ID` - Your Firebase app ID

### 4. Security Notes

- Never commit `.env.local` or any file containing real API keys to version control
- The `.gitignore` file has been updated to exclude environment files
- Use `.env.example` as a template for other developers

### 5. Vite Configuration

This project uses Vite, which automatically loads environment variables prefixed with `VITE_` from `.env.local` files.

## Troubleshooting

If you encounter issues:

1. Make sure your `.env.local` file exists in the project root
2. Verify all environment variables are properly set
3. Restart your development server after making changes
4. Check that the environment variable names match exactly (including the `VITE_` prefix)
