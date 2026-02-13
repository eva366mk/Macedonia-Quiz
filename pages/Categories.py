import streamlit as st
import json

st.set_page_config(
    page_title="Categories - Macedonia Quiz Master",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for enhanced design
st.markdown("""
<style>
.category-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    padding: 25px;
    margin: 15px 0;
    color: white;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.15);
    transition: all 0.3s ease;
    text-align: center;
    cursor: pointer;
}

.category-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 48px rgba(102, 126, 234, 0.3);
}

.category-emoji {
    font-size: 48px;
    margin-bottom: 10px;
}

.category-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

.category-count {
    font-size: 14px;
    opacity: 0.9;
}

.difficulty-badge {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 20px;
    margin: 5px;
    font-size: 12px;
    font-weight: bold;
}

.easy { background: #84fab0; color: #2c3e50; }
.medium { background: #f5a623; color: white; }
.hard { background: #e74c3c; color: white; }
</style>
""", unsafe_allow_html=True)

# Load questions
def load_questions():
    with open("data/questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

st.title("📚 Select Your Category")

questions = load_questions()
categories = list(questions["categories"].keys())

st.write("Choose a category and test your knowledge about North Macedonia!")
st.divider()

# Category emojis
category_emojis = {
    "Geography": "🏛️",
    "History": "📚",
    "Culture": "🎭",
    "Nature & Wildlife": "🌿",
    "Modern Facts": "🌍"
}

# Create a grid of category buttons
cols = st.columns(2)

for idx, category in enumerate(categories):
    with cols[idx % 2]:
        question_count = len(questions["categories"][category]["questions"])
        
        # Count questions by difficulty
        easy_count = sum(1 for q in questions["categories"][category]["questions"] if q.get("difficulty") == "easy")
        medium_count = sum(1 for q in questions["categories"][category]["questions"] if q.get("difficulty") == "medium")
        hard_count = sum(1 for q in questions["categories"][category]["questions"] if q.get("difficulty") == "hard")
        
        emoji = category_emojis.get(category, "📖")
        
        if st.button(
            f"{emoji}\n\n{category}\n\n{question_count} Questions",
            key=f"cat_{category}",
            use_container_width=True
        ):
            # Initialize session state for the quiz
            st.session_state.current_category = category
            st.session_state.current_question_index = 0
            st.session_state.user_answers = {}
            st.session_state.quiz_started = True
            st.session_state.quiz_finished = False
            st.session_state.score = 0
            
            # Navigate to quiz page
            st.switch_page("Quiz")
        
        # Show difficulty breakdown
        st.markdown(f"""
        <div style='text-align: center; padding: 10px;'>
            <span class='difficulty-badge easy'>🟢 {easy_count} Easy</span>
            <span class='difficulty-badge medium'>🟡 {medium_count} Medium</span>
            <span class='difficulty-badge hard'>🔴 {hard_count} Hard</span>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# Statistics
st.subheader("📊 Quiz Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_questions = sum(len(cat["questions"]) for cat in questions["categories"].values())
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 10px; color: white;'>
        <h3>Total Questions</h3>
        <h2>{total_questions}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                border-radius: 10px; color: white;'>
        <h3>Categories</h3>
        <h2>{len(categories)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    difficulty_counts = {
        "easy": sum(1 for cat in questions["categories"].values() for q in cat["questions"] if q.get("difficulty") == "easy"),
        "medium": sum(1 for cat in questions["categories"].values() for q in cat["questions"] if q.get("difficulty") == "medium"),
        "hard": sum(1 for cat in questions["categories"].values() for q in cat["questions"] if q.get("difficulty") == "hard")
    }
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                border-radius: 10px; color: white;'>
        <h3>Easy Questions</h3>
        <h2>{difficulty_counts['easy']}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                border-radius: 10px; color: white;'>
        <h3>Hard Questions</h3>
        <h2>{difficulty_counts['hard']}</h2>
    </div>
    """, unsafe_allow_html=True)
