import streamlit as st
import pandas as pd
import os

FILE_NAME = "typing_history.csv"

# File creation
if not os.path.exists(FILE_NAME):
    df_init = pd.DataFrame(columns=["name", "wpm", "accuracy", "time", "date"])
    df_init.to_csv(FILE_NAME, index=False)

st.set_page_config(page_title="TypeCore", layout="wide")

# Session
query_params = st.query_params

# Default page
if "page" not in st.session_state:
    st.session_state.page = "home"
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "username" not in st.session_state:
    st.session_state.username = "Guest"
       
# Logo click
if "nav" in query_params and query_params["nav"] == "home":
    st.session_state.page = "home"
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
if "final_time" not in st.session_state:
    st.session_state.final_time = 0

# CSS
st.markdown("""
<style>
header {visibility: hidden;}
section[data-testid="stHeader"] {display: none;}

html, body {
    overflow: visible !important;
}

.block-container {
    padding-top: 1rem !important;
    padding-left: 1rem;
    padding-right: 1rem;
}

.stApp {
    background-color: #0b0f14;
}

.logo {
    font-size: 30px;
    font-weight: bold;
    color: white;
}

.logo-container {
    display: flex;
    align-items: center;
    gap: 10px;
}

.logo-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;  
    border-radius: 22px;
    border: 1px solid rgba(0, 224, 255, 0.6);
    background: transparent;
    font-size: 35px; 
    font-weight: 700;  
    color: white;
}

.logo-badge .core {
    color: #00e0ff;
}

.logo-badge:hover {
    box-shadow: 0 0 10px rgba(0, 224, 255, 0.5);
    border-color: #00e0ff;
}

.icon-box {
    background: linear-gradient(135deg, #00e0ff, #008cff);
    color: black;
    padding: 6px 10px;
    border-radius: 8px;
    font-size: 18px;
    box-shadow: 0 0 10px rgba(0, 224, 255, 0.6);
}

.logo-text {
    font-size: 26px;
    font-weight: bold;
    color: white;
}

.logo-text span {
    background: linear-gradient(90deg, #00e0ff, #008cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero {
    text-align: center;
    margin-top: 80px;
}

.tag {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 20px;
    border: 1px solid #00e0ff;
    color: #00e0ff;
    font-size: 14px;
    margin-bottom: 25px;
}

.heading {
    font-size: 64px;
    font-weight: bold;
    color: white;
    line-height: 1.1; 
}

.gradient {
    background: linear-gradient(90deg, #00e0ff, #8a2be2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtext {
    color: #9ca3af;
    font-size: 18px;
    margin-top: 20px;
    line-height: 1; 
    margin-bottom: 15px;
}

.stButton>button {
    background: linear-gradient(90deg, #00e0ff, #00ffa6);
    color: black;
    padding: 12px 28px;
    border-radius: 8px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    box-shadow: 0 0 15px rgba(0, 224, 255, 0.7);
    transform: scale(1.05);
    transition: 0.3s ease;
}

.card {
    background-color: #11161d;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #1f2937;
}

.card {
    background-color: #11161d;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #1f2937;
    transition: all 0.3s ease;  
}

.card:hover {
    transform: translateY(-8px);  
    box-shadow: 0 10px 25px rgba(0, 224, 255, 0.2);  
    border-color: #00e0ff;   
}

.card h3 {color: white;}
.card p {color: #9ca3af;}
</style>
""", unsafe_allow_html=True)

# Navbar
col1, col2 = st.columns([6, 4])

with col1:
    if st.button("⚡ TYPECORE", key="logo_btn"):
        st.session_state.page = "home"

    st.markdown("""
    <style>
    div[data-testid="stButton"] button[key="logo_btn"] {
        border: 1px solid rgba(0, 224, 255, 0.6);
        background: transparent;
        border-radius: 22px;
        padding: 8px 18px;
        font-size: 20px;
        font-weight: 700;
        color: white;
    }

    div[data-testid="stButton"] button[key="logo_btn"]:hover {
        box-shadow: 0 0 10px rgba(0, 224, 255, 0.5);
        border-color: #00e0ff;
    }
    </style>
    """, unsafe_allow_html=True)

with col2:
    c1, c2, c3 = st.columns([0.9, 1, 1.2], gap="small")
    with c1:
        if st.button("Practice"):
            st.session_state.page = "test"
    with c2:
        if st.button("Dashboard"):
            st.session_state.page = "dashboard"
    with c3:
        if st.button("Leaderboard"):
            st.session_state.page = "leaderboard"

