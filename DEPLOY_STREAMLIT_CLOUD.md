# 🚀 Deploy to Streamlit Cloud

Your Quiz Master app is ready for Streamlit Cloud! Follow these steps:

## Step 1: Create a GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. **Repository name:** `quiz-master` (or any name you prefer)
3. **Description:** `Macedonia Quiz Master - Interactive quiz with 75 questions`
4. **Visibility:** Public (required for Streamlit Cloud free tier)
5. Click "Create repository"

## Step 2: Push Code to GitHub

Run these commands in your PowerShell terminal:

```powershell
cd "c:\Users\esklehrer\Documents\Quiz master"

# Add the remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/quiz-master.git
git branch -M main
git push -u origin main
```

## Step 3: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Fill in:
   - **GitHub account:** YOUR_USERNAME
   - **Repository:** quiz-master
   - **Branch:** main
   - **Main file path:** `Home.py`
4. Click "Deploy"

The app will be live in 2-3 minutes at: `https://quiz-master.streamlit.app`

## Step 4: Test It

- Visit your Streamlit Cloud URL
- Test the quiz functionality
- Open DevTools (F12) Console to check if sounds play
- Sounds should work better on Streamlit Cloud than localhost

## Features Your Deploy Includes

✓ 75 Macedonia questions (5 categories)  
✓ Difficulty-based scoring (easy/medium/hard)  
✓ Leaderboard & achievements  
✓ Dark mode  
✓ Yellow/Red Macedonia flag theme  
✓ Sound effects (sine wave synthesis)  
✓ Confetti animations  
✓ Gamification system  

## If Sounds Still Don't Work on Cloud

The issue is likely browser autoplay policy. On Streamlit Cloud:
1. Click anywhere on the page first
2. Then try the quiz
3. Open DevTools Console (F12) to see if sounds are playing

The console should show: `Playing tone: 1047 Hz` etc.

---

**Need help?** Reply with your GitHub username and I can verify the deployment setup.
