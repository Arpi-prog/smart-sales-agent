# styles.py - CSS Styling Module for Smart Sales Agent Pro
import streamlit as st

def apply_custom_styles():
    """Apply all custom CSS styles to the Streamlit app"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        /* Global Styles */
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Animations */
        @keyframes glow {
            from { text-shadow: 0 0 20px rgba(102, 126, 234, 0.5); }
            to { text-shadow: 0 0 30px rgba(102, 126, 234, 0.8); }
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        @keyframes slideIn {
            from { transform: translateX(-100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        /* Main Container */
        .main .block-container {
            padding-top: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        /* Header Styling */
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3.5rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 2rem;
            animation: glow 3s ease-in-out infinite alternate;
        }
        
        /* Glass Card Effect */
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
            animation: fadeInUp 0.6s ease-out;
            margin-bottom: 2rem;
        }
        
        /* User Info Card */
        .user-info {
            background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.1) 100%);
            backdrop-filter: blur(10px);
            padding: 1rem 1.5rem;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            animation: slideIn 0.8s ease-out;
        }
        
        /* Mood Display */
        .mood-display {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            color: white;
            font-size: 1.3rem;
            font-weight: 600;
            padding: 2rem;
            border-radius: 20px;
            margin: 1rem 0;
            text-align: center;
            box-shadow: 0 15px 30px rgba(255, 107, 107, 0.3);
            animation: pulse 2s infinite;
        }
        
        /* Reply Box */
        .reply-box {
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            margin: 1rem 0;
            box-shadow: 0 15px 30px rgba(116, 185, 255, 0.3);
            animation: fadeInUp 0.8s ease-out;
        }
        
        /* Stats Boxes */
        .stats-box {
            background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.05) 100%);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.1);
            margin: 1rem 0;
            transition: all 0.3s ease;
            color: white;
        }
        
        .stats-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
        
        /* Alert Styles */
        .alert-danger {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            color: white;
            padding: 1rem 2rem;
            border-radius: 15px;
            border: none;
            animation: pulse 1s infinite;
            font-weight: 600;
        }
        
        .alert-success {
            background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
            color: white;
            padding: 1rem 2rem;
            border-radius: 15px;
            border: none;
            font-weight: 600;
        }
        
        /* Button Styles */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.7rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        }
        
        /* Sidebar Styling */
        .css-1d391kg {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Progress Bar */
        .stProgress .st-bo {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
        }
        
        /* Chat History */
        .chat-item {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 1rem;
            margin: 0.5rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }
        
        .chat-item:hover {
            transform: translateX(10px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        }
        
        /* Floating Action Button */
        .floating-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            color: white;
            font-size: 1.5rem;
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
            cursor: pointer;
            transition: all 0.3s ease;
            z-index: 1000;
        }
        
        .floating-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.6);
        }
        
        /* Text Area Styling */
        .stTextArea textarea {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            color: white;
            backdrop-filter: blur(10px);
        }
        
        .stTextArea textarea:focus {
            border-color: #667eea;
            box-shadow: 0 0 25px rgba(102, 126, 234, 0.3);
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 0.5rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 10px;
            color: white;
            font-weight: 600;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: white;
            font-weight: 600;
        }
        
        /* Metrics */
        .metric-card {
            background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.05) 100%);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.1);
            text-align: center;
            transition: all 0.3s ease;
            color: white;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
        
        /* Loading Animation */
        .loading-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100px;
        }
        
        .loading-spinner {
            width: 40px;
            height: 40px;
            border: 4px solid rgba(255,255,255,0.3);
            border-top: 4px solid #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
    """, unsafe_allow_html=True)

def render_login_header():
    """Render the login page header with animations"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            white-space: nowrap;
            animation: glow 2s ease-in-out infinite alternate;
        ">
            <span style="color: #8ab4f8;">🧠</span>&nbsp;
            <span style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            ">Smart Sales Agent Pro</span>
        </h1>
        <p style="font-size: 1.2rem; color: #aaa; margin-top: 0.5rem;">
            AI-Powered Customer Emotion Detection & Smart Reply Generation
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_main_header():
    """Render the main application header"""
    st.markdown("""
    <div class="glass-card" style="padding: 20px;">
        <div style="text-align: center;">
            <span style="font-size: 2.5rem;">
                <span style="color: #8ab4f8;">🧠</span> 
                <span class="main-header" style="font-size: 2.5rem; font-weight: bold; color: #a287ff; text-shadow: 0 0 10px #a287ff;">
                    Smart Sales Agent Pro
                </span>
            </span>
        </div>
        <div style="text-align: center; color: white; font-size: 1.2rem; margin-top: -0.5rem;">
            AI-Powered Customer Emotion Detection & Smart Reply Generation
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_user_info(username):
    """Render user information card"""
    st.markdown(f"""
    <div class="user-info">
        <span style="font-size: 1.1rem;">👤 Welcome, <strong>{username}</strong></span>
        <br><span style="font-size: 0.9rem; opacity: 0.8;">🚀 Ready to analyze customer emotions!</span>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar_header():
    """Render sidebar header"""
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 15px; margin-bottom: 2rem;">
        <h2 style="color: white; margin: 0;">🛠 Control Center</h2>
        <p style="color: rgba(255,255,255,0.8); margin: 0.5rem 0 0 0;">Customize your experience</p>
    </div>
    """, unsafe_allow_html=True)