# Home page
if st.session_state.page == "home":

    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown('<div class="tag">⚡ High-Performance Typing Coach</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="heading">
        Enter the <span class="gradient">flow state</span>.<br>
        Master the keyboard.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtext">
        TypeCore is a precision-engineered typing test designed to measure your speed,
        track your accuracy, and push you beyond your limits.
    </div>
    """, unsafe_allow_html=True)

    # Start button
    st.markdown('<div class="start-btn">', unsafe_allow_html=True)
    if st.button("START TEST"):
        st.session_state.page = "test"
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card">
        <div style="font-size:40px;">📊</div>
            <h3>Real-time Analytics</h3>
            <p>Track WPM and accuracy instantly as you type. Get character-by-character precision feedback.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <div style="font-size:40px;">🧠</div>
            <h3>Smart Feedback</h3>
            <p>Receive actionable, AI-driven insights after every test to help you target your weaknesses.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <div style="font-size:40px;">🌍</div>
            <h3>Leaderboard</h3>
            <p>Compete with the best typists. Climb the ranks and prove your speed.</p>
        </div>
        """, unsafe_allow_html=True)


elif st.session_state.page == "test":
    import time
    import random

    # CSS
    st.markdown("""
    <style>

    .stat-box {
        background: #11161d;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1f2937;
        text-align: center;
    }

    .stat-value {
        font-size: 32px;
        font-weight: bold;
        color: #00e0ff;
    }

    .accuracy { color: #a855f7; }
    .time { color: white; }

    .typing-box {
        background: #0f141a;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #1f2937;
        font-size: 22px;
        line-height: 1.8;
        min-height: 200px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Session
    if "input" not in st.session_state:
        st.session_state.input = ""
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if "started" not in st.session_state:
        st.session_state.started = False
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    # Difficulty
    difficulty = st.radio(
        "Select Difficulty",
        ["Easy", "Medium", "Hard"],
        index=None,
        horizontal=True
    )

    if difficulty is None:
        st.warning("⚠ Select your difficulty first")
        st.stop()

    # Username
    user_name = st.text_input("USERNAME")

    # Sentences
    sentences_pool = [
        "Cooking your own meals is a great skill to develop.",
        "Fresh ingredients make food taste better and healthier.",
        "Practice daily to improve your typing speed and accuracy.",
        "Technology is evolving rapidly in today's world.",
        "Reading books can improve your vocabulary and focus.",
        "Consistency is the key to mastering any skill.",
        "Healthy habits lead to a better lifestyle.",
        "Learning new things keeps your brain active.",
        "Time management helps in achieving goals faster.",
        "Confidence grows when you practice regularly.",
        "Typing fast requires both speed and accuracy.",
        "Regular practice builds muscle memory in fingers.",
        "Focus on accuracy first before increasing speed.",
        "A calm mind improves overall typing performance.",
        "Avoid looking at the keyboard while typing."
    ]

    if difficulty == "Easy":
        line_count = 3
    elif difficulty == "Medium":
        line_count = random.randint(6, 7)
    else:
        line_count = random.randint(10, 11)

    # Generate text
    if "target_text" not in st.session_state or st.session_state.get("last_diff") != difficulty:
        st.session_state.target_text = " ".join(random.sample(sentences_pool, line_count))
        st.session_state.last_diff = difficulty

    target_text = st.session_state.target_text

    display = ""
    user_input = st.session_state.input

    for i in range(len(target_text)):
        if i < len(user_input):
            if user_input[i] == target_text[i]:
                display += f"<span style='color:#00e0ff'>{target_text[i]}</span>"
            else:
                display += f"<span style='color:red'>{target_text[i]}</span>"
        else:
            display += f"<span style='color:#6b7280'>{target_text[i]}</span>"

    # Calculations
    correct = sum(1 for i in range(len(user_input)) if i < len(target_text) and user_input[i] == target_text[i])
    total = len(user_input)

    accuracy = (correct / total * 100) if total > 0 else 0
    elapsed = int(time.time() - st.session_state.start_time) if st.session_state.start_time else 0
    wpm = (len(user_input) / 5) / (elapsed / 60) if elapsed > 0 else 0

    # Submit control
    if not st.session_state.submitted:
        show_wpm = 0
        show_acc = 0
        show_time = 0
    else:
        show_wpm = st.session_state.final_wpm
        show_acc = st.session_state.final_acc
        show_time = st.session_state.final_time

    # stats
    c1, c2, c3 = st.columns(3)

    c1.markdown(f"<div class='stat-box'><div>WPM</div><div class='stat-value'>{show_wpm}</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='stat-box'><div>ACCURACY</div><div class='stat-value accuracy'>{show_acc}%</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='stat-box'><div>TIME</div><div class='stat-value time'>{show_time}s</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Paragraph
    st.markdown(f"<div class='typing-box'>{display}</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Input box
    new_input = st.text_area(
        "Start Typing Here",
        value=st.session_state.input,
        key="typing_input",
        height=180,
        label_visibility="collapsed"
    )

    if new_input and not st.session_state.started:
        st.session_state.start_time = time.time()
        st.session_state.started = True

    st.session_state.input = new_input
    st.markdown("<br>", unsafe_allow_html=True)
    
    left, center, right = st.columns([3, 2, 3])
    with center:
        b1, b2 = st.columns(2)
        with b1:
            if st.button("⟳ RESTART"):
                st.session_state.input = ""
                st.session_state.start_time = None
                st.session_state.started = False
                st.session_state.submitted = False
                st.session_state.final_time = 0
                st.session_state.final_wpm = 0
                st.session_state.final_acc = 0
                if "target_text" in st.session_state:
                    del st.session_state.target_text
                st.rerun()
                
        with b2:
            if st.button("✅ SUBMIT") and not st.session_state.submitted:
                st.session_state.submitted = True
                st.session_state.username = user_name
                if not st.session_state.started:
                 st.warning("⚠ Please start typing first")
                 st.stop()

                # Calculate final time
                if st.session_state.start_time:
                    final_time = int(time.time() - st.session_state.start_time)
                else:
                   final_time = 1   # prevent zero

                # Calculate final wpm
                final_wpm = (len(st.session_state.input) / 5) / (final_time / 60) if final_time > 0 else 0

                # Calculate final accuracy
                correct = sum(
                   1 for i in range(len(st.session_state.input))
                   if i < len(target_text) and st.session_state.input[i] == target_text[i]
                )
                total = len(st.session_state.input)
                final_acc = (correct / total * 100) if total > 0 else 0

                # Store final values
                st.session_state.final_time = final_time
                st.session_state.final_wpm = int(final_wpm)
                st.session_state.final_acc = int(final_acc)

                # Save to history
                new_data = pd.DataFrame([{
                   "name": user_name if user_name else "Guest",
                   "wpm": st.session_state.final_wpm,
                   "accuracy": st.session_state.final_acc,
                   "time": st.session_state.final_time,
                   "date": pd.Timestamp.now()
                }])

                # Append to CSV
                new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)

                
    if st.session_state.submitted:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            "<h1 style='text-align:center;font-size:40px'>Test Complete </h1>",
            unsafe_allow_html=True
        )

        user_name = st.session_state.get("username", "Guest")
        st.markdown(
            f"<p style='text-align:center; font-size:28px; color:#00e0ff;'>Well done! {user_name} </p>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align:center; color:#a855f7; font-size:22px;'>Keep practicing to improve your speed and accuracy.</p>",
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        left, center, right = st.columns([1,2,1])
        with center:
            if st.button("DASHBOARD ➜", use_container_width=True):
             st.session_state.page = "dashboard"
             st.rerun()
             st.stop()
     
# Dashboard
elif st.session_state.page == "dashboard":

    import pandas as pd

    st.markdown("""
    <style>
    .dash-title {font-size: 34px; font-weight: bold; color: white;}
    .dash-sub {color: #9ca3af; margin-top: -10px;}
    .user-box {
        text-align: right;
        font-size: 15px;
        color: white;
        border: 1px solid #1f2937;
        padding: 8px 14px;
        border-radius: 10px;
        display: inline-block;
    }
    
    .stat-card {
        background: #11161d;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1f2937;
    }
    
    div[data-testid="stLineChart"] {
    background: #11161d;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #1f2937;
    margin-bottom: 15px;
    }
    
    .dashboard-wrapper {
    padding-left: 2rem;
    padding-right: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # User
    user_name = st.session_state.get("username", "Guest")
    
    #Filter user data
    df_all = pd.read_csv(FILE_NAME)

    # Filter by user
    df = df_all[df_all["name"] == user_name]

    if df.empty:
        st.warning("No data found for this user.")
        st.stop()

    df = df.sort_values("date")
    df = df.drop_duplicates(subset=["wpm", "accuracy", "time"], keep="last")
    
    #Header
    col1, col2 = st.columns([4,2])

    with col1:
          st.markdown("<div class='dash-title'>Performance Dashboard</div>", unsafe_allow_html=True)
          st.markdown("<br>", unsafe_allow_html=True)  
          st.markdown("<div class='dash-sub'>Track your progress over time.</div>", unsafe_allow_html=True)

    with col2:
          st.markdown(f"<div class='user-box'>👤 {user_name}</div>", unsafe_allow_html=True)
          st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Stats
    best_wpm = int(df["wpm"].max())
    avg_wpm = int(df["wpm"].mean())
    avg_acc = int(df["accuracy"].mean())

    c1, c2, c3 = st.columns(3)

    c1.markdown(f"<div class='stat-card'><div>🚀 USER BEST WPM</div><div>{best_wpm}</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='stat-card'><div>📊 USER AVG WPM</div><div>{avg_wpm}</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='stat-card'><div>🎯 USER AVG ACCURACY</div><div>{avg_acc}%</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Graphs
    import altair as alt
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📈 Speed Trend (WPM)")
        chart1 = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X("date:T", axis=alt.Axis(labelAngle=0)),  # 👈 horizontal labels
            y="wpm:Q"
        )

        st.altair_chart(chart1, width="stretch")

    with col2:
        st.markdown("### 🎯 Accuracy Trend (%)")
        chart2 = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X("date:T", axis=alt.Axis(labelAngle=0)),  # 👈 horizontal labels
            y="accuracy:Q"
        )   

        st.altair_chart(chart2, width="stretch")
        st.markdown("<br>", unsafe_allow_html=True)

    # Table
    st.subheader("Test History")
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%d %b %H:%M")
    st.dataframe(df, width="stretch")
    
# Leaderboard    
elif st.session_state.page == "leaderboard":
    
    import pandas as pd

    st.markdown("""
    <style>

    .trophy {
        text-align: center;
        font-size: 40px;
        margin-top: 10px;
    }

    .lb-title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: white;
    }

    .lb-sub {
        text-align: center;
        color: #9ca3af;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .leaderboard-table {
    background: #11161d;
    border-radius: 14px;
    border: 1px solid #1f2937;
    overflow: hidden;
    }

    .row {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr 1fr 2fr;
        width: 100%; 
    }
    
    .cell {
    padding: 14px 20px;
    border-bottom: 1px solid #1f2937;
    border-right: 1px solid #1f2937;
    height: 100%;
    }
    
    .leaderboard-table .row:last-child .cell {
    border-bottom: none;
    }
    
    .row .cell:first-child {
    border-left: 1px solid #1f2937;   
    }


    .header .cell {
    color: #00e0ff;
    font-weight: bold;
    background: #0f141a;
    }

    .rank {
        font-weight: bold;
        color: white;
    }
    
    .leaderboard-table {
    background: #11161d;
    border-radius: 14px;
    border: 1px solid #1f2937;  
    overflow: hidden;
    }
    
    .dashboard-wrapper {
    padding-left: 6rem;   
    padding-right: 6rem; 
    }
    
    .name { color: white; }
    .wpm { color: #00e0ff; font-weight: bold; }
    .accuracy { color: #a855f7; font-weight: bold; }
    .date { color: #9ca3af; }

    .top1 { color: gold; }
    .top2 { color: silver; }
    .top3 { color: #cd7f32; }

    </style>
    """, unsafe_allow_html=True)

    # Data
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        st.warning("No data available.")
        st.stop()

    df["date"] = pd.to_datetime(df["date"])

    # Best score per user
    df = df.sort_values("wpm", ascending=False)
    df = df.drop_duplicates(subset=["name"], keep="first")

    # Ranking
    df = df.sort_values("wpm", ascending=False).reset_index(drop=True)
    df["rank"] = df.index + 1

    df["date"] = df["date"].dt.strftime("%d %b %H:%M")

    # UI
    st.markdown("<div class='trophy'>🏆</div>", unsafe_allow_html=True)
    st.markdown("<div class='lb-title'>Leaderboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='lb-sub'>The fastest typists on the platform.</div>", unsafe_allow_html=True)

    # Table
    st.markdown("<div class='dashboard-wrapper'>", unsafe_allow_html=True)
    st.markdown("<div class='leaderboard-table'>", unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class='row header'>
    <div class='cell'>RANK</div>
    <div class='cell'>TYPIST</div>
    <div class='cell'>WPM</div>
    <div class='cell'>ACCURACY</div>
    <div class='cell'>DATE</div>
    </div>
    """, unsafe_allow_html=True)

    # Rows
    for i, row in df.iterrows():

        rank_class = ""
        if row["rank"] == 1:
            rank_display = "🥇"
        elif row["rank"] == 2:
            rank_display = "🥈"
        elif row["rank"] == 3:
            rank_display = "🥉"
        else:
            rank_display = str(row["rank"])

        st.markdown(f"""
        <div class='row'>
        <div class='cell rank'>{rank_display}</div>
        <div class='cell name'>{row['name']}</div>
        <div class='cell wpm'>{row['wpm']}</div>
        <div class='cell accuracy'>{row['accuracy']}%</div>
        <div class='cell date'>{row['date']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)