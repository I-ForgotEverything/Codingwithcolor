import streamlit as st

st.set_page_config(page_title="CodeWithColor", page_icon="🎨", layout="centered")

# Edit this list to change the course. Progress total updates automatically.
LESSONS = [
    "Meet the Code", "Print a Message", "Variables", "Numbers",
    "Strings", "User Input", "If Statements", "Comparisons",
    "Logical Operators", "For Loops", "While Loops", "Lists",
    "List Positions", "Functions", "Parameters", "Return Values",
    "Dictionaries", "Debugging", "Mini Project", "Final Challenge"
]

if "completed" not in st.session_state:
    st.session_state.completed = 2
if "xp" not in st.session_state:
    st.session_state.xp = 40
if "streak" not in st.session_state:
    st.session_state.streak = 2
if "selected" not in st.session_state:
    st.session_state.selected = min(st.session_state.completed, len(LESSONS)-1)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');
html, body, [class*="css"] {font-family:Nunito,sans-serif}
.stApp {background:#faf8ff;color:#30264c}
.block-container {max-width:720px;padding-top:1.5rem}
header,footer,#MainMenu {visibility:hidden}
.brand {font-size:28px;font-weight:900;color:#6848dc}
.stat {background:white;border:2px solid #eee8ff;border-radius:14px;padding:7px 12px;font-weight:900}
.bar {height:12px;background:#e9e3f7;border-radius:20px;overflow:hidden;margin:8px 0 20px}
.fill {height:12px;background:linear-gradient(90deg,#7955e8,#39c9a5);border-radius:20px}
.streak {background:#fff2d8;border:2px solid #ffe2a6;border-radius:18px;padding:14px 18px;margin:12px 0 24px;display:flex;justify-content:space-between;align-items:center}
.streak strong {font-size:22px;color:#d88716}
.days {font-size:19px;letter-spacing:3px}
.hint {text-align:center;color:#9389aa;font-weight:800;font-size:13px;margin-bottom:12px}
div.stButton>button {border-radius:50%;width:66px;height:66px;padding:0;font-size:19px;font-weight:900;border:0;box-shadow:0 5px 0 #d8d1e9}
div.stButton>button[kind="primary"] {background:#704fe1;color:white}
div.stButton>button[kind="secondary"] {background:#e4e0ed;color:#9991ad}
.lessonbox {background:white;border:2px solid #eee8ff;border-radius:20px;padding:18px;margin-top:18px}
</style>
""", unsafe_allow_html=True)

a, b = st.columns([3, 1])
with a:
    st.markdown('<div class="brand">🎨 CodeWithColor</div>', unsafe_allow_html=True)
with b:
    st.markdown(f'<div class="stat">⚡ {st.session_state.xp} XP</div>', unsafe_allow_html=True)

total = len(LESSONS)
done = min(st.session_state.completed, total)
st.markdown(
    f'<div style="display:flex;justify-content:space-between;font-weight:900;color:#817799">'
    f'<span>YOUR LEARNING PATH</span><span>{done}/{total}</span></div>'
    f'<div class="bar"><div class="fill" style="width:{done/total*100:.1f}%"></div></div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="streak"><div><strong>🔥 {st.session_state.streak} day streak</strong>'
    f'<div style="color:#a77b3b;font-size:13px;font-weight:800">Keep your learning streak alive!</div></div>'
    f'<div class="days">🔥 🔥 ○ ○ ○ ○ ○</div></div>',
    unsafe_allow_html=True
)
st.markdown('<div class="hint">PICK A LESSON AND FOLLOW THE PATH</div>', unsafe_allow_html=True)

# Winding path uses three columns, so offsets stay within -1, 0, and 1.
offsets = [0, 1, 0, -1, 0, 1, 0, -1]
for i, lesson in enumerate(LESSONS):
    offset = offsets[i % len(offsets)]
    left, center, right = st.columns([1, 1, 1])
    target_col = [left, center, right][offset + 1]
    with target_col:
        if i < done:
            label, kind = "✓", "primary"
        elif i == done:
            label, kind = str(i + 1), "primary"
        else:
            label, kind = "🔒", "secondary"
        if st.button(label, key=f"lesson_{i}", type=kind, disabled=(i > done)):
            st.session_state.selected = i
        st.caption("Completed" if i < done else ("Start here" if i == done else f"Lesson {i+1}"))

selected = min(st.session_state.selected, total - 1)
st.markdown('<div class="lessonbox">', unsafe_allow_html=True)
st.markdown(f"### Lesson {selected+1}: {LESSONS[selected]}")
st.write("Ready to practice a new coding skill? Complete this lesson to earn XP and unlock the next one.")
if selected < done:
    st.success("You have already completed this lesson!")
elif selected == done:
    if st.button("Complete lesson  +20 XP", type="primary", use_container_width=True):
        st.session_state.completed = min(done + 1, total)
        st.session_state.xp += 20
        st.session_state.selected = min(done + 1, total - 1)
        st.rerun()
else:
    st.info("Complete the lessons before this one to unlock it.")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("Demo version: progress lasts for this browser session. Permanent accounts and streak tracking can be added later.")
