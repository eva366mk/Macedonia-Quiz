import streamlit as st
import json
import os
from datetime import datetime
import time

st.set_page_config(
    page_title="Quiz - Macedonia Quiz Master",
    page_icon="📝",
    layout="wide"
)

# ==================== SOUND & EFFECT HELPERS ====================
def show_confetti_effect(correct=True, emoji_count=12):
    """Show confetti falling from top with animation"""
    emojis = ['⭐', '✨', '🌟', '💫', '🎉', '🎊'] if correct else ['❌', '😅', '💔']
    
    html = '<style>'
    for i in range(emoji_count):
        delay = i * 0.1
        y_offset = 400 + (i % 3) * 100
        x_offset = (i - emoji_count/2) * 50
        html += f"""
        @keyframes confetti{i} {{
            0% {{ opacity: 1; transform: translateY(0px) translateX(0px) rotate(0deg); }}
            100% {{ opacity: 0; transform: translateY({y_offset}px) translateX({x_offset}px) rotate({i*45}deg); }}
        }}
        .confetti{i} {{
            position: fixed;
            left: {i*8}%;
            top: -50px;
            font-size: 28px;
            animation: confetti{i} 2.5s ease-out forwards;
            animation-delay: {delay}s;
            pointer-events: none;
            z-index: 9999;
        }}
        """
    html += '</style>'
    
    for i in range(emoji_count):
        html += f'<div class="confetti{i}">{emojis[i % len(emojis)]}</div>'
    
    st.markdown(html, unsafe_allow_html=True)

def play_sound_effect(frequencies_with_delays):
    """Play sound effects with proper timing
    frequencies_with_delays: list of tuples (frequency, duration_ms, gain, delay_ms)
    Example: [(800, 150, 0.04, 0), (1000, 150, 0.04, 200)]
    """
    js_code = """
    <script>
    // Get or create global audio context
    if (!window.globalAudioContext) {
        try {
            window.globalAudioContext = new (window.AudioContext || window.webkitAudioContext)();
        } catch(e) {
            console.error('AudioContext creation failed:', e);
        }
    }
    
    function playTone(freq, dur, gain, delay) {
        setTimeout(function() {
            try {
                var ctx = window.globalAudioContext;
                
                // Resume context if suspended (required by browsers for autoplay policy)
                if (ctx.state === 'suspended') {
                    ctx.resume().then(function() {
                        console.log('AudioContext resumed');
                    });
                }
                
                var oscillator = ctx.createOscillator();
                var gainNode = ctx.createGain();
                
                oscillator.frequency.value = freq;
                oscillator.type = 'sine';
                
                gainNode.gain.setValueAtTime(gain, ctx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur / 1000);
                
                oscillator.connect(gainNode);
                gainNode.connect(ctx.destination);
                
                oscillator.start(ctx.currentTime);
                oscillator.stop(ctx.currentTime + dur / 1000);
                console.log('Playing tone:', freq, 'Hz for', dur, 'ms');
            } catch(e) {
                console.error('Sound error:', e);
            }
        }, delay);
    }
    """ 
    
    for freq, dur, gain, delay in frequencies_with_delays:
        js_code += f"playTone({freq}, {dur}, {gain}, {delay});\n"
    
    js_code += """
    </script>
    """
    
    st.markdown(js_code, unsafe_allow_html=True)

# ==================== GAMIFICATION SYSTEM ====================
def calculate_points(is_correct, difficulty):
    """Calculate points based on answer correctness and difficulty"""
    points_map = {
        "easy": 10,
        "medium": 25,
        "hard": 50
    }
    return points_map.get(difficulty, 10) if is_correct else 0

def get_grade_emoji(percentage):
    """Get emoji based on performance percentage"""
    if percentage >= 95:
        return "🌟🌟🌟"
    elif percentage >= 90:
        return "🌟🌟"
    elif percentage >= 80:
        return "⭐⭐"
    elif percentage >= 70:
        return "⭐"
    elif percentage >= 60:
        return "👍"
    else:
        return "💪"

