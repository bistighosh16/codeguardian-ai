"""
CodeGuardian AI - Web Version
Made with 💜 by Vivi
"""

import streamlit as st
import os
from dotenv import load_dotenv
from codeguardian.reviewer import CodeReviewer

# Load environment
load_dotenv()

# Page config
st.set_page_config(
    page_title="CodeGuardian AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cyberpunk Neon CSS
st.markdown("""
<style>
    /* Import futuristic font */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* Main background - dark cyberpunk */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a0b2e 50%, #0a1929 100%);
        background-attachment: fixed;
    }
    
    /* Animated grid background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(0, 255, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 0, 255, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: 0;
    }
    
    /* Main title - neon glow */
    .main-title {
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 3.5em !important;
        background: linear-gradient(90deg, #00ffff, #ff00ff, #00ffff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        text-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
        animation: shine 3s linear infinite;
        margin: 0;
    }
    
    @keyframes shine {
        to { background-position: 200% center; }
    }
    
    /* Subtitle */
    .subtitle {
        font-family: 'JetBrains Mono', monospace;
        color: #00ffff;
        text-align: center;
        font-size: 1.1em;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 10px;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }
    
    /* Made with heart */
    .made-with {
        text-align: center;
        font-family: 'JetBrains Mono', monospace;
        color: #ff00ff;
        font-size: 0.9em;
        margin-top: 5px;
        text-shadow: 0 0 10px rgba(255, 0, 255, 0.5);
    }
    
    /* Section headers */
    h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00ffff !important;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
        border-left: 4px solid #ff00ff;
        padding-left: 15px;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0e27 0%, #1a0b2e 100%);
        border-right: 2px solid #ff00ff;
        box-shadow: 5px 0 20px rgba(255, 0, 255, 0.2);
    }
    
    [data-testid="stSidebar"] h3 {
        color: #00ffff !important;
        border-left: none;
        padding-left: 0;
    }
    
    /* Buttons - neon style */
    .stButton > button {
        font-family: 'Orbitron', sans-serif !important;
        background: linear-gradient(90deg, #ff00ff, #00ffff);
        color: #0a0e27 !important;
        border: 2px solid #00ffff;
        border-radius: 0;
        padding: 12px 40px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        box-shadow: 
            0 0 20px rgba(0, 255, 255, 0.5),
            inset 0 0 20px rgba(255, 0, 255, 0.2);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #00ffff, #ff00ff);
        transform: translateY(-2px);
        box-shadow: 
            0 0 30px rgba(255, 0, 255, 0.8),
            inset 0 0 30px rgba(0, 255, 255, 0.3);
        color: #0a0e27 !important;
    }
    
    /* Text areas */
    .stTextArea textarea {
        background: rgba(10, 14, 39, 0.8) !important;
        color: #00ff9f !important;
        border: 2px solid #ff00ff !important;
        border-radius: 0 !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 14px !important;
        box-shadow: 0 0 15px rgba(255, 0, 255, 0.2);
    }
    
    .stTextArea textarea:focus {
        border-color: #00ffff !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.4) !important;
    }
    
    /* Text input */
    .stTextInput input {
        background: rgba(10, 14, 39, 0.8) !important;
        color: #00ffff !important;
        border: 2px solid #ff00ff !important;
        border-radius: 0 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background: rgba(10, 14, 39, 0.8) !important;
        color: #00ffff !important;
        border: 2px solid #ff00ff !important;
        border-radius: 0 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    /* Slider */
    .stSlider [data-baseweb="slider"] {
        background: linear-gradient(90deg, #ff00ff, #00ffff);
    }
    
    /* Labels */
    .stTextArea label, .stTextInput label, .stSelectbox label, .stSlider label {
        color: #00ffff !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        font-size: 0.85em !important;
    }
    
    /* Review output card */
    .review-card {
        background: rgba(10, 14, 39, 0.6);
        border: 2px solid #00ffff;
        border-radius: 0;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 
            0 0 30px rgba(0, 255, 255, 0.2),
            inset 0 0 30px rgba(255, 0, 255, 0.05);
        color: #e0e0e0;
        font-family: 'JetBrains Mono', monospace;
        position: relative;
    }
    
    .review-card::before {
        content: '> AI ANALYSIS';
        position: absolute;
        top: -12px;
        left: 20px;
        background: #0a0e27;
        padding: 0 15px;
        color: #ff00ff;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.85em;
        font-weight: 700;
        letter-spacing: 2px;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"] .stMarkdown {
        color: #e0e0e0 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    [data-testid="stSidebar"] a {
        color: #00ffff !important;
        text-decoration: none !important;
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] a:hover {
        color: #ff00ff !important;
        text-shadow: 0 0 10px rgba(255, 0, 255, 0.5);
    }
    
    /* Info/Success/Error boxes */
    .stAlert {
        background: rgba(10, 14, 39, 0.8) !important;
        border: 2px solid #00ff9f !important;
        border-radius: 0 !important;
        color: #00ff9f !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #00ffff !important;
        border-right-color: #ff00ff !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Footer */
    .custom-footer {
        text-align: center;
        padding: 30px 20px;
        margin-top: 50px;
        border-top: 2px solid #ff00ff;
        background: rgba(10, 14, 39, 0.5);
    }
    
    .footer-text {
        font-family: 'Orbitron', sans-serif;
        color: #00ffff;
        letter-spacing: 3px;
        font-size: 1em;
        text-transform: uppercase;
    }
    
    .footer-heart {
        color: #ff00ff;
        font-size: 1.3em;
        text-shadow: 0 0 15px rgba(255, 0, 255, 0.8);
    }
    
    /* Code blocks in review */
    .review-card code {
        background: rgba(255, 0, 255, 0.1) !important;
        color: #00ff9f !important;
        padding: 2px 8px !important;
        border: 1px solid #ff00ff !important;
        border-radius: 0 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .review-card pre {
        background: rgba(0, 0, 0, 0.5) !important;
        border: 1px solid #00ffff !important;
        padding: 15px !important;
        border-radius: 0 !important;
    }
    
    /* Divider line effect */
    .neon-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ff00ff, #00ffff, #ff00ff, transparent);
        margin: 30px 0;
        box-shadow: 0 0 10px rgba(255, 0, 255, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="padding: 20px 0;">
    <h1 class="main-title">⚡ CODEGUARDIAN AI ⚡</h1>
    <p class="subtitle">// AI-Powered Code Review System //</p>
    <p class="made-with">[ Made with 💜 by Vivi ]</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ CONFIG")
    
    language = st.selectbox(
        "LANGUAGE",
        ["python", "javascript", "typescript", "java", "cpp", "go", "rust", "ruby", "php"],
        index=0
    )
    
    focus = st.selectbox(
        "REVIEW MODE",
        ["general", "security", "performance"],
        index=0
    )
    
    max_tokens = st.slider(
        "RESPONSE LENGTH",
        min_value=500,
        max_value=4000,
        value=2000,
        step=500
    )
    
    st.markdown("---")
    
    st.markdown("### 📡 SYSTEM INFO")
    st.markdown("""
    **MODEL:** Llama 3.3 70B  
    **PROVIDER:** Groq  
    **VERSION:** 0.1.0  
    **STATUS:** 🟢 ONLINE
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔗 LINKS")
    st.markdown("[> GitHub Repo](https://github.com/bistighosh16/codeguardian-ai)")
    st.markdown("[> Made by Vivi 💜](https://github.com/bistighosh16)")

# Main content - two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 INPUT CODE")
    
    code_input = st.text_area(
        "CODE",
        height=400,
        placeholder="// Paste your code here...\ndef hello_world():\n    print('Hello, World!')",
        label_visibility="collapsed"
    )
    
    filename = st.text_input(
        "FILENAME",
        value="code.py",
        placeholder="example.py"
    )

with col2:
    st.markdown("### 🤖 ANALYSIS OUTPUT")
    review_container = st.container()
    
    with review_container:
        if "review_result" not in st.session_state:
            st.markdown("""
            <div class="review-card">
                <p style="color: #00ffff; text-align: center; padding: 100px 20px;">
                    >> AWAITING INPUT...<br>
                    >> PASTE CODE AND CLICK ANALYZE<br>
                    >> SYSTEM READY 🟢
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="review-card">
                {st.session_state.review_result}
            </div>
            """, unsafe_allow_html=True)

# Review button
st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    review_button = st.button("⚡ ANALYZE CODE ⚡", use_container_width=True)

# Process review
if review_button:
    if not code_input.strip():
        st.error("⚠️ ERROR: No code detected. Please paste code to analyze.")
    else:
        with st.spinner("🤖 NEURAL NETWORK PROCESSING..."):
            try:
                if not os.getenv("GROQ_API_KEY"):
                    st.error("❌ ERROR: GROQ_API_KEY not configured!")
                else:
                    reviewer = CodeReviewer()
                    formatted_code = "\n".join([f"+ {line}" for line in code_input.split("\n")])
                    
                    review = reviewer.review_code(
                        filename=filename,
                        diff=formatted_code,
                        language=language,
                        focus=focus,
                        max_tokens=max_tokens
                    )
                    
                    st.session_state.review_result = review
                    st.rerun()
                    
            except Exception as e:
                st.error(f"❌ SYSTEM ERROR: {str(e)}")

# Footer
st.markdown("""
<div class="custom-footer">
    <p class="footer-text">
        [ MADE WITH <span class="footer-heart">💜</span> BY VIVI ]
    </p>
    <p style="color: #ff00ff; font-family: 'JetBrains Mono', monospace; margin-top: 10px; font-size: 0.85em;">
        // POWERED BY GROQ AI // BUILT WITH STREAMLIT //
    </p>
</div>
""", unsafe_allow_html=True)