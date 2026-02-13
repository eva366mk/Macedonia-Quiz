"""
Macedonia Quiz Master - Complete Single-File App
Fully compatible with Streamlit Cloud and local deployment
"""

import streamlit as st
import json
import os
from datetime import datetime
import time
import sys

# ==================== CONFIGURATION ====================
st.set_page_config(
    page_title="🇲🇰 Macedonia Quiz Master",
    page_icon="🇲🇰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== PATH HANDLING ====================
def get_data_path(filename):
    """Get correct path for data files"""
    app_root = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(app_root, "data", filename)

# ==================== DATA LOADING ====================
@st.cache_resource
def load_questions():
    """Load questions from JSON"""
    try:
        with open(get_data_path("questions.json"), "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading questions: {e}")
        return {"categories": {}}

@st.cache_resource
def load_highscores():
    """Load highscores from JSON"""
    try:
        path = get_data_path("highscores.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        st.warning(f"Could not load highscores: {e}")
    return {"highscores": []}

def save_highscores(data):
    """Save highscores to JSON"""
    try:
        with open(get_data_path("highscores.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        st.error(f"Error saving highscores: {e}")

# ==================== CSS STYLING ====================
st.markdown("""
<style>
:root {
    --primary-red: #CE1126;
    --primary-yellow: #FFD700;
}

.main { background: linear-gradient(135deg, #CE1126 0%, #FFD700 50%, #CE1126 100%); }

.category-card {
    background: linear-gradient(135deg, #CE1126 0%, #FFD700 100%);
    border-radius: 15px;
    padding: 30px;
    margin: 15px 0;
    color: white;
    box-shadow: 0 8px 32px rgba(206,17,38,0.5);
    transition: all 0.3s ease;
    border: 2px solid #FFD700;
    cursor: pointer;
    text-align: center;
}

.category-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 48px rgba(255,215,0,0.8);
}

.stat-box {
    background: linear-gradient(135deg, #CE1126 0%, #FFD700 100%);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    color: white;
    box-shadow: 0 4px 15px rgba(206,17,38,0.3);
}

.stat-number { font-size: 32px; font-weight: bold; }
.stat-label { font-size: 12px; margin-top: 5px; }

.game-card {
    background: linear-gradient(135deg, #CE1126 0%, #FF6B6B 100%);
    border-radius: 15px;
    padding: 30px;
    color: white;
    box-shadow: 0 8px 32px rgba(206,17,38,0.5);
    border: 2px solid #FFD700;
}

.achievement-badge {
    display: inline-block;
    background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
    padding: 10px 20px;
    border-radius: 10px;
    margin: 5px;
    color: black;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(255,215,0,0.4);
}

.correct-answer { background: #d4edda; padding: 15px; border-radius: 8px; margin: 10px 0; }
.incorrect-answer { background: #f8d7da; padding: 15px; border-radius: 8px; margin: 10px 0; }

.leaderboard-row { 
    background: linear-gradient(90deg, #CE1126 0%, #FFD700 100%); 
    color: white;
    padding: 15px;
    margin: 8px 0;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

# ==================== INITIALIZE SESSION STATE ====================
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "current_category" not in st.session_state:
    st.session_state.current_category = None
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False
if "score" not in st.session_state:
    st.session_state.score = 0

# ==================== HELPER FUNCTIONS ====================
def calculate_points(is_correct, difficulty):
    """Calculate points based on difficulty"""
    if not is_correct:
        return 0
    points = {"easy": 10, "medium": 25, "hard": 50}
    return points.get(difficulty, 10)

def get_grade_emoji(percentage):
    """Get emoji based on score percentage"""
    if percentage >= 90:
        return "🌟"
    elif percentage >= 80:
        return "⭐"
    elif percentage >= 70:
        return "✅"
    elif percentage >= 60:
        return "👍"
    else:
        return "📚"

# ==================== HOME PAGE ====================
def show_home():
    st.title("🇲🇰 Macedonia Quiz Master ☀️")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="stat-box"><div class="stat-number">75</div><div class="stat-label">Questions</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="stat-box"><div class="stat-number">5</div><div class="stat-label">Categories</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="stat-box"><div class="stat-number">∞</div><div class="stat-label">Fun</div></div>""", unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""<div class="game-card">
    Test your knowledge about <b>North Macedonia</b> with 75+ questions!
    </div>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 Categories")
        st.write("""
        - 🏛️ **Geography** - Capital, lakes, mountains, borders
        - 📚 **History** - Ancient Macedonia, Ottoman rule, independence
        - 🎭 **Culture** - Traditions, food, music, holidays
        - 🌿 **Nature & Wildlife** - National parks, flora, fauna
        - 🌍 **Modern Facts** - Language, currency, information
        """)
        if st.button("🚀 Start Quiz", use_container_width=True, key="start_quiz"):
            st.session_state.page = "Categories"
            st.rerun()
    
    with col2:
        st.subheader("🎮 How to Play")
        st.write("""
        1. Choose a category
        2. Answer 15 questions
        3. View your score
        4. Compete on leaderboard!
        """)
        if st.button("🏆 View Leaderboard", use_container_width=True):
            st.session_state.page = "Highscores"
            st.rerun()

# ==================== CATEGORIES PAGE ====================
def show_categories():
    st.title("📚 Select Your Category")
    
    questions_data = load_questions()
    categories = list(questions_data.get("categories", {}).keys())
    
    if not categories:
        st.error("❌ No categories found. Please check data/questions.json")
        return
    
    st.write("Choose a category and test your knowledge about Macedonia!")
    st.divider()
    
    for idx, category in enumerate(categories):
        cat_data = questions_data["categories"][category]
        num_questions = len(cat_data)
        
        if st.button(f"{category}\n({num_questions} Questions)", use_container_width=True, key=f"cat_{idx}"):
            st.session_state.current_category = category
            st.session_state.current_question_index = 0
            st.session_state.user_answers = {}
            st.session_state.quiz_started = True
            st.session_state.quiz_finished = False
            st.session_state.score = 0
            st.rerun()

# ==================== QUIZ PAGE ====================
def show_quiz():
    questions_data = load_questions()
    
    if not st.session_state.quiz_started or not st.session_state.current_category:
        st.warning("Please select a category first!")
        if st.button("← Back to Categories"):
            st.session_state.page = "Categories"
            st.rerun()
        return
    
    category = st.session_state.current_category
    questions = questions_data["categories"][category]
    current_idx = st.session_state.current_question_index
    
    if current_idx >= len(questions):
        # Quiz completed
        st.session_state.quiz_finished = True
        st.session_state.quiz_started = False
        st.rerun()
        return
    
    question = questions[current_idx]
    
    st.title(f"📝 Quiz - {category}")
    st.progress((current_idx + 1) / len(questions))
    
    st.subheader(f"Question {current_idx + 1} of {len(questions)}")
    st.write(f"**Difficulty:** {question.get('difficulty', 'Easy').upper()}")
    st.divider()
    
    st.write(f"### {question['question']}")
    
    # Answer options
    selected = st.radio("Select your answer:", question["options"], key=f"q_{current_idx}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✓ Save Answer", use_container_width=True):
            st.session_state.user_answers[current_idx] = selected
            
            if selected == question["answer"]:
                points = calculate_points(True, question.get("difficulty", "easy"))
                st.session_state.score += points
                st.success(f"✅ Correct! +{points} points")
            else:
                st.error(f"❌ Wrong! Correct answer: {question['answer']}")
            
            time.sleep(1)
            st.session_state.current_question_index += 1
            st.rerun()
    
    with col2:
        if st.button("← Back", use_container_width=True):
            st.session_state.quiz_started = False
            st.session_state.page = "Categories"
            st.rerun()

# ==================== RESULTS PAGE ====================
def show_results():
    if not st.session_state.quiz_finished:
        st.warning("Complete a quiz first!")
        return
    
    questions_data = load_questions()
    category = st.session_state.current_category
    questions = questions_data["categories"][category]
    
    st.title("🎉 Quiz Complete!")
    
    score = st.session_state.score
    percentage = (score / len(questions)) / 10 * 100  # Rough calculation
    percentage = min(100, percentage)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Your Score", f"{score} pts")
    with col2:
        st.metric("Correct Answers", len([a for i, a in st.session_state.user_answers.items() if i < len(questions) and a == questions[i]["answer"]]))
    with col3:
        st.metric("Grade", get_grade_emoji(percentage))
    
    st.divider()
    
    # Save to leaderboard
    highscores_data = load_highscores()
    name = st.text_input("Enter your name for the leaderboard:")
    
    if st.button("💾 Save to Leaderboard"):
        if name:
            highscores_data["highscores"].append({
                "name": name,
                "category": category,
                "score": score,
                "date": datetime.now().isoformat()
            })
            # Sort and keep top 10
            highscores_data["highscores"].sort(key=lambda x: x["score"], reverse=True)
            highscores_data["highscores"] = highscores_data["highscores"][:10]
            save_highscores(highscores_data)
            st.success(f"✅ {name} saved to leaderboard!")
    
    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"
        st.session_state.quiz_finished = False
        st.rerun()

# ==================== HIGHSCORES PAGE ====================
def show_highscores():
    st.title("🏆 Leaderboard")
    
    highscores_data = load_highscores()
    scores = highscores_data.get("highscores", [])
    
    if scores:
        for idx, entry in enumerate(scores[:10], 1):
            st.markdown(f"""
            <div class="leaderboard-row">
                <div><strong>#{idx}</strong> {entry['name']}</div>
                <div><strong>{entry['score']} pts</strong> - {entry.get('category', 'Unknown')}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("🎉 No highscores yet. Complete a quiz to be first!")
    
    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

# ==================== SIDEBAR NAVIGATION ====================
with st.sidebar:
    st.title("🇲🇰 Navigation")
    st.divider()
    
    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        st.session_state.page = "Home"
        st.rerun()
    
    if st.button("📚 Categories", use_container_width=True, key="nav_cat"):
        st.session_state.page = "Categories"
        st.rerun()
    
    if st.button("🏆 Leaderboard", use_container_width=True, key="nav_high"):
        st.session_state.page = "Highscores"
        st.rerun()
    
    st.divider()
    st.caption("Macedonia Quiz Master v1.0")

# ==================== MAIN PAGE ROUTER ====================
if st.session_state.quiz_finished:
    show_results()
elif st.session_state.quiz_started:
    show_quiz()
elif st.session_state.page == "Categories":
    show_categories()
elif st.session_state.page == "Highscores":
    show_highscores()
else:
    show_home()