def check_achievement(score, total, category):
    """Check if player unlocked any achievements"""
    achievements = []
    percentage = (score / total) * 100
    
    if percentage == 100:
        achievements.append({"name": "Perfect Score!", "emoji": "🎯", "points": 100})
    if percentage >= 90:
        achievements.append({"name": "Expert!", "emoji": "🔥", "points": 50})
    if percentage >= 80:
        achievements.append({"name": "Proficient", "emoji": "✅", "points": 25})
    
    return achievements

# Load questions
def load_questions():
    with open("data/questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Load highscores
def load_highscores():
    if os.path.exists("data/highscores.json"):
        with open("data/highscores.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"highscores": []}

# Save highscores
def save_highscores(highscores):
    with open("data/highscores.json", "w", encoding="utf-8") as f:
        json.dump(highscores, f, indent=2, ensure_ascii=False)

# Custom CSS with animations and yellow/red Macedonia theme
st.markdown("""
<style>
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

@keyframes slideIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes confetti {
    0% { opacity: 1; transform: translateY(0) rotate(0deg); }
    100% { opacity: 0; transform: translateY(-100px) rotate(360deg); }
}

@keyframes sunrotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes glow {
    0%, 100% { box-shadow: 0 0 10px #FFD700; }
    50% { box-shadow: 0 0 30px #CE1126; }
}

.pulse {
    animation: pulse 0.6s ease-in-out;
}

.slide-in {
    animation: slideIn 0.3s ease-out;
}

.correct-answer {
    background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
    padding: 15px;
    border-radius: 10px;
    color: #CE1126;
    font-weight: bold;
    border: 2px solid #CE1126;
}

.incorrect-answer {
    background: linear-gradient(135deg, #CE1126 0%, #FF6B6B 100%);
    padding: 15px;
    border-radius: 10px;
    color: #FFD700;
    font-weight: bold;
    border: 2px solid #FFD700;
}

.difficulty-easy {
    color: #FFD700;
    font-weight: bold;
    background: #CE1126;
    padding: 5px 10px;
    border-radius: 5px;
}

.difficulty-medium {
    color: #CE1126;
    font-weight: bold;
    background: #FFD700;
    padding: 5px 10px;
    border-radius: 5px;
}

.difficulty-hard {
    color: #FFD700;
    font-weight: bold;
    background: #CE1126;
    padding: 5px 10px;
    border-radius: 5px;
}

.achievement-pop {
    background: linear-gradient(135deg, #FFD700 0%, #CE1126 100%);
    padding: 20px;
    border-radius: 15px;
    color: #CE1126;
    font-weight: bold;
    text-align: center;
    animation: pulse 0.6s ease-in-out;
    box-shadow: 0 8px 32px rgba(255,215,0,0.6);
    border: 3px solid #CE1126;
}

.sun-icon {
    animation: sunrotate 3s linear infinite;
    font-size: 40px;
    display: inline-block;
}

.quiz-container {
    background: linear-gradient(135deg, #FFD700 0%, #CE1126 50%, #FFD700 100%);
    border-radius: 15px;
    padding: 20px;
    border: 3px solid #CE1126;
    box-shadow: 0 0 30px rgba(255,215,0,0.5);
}
</style>
""", unsafe_allow_html=True)

st.title("📝 Quiz")

# Check if quiz is started
if not st.session_state.get("quiz_started", False):
    st.warning("Please select a category from the Categories page to start the quiz!")
    if st.button("Go to Categories"):
        st.switch_page("Categories")
    st.stop()

# Get category and questions
questions_data = load_questions()
category = st.session_state.current_category
questions = questions_data["categories"][category]["questions"]

# Get current question
current_idx = st.session_state.current_question_index
current_question = questions[current_idx]

# Add fun sound effects in sidebar
st.sidebar.markdown("### 🎵 Sound Effects")
sfx_col1, sfx_col2 = st.sidebar.columns(2)

with sfx_col1:
    if st.button("🎺 Win!", use_container_width=True, key="win_sound"):
        st.success("🎵 Playing Win sound!")
        show_confetti_effect(correct=True, emoji_count=15)
        play_sound_effect([(800, 150, 0.04, 0), (1000, 150, 0.04, 170), (1200, 300, 0.04, 340)])

with sfx_col2:
    if st.button("💥 Epic!", use_container_width=True, key="epic_sound"):
        st.success("🎵 Playing Epic sound!")
        show_confetti_effect(correct=True, emoji_count=15)
        play_sound_effect([(600, 100, 0.04, 0), (700, 100, 0.04, 120), (1000, 200, 0.04, 240), (1200, 150, 0.04, 460)])

# Display quiz progress with visual enhancements
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.markdown("## ☀️ **📚 " + category + "** ☀️", unsafe_allow_html=True)

with col2:
    st.metric("Question", f"{current_idx + 1}/{len(questions)}")

with col3:
    difficulty = current_question.get("difficulty", "medium")
    if difficulty == "easy":
        difficulty_display = '<span class="difficulty-easy">🟢 Easy</span>'
    elif difficulty == "medium":
        difficulty_display = '<span class="difficulty-medium">🟡 Medium</span>'
    else:
        difficulty_display = '<span class="difficulty-hard">🔴 Hard</span>'
    st.markdown(difficulty_display, unsafe_allow_html=True)

# Progress bar
progress = (current_idx + 1) / len(questions)
st.progress(progress)

st.divider()

# Display question with animation
st.write(f"### {current_question['question']}")

# Display options with styling
selected_answer = st.radio(
    "Select your answer:",
    options=current_question["options"],
    key=f"question_{current_idx}",
    label_visibility="collapsed"
)

st.divider()

# Navigation buttons with gamification hints
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if current_idx > 0:
        if st.button("⬅️ Previous", use_container_width=True):
            st.session_state.current_question_index -= 1
            st.rerun()

with col2:
    if st.button("💾 Save Answer", use_container_width=True):
        st.session_state.user_answers[current_idx] = selected_answer
        is_correct = selected_answer == current_question["answer"]
        
        if is_correct:
            st.success("✅ Correct Answer!")
            show_confetti_effect(correct=True, emoji_count=12)
            play_sound_effect([(1047, 100, 0.04, 0), (1319, 100, 0.04, 120), (1567, 150, 0.04, 240)])
        else:
            st.warning("❌ Incorrect. Try again!")
            show_confetti_effect(correct=False, emoji_count=6)
            play_sound_effect([(349, 150, 0.03, 0), (262, 150, 0.03, 170)])

with col3:
    if current_idx < len(questions) - 1:
        if st.button("Next ➡️", use_container_width=True):
            st.session_state.user_answers[current_idx] = selected_answer
            is_correct = selected_answer == current_question["answer"]
            if is_correct:
                st.balloons()
            st.session_state.current_question_index += 1
            st.rerun()
    else:
        if st.button("🏁 Finish Quiz", use_container_width=True, type="primary"):
            st.session_state.user_answers[current_idx] = selected_answer
            st.session_state.quiz_finished = True
            st.rerun()

# Show results if quiz is finished
if st.session_state.quiz_finished:
    st.divider()
    
    # Calculate score
    score = 0
    points_earned = 0
    for idx, question in enumerate(questions):
        if st.session_state.user_answers.get(idx) == question["answer"]:
            score += 1
            points_earned += calculate_points(True, question.get("difficulty", "medium"))
        else:
            points_earned += calculate_points(False, question.get("difficulty", "medium"))
    
    st.session_state.score = score
    
    # Display celebratory message
    percentage = (score / len(questions)) * 100
    if percentage >= 80:
        st.success(f"🎉 Excellent Performance! {get_grade_emoji(percentage)}")
    elif percentage >= 60:
        st.info(f"✅ Good Job! {get_grade_emoji(percentage)}")
    else:
        st.warning(f"📚 Keep Learning! {get_grade_emoji(percentage)}")
    
    # Score display with gamification
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; color: white;'>
            <h3>Score</h3>
            <h2>{score}/{len(questions)}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    border-radius: 15px; color: white;'>
            <h3>Percentage</h3>
            <h2>{percentage:.1f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    border-radius: 15px; color: white;'>
            <h3>Points</h3>
            <h2>+{points_earned}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Check for achievements
    achievements = check_achievement(score, len(questions), category)
    if achievements:
        st.subheader("🏅 Achievements Unlocked!")
        for ach in achievements:
            st.markdown(f"""
            <div class="achievement-pop">
                {ach['emoji']} {ach['name']} +{ach['points']} points
            </div>
            """, unsafe_allow_html=True)
        st.divider()

    # Celebration visual + sound on high performance
    if percentage >= 60:
        st.balloons()
        col_center = st.columns(1)[0]
        with col_center:
            st.markdown("""
            <div style='text-align:center; margin: 20px 0;'>
              <div style="font-size:80px; animation: bounce 0.8s ease-in-out infinite; margin-bottom: 10px;">🎉</div>
              <div style="font-size:40px; display: flex; justify-content: center; gap: 10px; margin: 10px 0;">
                <span style="animation: spin 2s linear infinite;">⭐</span>
                <span style="animation: spin 2.5s linear infinite; animation-direction: reverse;">✨</span>
                <span style="animation: spin 2s linear infinite;">⭐</span>
              </div>
              <p style="font-size:20px; font-weight:bold; color:#CE1126; text-shadow: 2px 2px 4px rgba(255,215,0,0.6);">🎊 Amazing! You're doing great! 🎊</p>
            </div>
            <style>
            @keyframes bounce {
                0%, 100% { transform: translateY(0) scale(1); }
                50% { transform: translateY(-30px) scale(1.1); }
            }
            @keyframes spin {
                0% { transform: rotate(0deg) scale(1); }
                50% { transform: rotate(180deg) scale(1.2); }
                100% { transform: rotate(360deg) scale(1); }
            }
            </style>
            """, unsafe_allow_html=True)
        # Play celebratory arpeggio with confetti
        show_confetti_effect(correct=True, emoji_count=25)
        play_sound_effect([(880, 150, 0.04, 0), (1100, 150, 0.04, 170), (1320, 200, 0.04, 340), (1100, 150, 0.04, 560), (880, 250, 0.04, 730), (1760, 100, 0.04, 1000)])
    
    # Show answers review
    st.subheader("📊 Answer Review")
    
    correct_count = 0
    for idx, question in enumerate(questions):
        user_answer = st.session_state.user_answers.get(idx, "Not answered")
        correct_answer = question["answer"]
        is_correct = user_answer == correct_answer
        
        if is_correct:
            correct_count += 1
            status = "✅"
            bg_class = "correct-answer"
        else:
            status = "❌"
            bg_class = "incorrect-answer"
        
        with st.expander(f"{status} Question {idx + 1}: {question['question']}", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                if is_correct:
                    st.markdown(f'<div class="correct-answer">✅ Your Answer: {user_answer}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="incorrect-answer">❌ Your Answer: {user_answer}</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown(f'<div class="correct-answer">✅ Correct Answer: {correct_answer}</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Save to highscores
    st.subheader("💾 Save Your Score")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        player_name = st.text_input("Enter your name to save your score:", value=st.session_state.player_name, placeholder="Your Name")
    
    with col2:
        if st.button("🏆 Save Score", type="primary", use_container_width=True):
            if player_name.strip():
                highscores = load_highscores()
                highscores["highscores"].append({
                    "name": player_name,
                    "score": score,
                    "total": len(questions),
                    "percentage": percentage,
                    "category": category,
                    "points": points_earned,
                    "date": datetime.now().isoformat()
                })
                save_highscores(highscores)
                st.session_state.player_name = player_name
                st.success(f"✅ Score saved! {player_name} scored {score}/{len(questions)} ({percentage:.1f}%)")
                st.balloons()
            else:
                st.warning("Please enter your name")
    
    st.divider()
    
    # Reset button
    if st.button("🔄 Take Another Quiz", use_container_width=True):
        st.session_state.quiz_started = False
        st.session_state.quiz_finished = False
        st.session_state.current_category = None
        st.session_state.current_question_index = 0
        st.session_state.user_answers = {}
        st.switch_page("Categories")
