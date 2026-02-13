# 🚀 Quick Start - Macedonia Quiz Master

## Installation (First Time Only)

### Option A: Automatic Setup (Recommended)
1. Double-click **`SETUP.bat`** in the project folder
2. Wait for it to complete (~2 minutes)
3. Done! ✓

### Option B: Manual Setup
```powershell
# Open PowerShell and run:
cd "c:\Users\esklehrer\Documents\Quiz master"
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

---

## Running the App

### Option 1: Click to Launch ⭐ (Easiest)
1. Double-click **`START_APP.bat`** 
2. Your default browser opens automatically
3. App loads at `http://localhost:8501`

### Option 2: Desktop Shortcut
1. Run **`CREATE_SHORTCUT.bat`**
2. A shortcut appears on your Desktop
3. Double-click it anytime to launch

### Option 3: Command Line
```powershell
cd "c:\Users\esklehrer\Documents\Quiz master"
.\.venv\Scripts\python.exe -m streamlit run Home.py
```

---

## What You Get

✓ **75 Macedonia Questions** across 5 categories  
✓ **Gamification System** - Points, achievements, leaderboard  
✓ **Difficulty Levels** - Easy (10 pts), Medium (25 pts), Hard (50 pts)  
✓ **Dark Mode** - Eye-friendly interface  
✓ **Sound Effects** - Web Audio API synthesis  
✓ **Confetti Animations** - Celebration effects  
✓ **Leaderboard** - Track top scores  
✓ **Flag Theme** - Red and yellow Macedonia colors  

---

## First Time Tips

1. **Click on the page** before playing sound (browser autoplay policy)
2. **Open DevTools** (F12) if sounds don't work to debug
3. **Try the Quiz page** - Select a category and start playing
4. **Check Highscores** - See the leaderboard

---

## Troubleshooting

### App won't start?
- Make sure Python 3.8+ is installed
- Run `SETUP.bat` again
- Check that the `.venv` folder exists

### Sounds not playing?
1. Open DevTools (F12)
2. Go to Console tab
3. Click a button that plays sound
4. You should see "Playing tone: XXX Hz" messages
5. If you see errors, report them

### Port 8501 already in use?
```powershell
# Run on different port:
.\.venv\Scripts\python.exe -m streamlit run Home.py --server.port 8502
```

---

## File Structure

```
Quiz master/
├── START_APP.bat          ← Click this to launch! 
├── SETUP.bat              ← Run first time to install
├── CREATE_SHORTCUT.bat    ← Creates desktop shortcut
├── Home.py                ← Main app file
├── pages/
│   ├── Quiz.py            ← Quiz interface
│   ├── Categories.py      ← Category selection
│   └── Highscores.py      ← Leaderboard
├── data/
│   ├── questions.json     ← 75 questions
│   ├── highscores.json    ← Saved scores
│   └── game_stats.json    ← Statistics
├── .venv/                 ← Python environment
└── requirements.txt       ← Dependencies
```

---

## Next Steps

1. **Run SETUP.bat** once
2. **Double-click START_APP.bat** to launch
3. **Play the quiz!**
4. **Optional:** Deploy to Streamlit Cloud for online access

---

**Enjoy the Macedonia Quiz Master! 🇲🇰☀️**

Need help? Check the console (F12) for error messages.
