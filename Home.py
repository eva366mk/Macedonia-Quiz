import streamlit as st
import json
import os
from datetime import datetime
import base64

st.set_page_config(
    page_title="🇲🇰 Macedonia Quiz Master",
    page_icon="🇲🇰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS & THEMES ====================
def load_custom_css(dark_mode=False):
    if dark_mode:
        css = """
        <style>
        :root {
            --primary-red: #CE1126;
            --primary-yellow: #FFD700;
            --background: #0d1117;
            --surface: #161b22;
            --text: #c9d1d9;
            --text-secondary: #8b949e;
        }
        
        body { background: linear-gradient(135deg, #CE1126 0%, #FFD700 50%, #CE1126 100%); color: var(--text); }
        .stApp { background: linear-gradient(135deg, #CE1126 0%, #FFD700 50%, #CE1126 100%); }
        
        .game-card {
            background: linear-gradient(135deg, #CE1126 0%, #FF6B6B 100%);
            border-radius: 15px;
            padding: 30px;
            margin: 10px 0;
            color: white;
            box-shadow: 0 8px 32px rgba(206,17,38,0.5);
            transition: all 0.3s ease;
            border: 3px solid #FFD700;
        }
        
        .game-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 48px rgba(255,215,0,0.6);
        }
        
        .achievement-badge {
            display: inline-block;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            padding: 10px 20px;
            border-radius: 20px;
            color: #CE1126;
            margin: 5px;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(255,215,0,0.5);
        }
        
        .stat-box {
            background: var(--surface);
            border: 3px solid #FFD700;
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            text-align: center;
            box-shadow: 0 0 20px rgba(255,215,0,0.4);
        }
        
        .stat-number {
            font-size: 32px;
            font-weight: bold;
            color: #FFD700;
        }
        
        .stat-label {
            color: #FFD700;
            font-size: 14px;
            font-weight: bold;
        }
        
        .progress-bar {
            width: 100%;
            height: 8px;
            background: var(--surface);
            border-radius: 4px;
            overflow: hidden;
            border: 2px solid #FFD700;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #CE1126 0%, #FFD700 100%);
            animation: slideIn 0.5s ease;
        }
        
        @keyframes slideIn {
            from { width: 0%; }
        }
        
        .category-btn {
            background: linear-gradient(135deg, #CE1126 0%, #FFD700 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
            text-align: center;
        }
        
        .category-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
        }
        </style>
        """
    else:
        css = """
        <style>
        :root {
            --primary-red: #CE1126;
            --primary-yellow: #FFD700;
            --background: #fff5e6;
            --surface: #ffe6cc;
            --text: #2c3e50;
            --text-secondary: #7f8c8d;
        }
        
        body { background: linear-gradient(135deg, #FFD700 0%, #CE1126 50%, #FFD700 100%); color: var(--text); }
        .stApp { background: linear-gradient(135deg, #FFD700 0%, #CE1126 50%, #FFD700 100%); }
        
        .game-card {
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            border-radius: 15px;
            padding: 30px;
            margin: 10px 0;
            color: #CE1126;
            box-shadow: 0 8px 32px rgba(255,215,0,0.4);
            transition: all 0.3s ease;
            border: 3px solid #CE1126;
        }
        
        .game-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 48px rgba(206,17,38,0.6);
        }
        
        .achievement-badge {
            display: inline-block;
            background: linear-gradient(135deg, #CE1126 0%, #FF6B6B 100%);
            padding: 10px 20px;
            border-radius: 20px;
            color: #FFD700;
            margin: 5px;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(206,17,38,0.4);
        }
        
        .stat-box {
            background: var(--surface);
            border: 3px solid #CE1126;
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            text-align: center;
            box-shadow: 0 0 20px rgba(206,17,38,0.3);
        }
        
        .stat-number {
            font-size: 32px;
            font-weight: bold;
            color: #CE1126;
        }
        
        .stat-label {
            color: #CE1126;
            font-size: 14px;
            font-weight: bold;
        }
        
        .progress-bar {
            width: 100%;
            height: 8px;
            background: var(--surface);
            border-radius: 4px;
            overflow: hidden;
            border: 2px solid #CE1126;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #CE1126 0%, #FFD700 100%);
            animation: slideIn 0.5s ease;
        }
        
        @keyframes slideIn {
            from { width: 0%; }
        }
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)

# Initialize session state
if "current_category" not in st.session_state:
    st.session_state.current_category = None
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Load questions from JSON
def load_questions():
    with open("data/questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Load highscores
def load_highscores():
    if os.path.exists("data/highscores.json"):
        with open("data/highscores.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"highscores": []}

# Load game stats
def load_game_stats():
    if os.path.exists("data/game_stats.json"):
        with open("data/game_stats.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"players": {}}

# Save highscores
def save_highscores(highscores):
    with open("data/highscores.json", "w", encoding="utf-8") as f:
        json.dump(highscores, f, indent=2, ensure_ascii=False)

# Apply theme
load_custom_css(st.session_state.dark_mode)

# Main UI
st.title("🇲🇰 Macedonia Quiz Master")
st.markdown("---")

# Sidebar navigation and theme toggle
with st.sidebar:
    st.markdown("<h2 style='text-align:center;font-size:28px;'>🇲🇰</h2>", unsafe_allow_html=True)
    
    # Dark mode toggle
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**Theme**")
    with col2:
        if st.toggle("🌙", value=st.session_state.dark_mode, key="theme_toggle"):
            st.session_state.dark_mode = True
            st.rerun()
        elif st.session_state.dark_mode:
            st.session_state.dark_mode = False
            st.rerun()
    
    st.divider()
    st.subheader("Navigation")
    page = st.radio("Select Page", ["🏠 Home", "📚 Categories", "📝 Quiz", "🏆 Highscores"], label_visibility="collapsed")

# Home Page
if page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">75</div>
            <div class="stat-label">Questions</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">5</div>
            <div class="stat-label">Categories</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">∞</div>
            <div class="stat-label">Fun</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.header("Welcome to Macedonia Quiz Master! 🎓")
    
    st.markdown("""
    <div class="game-card">
    Test your knowledge about <b>North Macedonia</b> with our comprehensive quiz featuring 75+ questions!
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 Categories")
        st.write("""
        - 🏛️ **Geography** - Capital, lakes, mountains, and borders
        - 📚 **History** - Ancient Macedonia, Ottoman rule, and independence
        - 🎭 **Culture** - Traditions, food, music, and holidays
        - 🌿 **Nature & Wildlife** - National parks, flora, and fauna
        - 🌍 **Modern Facts** - Language, currency, and contemporary information
        """)
        
        if st.button("🚀 Start Quiz", use_container_width=True, type="primary"):
            st.switch_page("pages/Categories.py")
    
    with col2:
        st.subheader("🎮 How to Play")
        st.write("""
        1. **Choose a category** from the Categories page
        2. **Answer all questions** in the quiz
        3. **View your score** and performance
        4. **Compete** on the highscores leaderboard!
        
        ### 🏅 Gamification Features
        - ⭐ Earn points for correct answers
        - 🔥 Build streaks for consecutive wins
        - 🎖️ Unlock achievements and badges
        - 📈 Track your progress and level up
        - 🎯 Difficulty-based scoring system
        """)
    
    st.divider()
    
    # Global stats
    st.subheader("📊 Global Statistics")
    questions = load_questions()
    highscores = load_highscores()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_questions = sum(len(cat["questions"]) for cat in questions["categories"].values())
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{total_questions}</div>
            <div class="stat-label">Total Questions</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        total_categories = len(questions["categories"])
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{total_categories}</div>
            <div class="stat-label">Categories</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        total_players = len(highscores.get("highscores", []))
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{total_players}</div>
            <div class="stat-label">Players</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Top 3 players
    if highscores["highscores"]:
        st.subheader("🏆 Top 3 Players")
        sorted_scores = sorted(highscores["highscores"], key=lambda x: x["score"], reverse=True)
        
        medals = ["🥇", "🥈", "🥉"]
        cols = st.columns(3)
        
        for idx in range(min(3, len(sorted_scores))):
            with cols[idx]:
                score_entry = sorted_scores[idx]
                st.markdown(f"""
                <div class="game-card">
                    <h2>{medals[idx]}</h2>
                    <h3>{score_entry['name']}</h3>
                    <div class="stat-number">{score_entry['score']}/{score_entry['total']}</div>
                    <div class="stat-label">{score_entry.get('percentage', 0):.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

# Categories Page
elif page == "📚 Categories":
    st.switch_page("pages/Categories.py")

# Quiz Page
elif page == "📝 Quiz":
    st.switch_page("pages/Quiz.py")

# Highscores Page
elif page == "🏆 Highscores":
    st.switch_page("pages/Highscores.py")
