# 🇲🇰 Macedonia Quiz Master - Enhanced Edition

A beautiful, gamified Streamlit quiz application about North Macedonia with 75+ questions across 5 categories, featuring creative design, animations, dark mode, and extensive gamification elements.

## ✨ Features

### 📚 Content
- **75+ Questions** across 5 categories
- **Difficulty Levels**: Easy, Medium, Hard
- **Extensive Knowledge Base**: Geography, History, Culture, Nature & Wildlife, Modern Facts
- **Question Coverage**: From ancient Alexander the Great to modern Macedonia facts

### 🎮 Gamification System
- **Point System**: Earn points based on difficulty and correctness
  - Easy questions: 10 points
  - Medium questions: 25 points
  - Hard questions: 50 points
- **Achievement Badges**: 🎯 Perfect Score, 🔥 Expert, ✅ Proficient
- **Performance Grades**: Visual grade display with emojis (🌟 to 💪)
- **Leaderboard**: Track top players and compete globally
- **Category-based Scoring**: Separate scores for each category

### 🎨 Design & UX
- **Beautiful Gradient UI**: Modern color schemes with purple/blue/pink gradients
- **Dark Mode**: Toggle between light and dark themes
- **Smooth Animations**: Slide-in effects, pulse animations, confetti celebrations
- **Responsive Layout**: Works perfectly on all screen sizes
- **Interactive Cards**: Hover effects and smooth transitions

### 🎯 Quiz Experience
- **Question Navigation**: Move forward and backward through questions
- **Progress Tracking**: Visual progress bar and question counter
- **Answer Review**: See correct answers after completion
- **Instant Feedback**: Know immediately if answers are correct
- **Score Breakdown**: Detailed percentage and point calculations

### 🏆 Leaderboard Features
- **Top 3 Champions**: Medal display (🥇🥈🥉)
- **Full Rankings**: Complete leaderboard with all scores
- **Category Filtering**: View scores by category
- **Statistics**: Average score, highest score, player count
- **Date Tracking**: See when scores were achieved

## 🚀 Getting Started

### Installation

1. **Navigate to the Quiz Master directory**:
   ```bash
   cd "c:\Users\[YourUsername]\Documents\Quiz master"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run Home.py
   ```

4. **Open in browser**: The app will automatically open at `http://localhost:8501`

## 📖 How to Use

### Home Page
- View overall statistics (75 questions, 5 categories)
- See top 3 players on the leaderboard
- Learn about gamification features
- Start a quiz with the "Start Quiz" button

### Categories Page
- Choose from 5 Macedonia categories
- See question count per category
- View difficulty breakdown (Easy/Medium/Hard)
- Click to start a quiz

### Quiz Page
- Answer questions one by one
- Navigate with Previous/Next buttons
- Save answers before moving forward
- View difficulty level (Easy/Medium/Hard)
- See progress with visual progress bar

### Results Page
- View your final score and percentage
- See earned achievements (if any)
- Get points based on difficulty
- Review all answers with explanations
- Save your score to the leaderboard

### Highscores Page
- View leaderboard with all players
- See top 3 champions with medals
- Filter by category
- View statistics and trends

## 📊 Categories

### 🏛️ Geography (15 Questions)
Capital, lakes, mountains, borders, UNESCO sites, rivers, landmarks

### 📚 History (15 Questions)
Alexander the Great, Ottoman rule, independence, ancient kingdoms, uprisings

### 🎭 Culture (15 Questions)
Religion, traditions, food, festivals, music, holidays, customs

### 🌿 Nature & Wildlife (15 Questions)
National parks, flora, fauna, endemic species, highest peaks, lakes

### 🌍 Modern Facts (15 Questions)
Language, currency, sports, politics, economy, international relations

## 🎯 Scoring System

| Difficulty | Correct | Incorrect |
|-----------|---------|-----------|
| Easy      | +10 pts | 0 pts     |
| Medium    | +25 pts | 0 pts     |
| Hard      | +50 pts | 0 pts     |

**Maximum Score**: 900 points (if all questions are hard and correct)

## 🏅 Achievements

| Achievement | Condition |
|------------|-----------|
| 🎯 Perfect Score | 100% correct |
| 🔥 Expert | 90%+ correct |
| ✅ Proficient | 80%+ correct |

## 🌙 Theme Toggle

Click the moon icon (🌙) in the sidebar to switch between:
- **Light Mode**: Clean, bright interface
- **Dark Mode**: Eye-friendly dark theme

## 📁 Project Structure

```
Quiz master/
├── Home.py                      # Main app entry point
├── pages/
│   ├── Categories.py           # Category selection page
│   ├── Quiz.py                 # Quiz interface
│   └── Highscores.py           # Leaderboard page
├── data/
│   ├── questions.json          # 75+ quiz questions
│   ├── highscores.json         # Player scores
│   └── game_stats.json         # Player statistics
├── requirements.txt             # Python dependencies
└── .streamlit/
    └── config.toml             # Streamlit configuration
```

## 💾 Data Files

### questions.json
Structured quiz questions with:
- Question text
- Multiple choice options
- Correct answer
- Difficulty level (easy/medium/hard)

### highscores.json
Player scores with:
- Player name
- Score and total
- Percentage
- Category
- Points earned
- Date achieved

### game_stats.json
Player statistics for future enhancement:
- Total quizzes completed
- Total correct answers
- Level and experience points
- Streaks and achievements
- Favorite categories

## 🔧 Technologies Used

- **Streamlit**: Web app framework
- **Python 3.x**: Core language
- **JSON**: Data storage
- **HTML/CSS**: Custom styling

## 🎨 Design Highlights

### Color Scheme
- **Primary**: Purple/Blue gradient (#667eea → #764ba2)
- **Accent**: Pink/Red gradient (#f093fb → #f5576c)
- **Success**: Green gradient (#84fab0 → #8fd3f4)
- **Warning**: Orange/Red gradient (#fa709a → #fee140)

### Animations
- **Slide-in**: Smooth entrance of content
- **Pulse**: Emphasis animation for achievements
- **Hover**: Interactive card transformations
- **Confetti**: Celebration on high scores

## 📈 Future Enhancements

Potential features for expansion:
- [ ] Sound effects for correct/incorrect answers
- [ ] Level up system with progressive difficulty
- [ ] Daily challenges and rewards
- [ ] Multiplayer mode
- [ ] Timed challenges
- [ ] Power-ups (skip question, 50/50, hint)
- [ ] Mobile app version
- [ ] User accounts and profiles
- [ ] Custom question sets

## 🤝 Contributing

Feel free to:
- Add more questions to categories
- Improve the UI/UX
- Add new features
- Fix bugs
- Suggest improvements

## 📄 License

This project is open source and available for educational purposes.

## 🎓 About Macedonia

North Macedonia is a beautiful Balkan country with:
- Rich ancient history (home of Alexander the Great)
- Stunning natural landscapes (Lake Ohrid - UNESCO site)
- Vibrant culture and traditions
- Strategic historical importance
- Beautiful architecture and monuments

Enjoy learning about this fascinating country! 🇲🇰

---

**Created with ❤️ for Macedonia Quiz Master**

Happy Quizzing! 🚀
