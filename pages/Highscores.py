import streamlit as st
import json
import os

st.set_page_config(
    page_title="Highscores - Macedonia Quiz Master",
    page_icon="🏆",
    layout="wide"
)

# Custom CSS for leaderboard
st.markdown("""
<style>
.medal-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    padding: 25px;
    color: white;
    text-align: center;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2);
}

.rank-entry {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    padding: 15px;
    margin: 10px 0;
    border-radius: 10px;
    border-left: 5px solid #667eea;
}

.rank-entry:hover {
    box-shadow: 0 4px 16px rgba(102, 126, 234, 0.15);
    transform: translateX(5px);
    transition: all 0.3s ease;
}

.rank-number {
    font-size: 20px;
    font-weight: bold;
    color: #667eea;
}

.player-name {
    font-size: 18px;
    font-weight: bold;
    color: #2c3e50;
}

.player-score {
    font-size: 16px;
    color: #e74c3c;
    font-weight: bold;
}

.player-category {
    font-size: 12px;
    color: #7f8c8d;
}
</style>
""", unsafe_allow_html=True)

# Load highscores
def load_highscores():
    if os.path.exists("data/highscores.json"):
        with open("data/highscores.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"highscores": []}

st.title("🏆 Highscores Leaderboard")

highscores = load_highscores()

if highscores["highscores"]:
    sorted_scores = sorted(highscores["highscores"], key=lambda x: x["score"], reverse=True)
    
    # Display top 3 with medals
    st.subheader("👑 Champions")
    medals = ["🥇", "🥈", "🥉"]
    cols = st.columns(3)
    
    for idx in range(min(3, len(sorted_scores))):
        with cols[idx]:
            score_entry = sorted_scores[idx]
            st.markdown(f"""
            <div class="medal-card">
                <h1>{medals[idx]}</h1>
                <h3>{score_entry['name']}</h3>
                <h2 style='color: #4ECDC4;'>{score_entry['score']}/{score_entry['total']}</h2>
                <p style='font-size: 14px;'>📚 {score_entry.get('category', 'N/A')}</p>
                <p style='font-size: 12px;'>⭐ {score_entry.get('percentage', 0):.1f}%</p>
                <p style='font-size: 11px; opacity: 0.8;'>📈 {score_entry.get('points', 0)} points</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # Display all scores with filters
    st.subheader("📊 Full Rankings")
    
    # Filter by category
    categories = sorted(set(entry.get("category", "N/A") for entry in sorted_scores))
    selected_category = st.selectbox("Filter by Category:", ["🌍 All Categories"] + [f"📚 {cat}" for cat in categories])
    
    # Filter scores if needed
    if selected_category == "🌍 All Categories":
        filtered_scores = sorted_scores
    else:
        cat_name = selected_category.replace("📚 ", "")
        filtered_scores = [s for s in sorted_scores if s.get("category") == cat_name]
    
    # Display table
    if filtered_scores:
        # Header
        col1, col2, col3, col4, col5 = st.columns([0.5, 2.5, 1.5, 2, 1.5])
        
        with col1:
            st.markdown("**#**")
        with col2:
            st.markdown("**Player Name**")
        with col3:
            st.markdown("**Category**")
        with col4:
            st.markdown("**Score**")
        with col5:
            st.markdown("**Date**")
        
        st.divider()
        
        # Entries
        for idx, score_entry in enumerate(filtered_scores, 1):
            col1, col2, col3, col4, col5 = st.columns([0.5, 2.5, 1.5, 2, 1.5])
            
            with col1:
                st.markdown(f"<div class='rank-number'>#{idx}</div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<div class='player-name'>🎮 {score_entry['name']}</div>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"<div class='player-category'>📚 {score_entry.get('category', 'N/A')}</div>", unsafe_allow_html=True)
            with col4:
                percentage = score_entry.get('percentage', 0)
                if percentage >= 90:
                    emoji = "🌟"
                elif percentage >= 80:
                    emoji = "⭐"
                elif percentage >= 70:
                    emoji = "👍"
                else:
                    emoji = "📈"
                st.markdown(f"<div class='player-score'>{emoji} {score_entry['score']}/{score_entry['total']} ({percentage:.1f}%)</div>", unsafe_allow_html=True)
            with col5:
                date = score_entry.get('date', 'N/A')[:10]
                st.markdown(f"<div class='player-category'>📅 {date}</div>", unsafe_allow_html=True)
    else:
        st.info("No scores in this category yet.")
    
    st.divider()
    
    # Overall statistics
    st.subheader("📈 Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Players", len(filtered_scores))
    
    with col2:
        avg_score = sum(s["score"] for s in filtered_scores) / len(filtered_scores) if filtered_scores else 0
        st.metric("Average Score", f"{avg_score:.1f}")
    
    with col3:
        highest_score = max(s["score"] for s in filtered_scores) if filtered_scores else 0
        st.metric("Highest Score", highest_score)

else:
    st.info("🎉 No highscores yet. Complete a quiz to be the first on the leaderboard!")
    
    if st.button("📚 Start a Quiz"):
        st.switch_page("Categories")