def render_metric_card(value, label, color="#667eea"):
    """Render a metric card with custom styling"""
    st.markdown(f"""
    <div class="metric-card">
        <h2 style="margin: 0; color: {color};">{value}</h2>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">{label}</p>
    </div>
    """, unsafe_allow_html=True)

def render_mood_display(mood, confidence, mood_category, intensity=None, show_intensity=True):
    """Render mood analysis display"""
    intensity_text = f'<div style="font-size: 1rem; opacity: 0.9; margin-top: 0.5rem;">Intensity: {intensity.title()}</div>' if show_intensity and intensity else ''
    
    st.markdown(f"""
    <div class="glass-card">
        <h3 style="color: white; text-align: center; margin-bottom: 1.5rem;">
            🧠 Emotion Analysis Results
        </h3>
        <div class="mood-display">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{mood}</div>
            <div style="font-size: 1rem; opacity: 0.9;">
                Confidence: {confidence}% | Category: {mood_category.title()}
            </div>
            {intensity_text}
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_reply_display(reply, lead_score, next_action):
    """Render AI reply display"""
    st.markdown(f"""
    <div class="glass-card">
        <h3 style="color: white; text-align: center; margin-bottom: 1.5rem;">
            🤖 AI-Generated Smart Reply
        </h3>
        <div class="reply-box">
            <div style="font-size: 1.1rem; line-height: 1.6;">
                {reply}
            </div>
        </div>
        <div style="margin-top: 1rem; text-align: center;">
            <small style="color: rgba(255,255,255,0.8);">
                💡 Lead Score: {lead_score}/100 | Action: {next_action}
            </small>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_alert(message, alert_type="success"):
    """Render alert messages with styling"""
    alert_class = "alert-success" if alert_type == "success" else "alert-danger"
    icon = "✅ <strong>POSITIVE SIGNAL:</strong>" if alert_type == "success" else "🚨 <strong>URGENT ALERT:</strong>"
    
    st.markdown(f"""
    <div class="{alert_class}">
        {icon} {message}
    </div>
    """, unsafe_allow_html=True)

def render_loading_spinner():
    """Render loading animation"""
    st.markdown("""
    <div class="loading-container">
        <div class="loading-spinner"></div>
    </div>
    """, unsafe_allow_html=True)

def render_section_header(title, icon="📊"):
    """Render section headers with consistent styling"""
    st.markdown(f"""
    <div class="glass-card">
        <h2 style="color: white; text-align: center; margin-bottom: 2rem;">
            {icon} {title}
        </h2>
    </div>
    """, unsafe_allow_html=True)

def render_footer(username, chat_count):
    """Render application footer"""
    from datetime import datetime
    
    st.markdown(f"""
    <div class="glass-card">
        <div style="text-align: center;">
            <h3 style="color: white; margin-bottom: 1rem;">🧠 Smart Sales Agent Pro</h3>
            <p style="color: rgba(255,255,255,0.8); margin-bottom: 1rem;">
                AI-Powered Customer Emotion Detection & Smart Reply Generation
            </p>
            <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 1rem;">
                <div style="color: rgba(255,255,255,0.7);">
                    👤 <strong>User:</strong> {username}
                </div>
                <div style="color: rgba(255,255,255,0.7);">
                    📊 <strong>Messages:</strong> {chat_count}
                </div>
                <div style="color: rgba(255,255,255,0.7);">
                    🕒 <strong>Session:</strong> {datetime.now().strftime('%H:%M')}
                </div>
            </div>
            <p style="color: rgba(255,255,255,0.6); font-size: 0.9rem;">
                Built with ❤ for intelligent customer engagement
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)