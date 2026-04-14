import streamlit as st

st.set_page_config(
    page_title="Sangam AI — Business Plan",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── THEME ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;500;600&display=swap');

/* Global */
[data-testid="stHeader"] { display: none !important; }
.block-container { padding-top: 1.5rem !important; }
html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: radial-gradient(circle at top left, #0A2647, #061221) !important;
    color: #f0ede8;
    font-family: 'Inter', sans-serif;
}
[data-testid="stSidebar"] {
    background: rgba(6, 24, 44, 0.65) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-right: 1px solid rgba(201, 168, 76, 0.3);
}
[data-testid="stSidebar"] * { color: #f0ede8 !important; }

/* Custom Sidebar Radio Navigation */
div[role="radiogroup"] > label {
    display: flex !important;
    align-items: center;
    padding: 10px 14px;
    margin-bottom: 6px;
    border-radius: 8px;
    background: rgba(15, 56, 92, 0.2);
    border: 1px solid transparent;
    transition: all 0.3s ease;
    cursor: pointer;
}
div[role="radiogroup"] > label:hover {
    background: rgba(15, 56, 92, 0.6);
    border-color: rgba(201, 168, 76, 0.4);
    transform: translateX(4px);
}
div[role="radiogroup"] > label[data-baseweb="radio"] input[type="radio"] {
    display: none !important; 
}
/* If Streamlit uses custom radio UI, we might just let it show instead of risking hiding the text */
div[role="radiogroup"] > label[aria-checked="true"] {
    background: linear-gradient(90deg, rgba(201, 168, 76, 0.15), rgba(15, 56, 92, 0.4));
    border-left: 4px solid #c9a84c;
    border-radius: 4px 8px 8px 4px;
}
div[role="radiogroup"] > label[aria-checked="true"] p {
    color: #c9a84c !important;
    font-weight: 600 !important;
}
div[role="radiogroup"] > label p {
    color: #f0ede8;
    font-size: 0.9rem;
    margin: 0;
}

/* Headings */
h1,h2,h3,h4 { font-family: 'Playfair Display', serif !important; color: #ffffff !important; }
h1 {
    background: linear-gradient(90deg, #c9a84c, #fef1b8, #c9a84c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0px 4px 15px rgba(201, 168, 76, 0.2);
}

/* Gold divider */
.gold-line { 
    border: none; 
    height: 2px; 
    background: linear-gradient(to right, transparent, #c9a84c, transparent); 
    margin: 1.5rem 0; 
}

/* Custom Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(201, 168, 76, 0.5); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: #c9a84c; }

/* Base Card Styles */
.metric-card, .slide-card, .rev-card, .roadmap-step, .channel-card, .phase-box {
    background: rgba(15, 56, 92, 0.4);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(201, 168, 76, 0.3);
    border-radius: 8px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.metric-card:hover, .slide-card:hover, .rev-card:hover, .roadmap-step:hover, .channel-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3), 0 0 15px rgba(201, 168, 76, 0.15);
    border-color: rgba(201, 168, 76, 0.8);
}

/* Specific Card Layouts */
.metric-card { padding: 1rem 1.2rem; text-align: center; height: 100%; border: 1px solid rgba(201, 168, 76, 0.4); }
.metric-value { font-size: 2rem; font-weight: 700; color: #c9a84c; line-height: 1.1; }
.metric-label { font-size: 0.78rem; color: #A4C3D2; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; }

.section-header {
    background: rgba(6, 24, 44, 0.6);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(201, 168, 76, 0.3);
    border-left: 6px solid #c9a84c;
    border-radius: 8px;
    padding: 2rem 2.5rem;
    margin: 1rem 0 1.5rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.section-num { font-size: 0.8rem; color: #c9a84c; letter-spacing: 3px; text-transform: uppercase; }
.section-title { font-family: 'Playfair Display', serif; font-size: 2rem; color: #fff; margin: 0.3rem 0; }
.section-sub { color: #A4C3D2; font-size: 0.9rem; }

.slide-card { padding: 1.5rem; margin-bottom: 1rem; border-color: rgba(20, 66, 114, 0.6); }
.slide-title { font-size: 1rem; font-weight: 600; color: #c9a84c; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem; }

table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 0.85rem; border-radius: 8px; overflow: hidden; }
th { background: rgba(6, 24, 44, 0.8); color: #c9a84c; text-align: left; padding: 12px 15px; font-size: 0.78rem; text-transform: uppercase; }
td { padding: 10px 15px; border-bottom: 1px solid rgba(20, 66, 114, 0.4); color: #e0ddd8; background: rgba(15, 56, 92, 0.2); transition: background 0.3s; }
tr:hover td { background: rgba(15, 56, 92, 0.6); }
tr:last-child td { border-bottom: none; }

.badge-critical { background: linear-gradient(135deg, #c0392b, #e74c3c); color:#fff; padding:3px 10px; border-radius:12px; font-size:0.7rem; font-weight:600; border:1px solid #c0392b; box-shadow: 0 2px 5px rgba(231,76,60,0.4); }
.badge-high { background: linear-gradient(135deg, #d35400, #e67e22); color:#fff; padding:3px 10px; border-radius:12px; font-size:0.7rem; font-weight:600; box-shadow: 0 2px 5px rgba(230,126,34,0.4); }
.badge-medium { background: linear-gradient(135deg, #f39c12, #f1c40f); color:#000; padding:3px 10px; border-radius:12px; font-size:0.7rem; font-weight:600; box-shadow: 0 2px 5px rgba(241,196,15,0.4); }
.badge-low { background: linear-gradient(135deg, #27ae60, #2ecc71); color:#fff; padding:3px 10px; border-radius:12px; font-size:0.7rem; font-weight:600; box-shadow: 0 2px 5px rgba(46,204,113,0.4); }

.rev-card { border-top: 3px solid #c9a84c; padding: 1rem 1.2rem; height: 100%; border-color: rgba(20, 66, 114, 0.6); }
.rev-price { font-size: 1.1rem; color: #c9a84c; font-weight: 700; }
.rev-title { font-size: 0.95rem; font-weight: 600; color: #fff; margin: 0.2rem 0; }
.rev-desc { font-size: 0.8rem; color: #A4C3D2; line-height: 1.4; }

.sangam-row td { background: rgba(10, 77, 104, 0.6) !important; color: #c9a84c !important; font-weight: 600; }

.risk-high td:nth-child(2) { color: #e74c3c; font-weight: 600; text-shadow: 0 0 8px rgba(231,76,60,0.3); }
.risk-med td:nth-child(2) { color: #f39c12; font-weight: 600; }
.risk-low td:nth-child(2) { color: #2ecc71; font-weight: 600; }

.audit-box, .audit-good {
    background: rgba(10, 10, 10, 0.5);
    backdrop-filter: blur(8px);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin: 0.5rem 0;
    transition: all 0.3s ease;
}
.audit-box { border: 1px solid rgba(192,57,43,0.5); border-left: 5px solid #c0392b; box-shadow: 0 4px 15px rgba(192,57,43,0.1); }
.audit-box:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(192,57,43,0.25); border-color: #c0392b; }
.audit-good { border: 1px solid rgba(39,174,96,0.5); border-left: 5px solid #27ae60; box-shadow: 0 4px 15px rgba(39,174,96,0.1); background: rgba(10, 26, 13, 0.5); }
.audit-good:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(39,174,96,0.25); border-color: #27ae60; }

.roadmap-step { border-left: 4px solid #c9a84c; padding: 0.8rem 1rem; margin-bottom: 0.5rem; border-color: rgba(20, 66, 114, 0.6); }
.step-num { font-size: 0.7rem; color: #c9a84c; font-weight: 700; text-transform: uppercase; }
.step-title { font-size: 0.9rem; font-weight: 600; color: #fff; }
.step-desc { font-size: 0.8rem; color: #A4C3D2; margin-top: 3px; }

.channel-card { padding: 1rem; margin-bottom: 0.7rem; border-color: rgba(20, 66, 114, 0.6); }
.channel-title { font-size: 0.9rem; font-weight: 600; color: #fff; }
.channel-budget { font-size: 0.8rem; color: #c9a84c; }
.channel-roi { color: #f39c12; }

.phase-box { border-top: 3px solid; padding: 1rem; border-color: rgba(20, 66, 114, 0.6); }

/* hide streamlit chrome */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
[data-testid="stToolbar"] {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR NAV ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### SANGAM AI")
    st.markdown("**Complete Business Plan · 2025–2028**")
    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    pages = [
        "Cover & Overview",
        "Vision & Business Model",
        "Interactive AI Demo",
        "Market Analysis",
        "Investment Plan",
        "Legal Setup",
        "Tech Stack",
        "Subscriptions & Tools",
        "Team & Hiring",
        "Marketing & Growth",
        "Financial Projections",
        "Risk Register",
    ]
    page = st.radio("Navigate", pages, label_visibility="collapsed")

# ─── PAGE: COVER ─────────────────────────────────────────────────────────────
if page == "Cover & Overview":
    st.markdown("""
    <div style="text-align:center; padding: 3rem 0 2rem 0;">
        <div style="font-size:0.8rem; color:#c9a84c; letter-spacing:4px; text-transform:uppercase; margin-bottom:0.5rem;">
            Where Intelligence Meets Tradition
        </div>
        <h1 style="font-size:3.5rem; margin:0; letter-spacing:2px;">SANGAM AI</h1>
        <div style="font-size:0.85rem; color:#A4C3D2; margin-top:0.5rem; letter-spacing:2px;">
            COMPLETE BUSINESS PLAN  ·  FROM ZERO TO LAUNCH
        </div>
        <div style="font-size:1rem; color:#c9a84c; margin-top:0.5rem;">
            Pan-India AI-Powered Matrimonial Platform
        </div>
        <div style="font-size:1.2rem; color:#f0ede8; margin-top:1.5rem; font-weight:600; letter-spacing:1px; font-style:italic;">
            By Pravin A
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""<div class="metric-card"><div class="metric-value">₹5–15L</div>
        <div class="metric-label">Phase 1 Investment</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="metric-card"><div class="metric-value">50M+</div>
        <div class="metric-label">Target Users</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="metric-card"><div class="metric-value">29%</div>
        <div class="metric-label">Market CAGR</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="metric-card"><div class="metric-value" style="font-size:1.5rem;">₹2,000–3,500 Cr</div>
        <div class="metric-label">Realistic Digital TAM ✅</div></div>""", unsafe_allow_html=True)
    st.markdown("")

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### 📋 Table of Contents")
    toc = [
        ("01","Vision & Business Model","Slides 3–5"),
        ("02","Market Analysis","Slides 6–8"),
        ("03","Phase-wise Investment Plan","Slides 9–11"),
        ("04","Legal Setup & Registration","Slides 12–15"),
        ("05","Tech Stack & Software","Slides 16–18"),
        ("06","Subscriptions & Tools","Slides 19–20"),
        ("07","Team & Hiring Plan","Slides 21–22"),
        ("08","Marketing & Growth Strategy","Slides 23–24"),
        ("09","Financial Projections & KPIs","Slides 25–26"),
        ("10","Risk Register","Slide 28"),
    ]
    c1, c2 = st.columns(2)
    for i, (num, title, slides) in enumerate(toc):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""<div class="slide-card" style="padding:0.8rem 1rem; margin-bottom:0.5rem;">
            <span style="color:#c9a84c;font-weight:700;font-size:1.1rem;">{num}</span>
            <span style="color:#fff;font-weight:600;margin-left:0.8rem;">{title}</span>
            <span style="color:#A4C3D2;font-size:0.78rem;float:right;">{slides}</span>
            </div>""", unsafe_allow_html=True)

# ─── PAGE: VISION ─────────────────────────────────────────────────────────────
elif page == "Vision & Business Model":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 01</div>
    <div class="section-title">Vision & Business Model</div>
    <div class="section-sub">What Sangam AI is, and how it makes money</div>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="slide-card">
        <div class="slide-title">Vision</div>
        <p style="color:#e0ddd8;font-size:0.9rem;line-height:1.6;">
        To become India's most trusted AI-powered matchmaking platform — where every family finds love with dignity, data, and deep cultural respect.
        </p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="slide-card">
        <div class="slide-title">Mission</div>
        <p style="color:#e0ddd8;font-size:0.9rem;line-height:1.6;">
        Use AI to remove friction, bias, and fake profiles from Indian matrimony — while honouring family values, regional language, and community traditions.
        </p></div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### 🔑 Value Propositions")
    vp = [
        ("🤖","AI Matching","Compatibility score beyond caste & horoscope"),
        ("🗣️","22 Languages","Voice-first vernacular onboarding"),
        ("✅","Triple Verification","Aadhaar + Video + Family verified badges"),
        ("👨‍👩‍👧","Family Dashboard","Elder-inclusive approval flows built in"),
    ]
    cols = st.columns(4)
    for col, (icon, title, desc) in zip(cols, vp):
        with col:
            st.markdown(f"""<div class="metric-card">
            <div style="font-size:2rem;">{icon}</div>
            <div style="font-weight:600;color:#c9a84c;margin:0.4rem 0 0.3rem;">{title}</div>
            <div style="font-size:0.78rem;color:#A4C3D2;line-height:1.4;">{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### 💰 Business & Revenue Model")
    rm = [
        ("Freemium Subscription","₹499–₹1,999/mo","Basic free. Premium unlocks AI compatibility scores, chat, and verified contact details."),
        ("Profile Boost & Spotlight","₹199–₹999/use","Pay-per-use visibility boost. Show profile at top of search results for 7–30 days."),
        ("Premium Unlock Add-ons","₹149–₹599/each","Kundli report, background check, video call unlock, family meeting scheduler."),
        ("B2B Community Packages","₹9,999/yr","Caste associations, religious groups, NRI societies — white-label portal with community branding."),
    ]
    c1, c2 = st.columns(2)
    for i, (title, price, desc) in enumerate(rm):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""<div class="rev-card">
            <div class="rev-price">{price}</div>
            <div class="rev-title">{title}</div>
            <div class="rev-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)
            st.markdown("")

# ─── PAGE: INTERACTIVE AI DEMO ───────────────────────────────────────────────
elif page == "Interactive AI Demo":
    st.markdown("""<div class="section-header">
    <div class="section-num">LIVE DEMO</div>
    <div class="section-title">AI Compatibility Engine</div>
    <div class="section-sub">Experience the 40+ dimension matchmaking algorithm in action</div>
    </div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="slide-card" style="padding:1rem 1.5rem; border-color:#c9a84c; background: rgba(201, 168, 76, 0.05);">
    Test the proprietary Sangam AI scoring model. Enter mock profiles below to see how our engine avoids surface-level matching and dives into deep lifestyle expectations.
    </div>""", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<h4 style='color:#c9a84c !important; font-size:1.1rem;'>👰 Profile A: The Bride</h4>", unsafe_allow_html=True)
        bride_tradition = st.slider("Traditional vs Modern", 1, 10, 7, key="b1")
        bride_finance = st.selectbox("Financial Expectation", ["Joint Accounts", "Independent", "Traditional Provider"], index=1, key="b2")
        bride_career = st.slider("Career Drive", 1, 10, 9, key="b3")
        
    with c2:
        st.markdown("<h4 style='color:#c9a84c !important; font-size:1.1rem;'>🤵 Profile B: The Groom</h4>", unsafe_allow_html=True)
        groom_tradition = st.slider("Traditional vs Modern", 1, 10, 4, key="g1")
        groom_finance = st.selectbox("Financial Expectation", ["Joint Accounts", "Independent", "Traditional Provider"], index=2, key="g2")
        groom_career = st.slider("Career Drive", 1, 10, 6, key="g3")
        
    if st.button("🚀 Run Sangam AI Compatibility Engine", use_container_width=True):
        import time
        with st.spinner("Analyzing 40+ cultural, financial, and psychological data points..."):
            time.sleep(1.5)
            
        st.markdown("<h3 style='margin-top: 1rem;'>📊 Real-time Match Report</h3>", unsafe_allow_html=True)
        
        # Calculate a mock score to make it dynamic based on inputs
        tradition_diff = abs(bride_tradition - groom_tradition)
        career_diff = abs(bride_career - groom_career)
        fin_match = 100 if bride_finance == groom_finance else 60
        
        overall_score = int(100 - (tradition_diff * 4) - (career_diff * 2))
        overall_score = (overall_score + fin_match) // 2
        
        # Colors based on score
        color = "#2ecc71" if overall_score > 75 else "#f39c12" if overall_score > 50 else "#e74c3c"
        
        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown(f"""<div class="metric-card">
            <div class="metric-label">Value Alignment</div>
            <div class="metric-value" style="color:{color};">{100 - tradition_diff * 10}%</div>
            </div>""", unsafe_allow_html=True)
        with r2:
            st.markdown(f"""<div class="metric-card">
            <div class="metric-label">Financial Harmony</div>
            <div class="metric-value" style="color:{'#2ecc71' if fin_match==100 else '#f39c12'};">{fin_match}%</div>
            </div>""", unsafe_allow_html=True)
        with r3:
            st.markdown(f"""<div class="metric-card">
            <div class="metric-label" style="color:{color};font-weight:bold;">Overall Sangam Score</div>
            <div class="metric-value" style="color:{color};font-size:2.5rem;">{overall_score}%</div>
            </div>""", unsafe_allow_html=True)
            
        # AI generated reasoning box
        reasoning = ""
        if overall_score > 75:
            reasoning = "<strong>🌟 Highly Compatible:</strong> There is a strong alignment in core priorities. Both individuals have realistic and compatible outlooks on career balance and financial structures. Proceed to Family Chat."
        elif overall_score > 50:
            reasoning = "<strong>⚠️ Moderate Match:</strong> The cultural gap exists but is manageable. We recommend our <em>Guided Family Chat</em> feature to discuss differing financial expectations explicitly."
        else:
            reasoning = "<strong>❌ Low Compatibility:</strong> Not recommended. Significant divergence in lifestyle expectations (Traditional vs Modern) will likely cause friction. Sangam AI auto-filters these pairs out to save family time."
            
        st.markdown(f"""<div class="phase-box" style="margin-top:1.5rem; background: rgba(6, 24, 44, 0.6); border-top:3px solid {color};">
        <h4 style="margin-top:0;">🤖 AI Narrative Report</h4>
        <p style="font-size:0.95rem; color:#f0ede8;">{reasoning}</p>
        <p style="font-size:0.8rem; color:#A4C3D2; font-style:italic; margin-top:10px;">Generated via Sangam Vernacular Engine inside the Family Dashboard.</p>
        </div>""", unsafe_allow_html=True)

# ─── PAGE: MARKET ANALYSIS ───────────────────────────────────────────────────
elif page == "Market Analysis":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 02</div>
    <div class="section-title">Market Analysis</div>
    <div class="section-sub">Realistic sizing of the opportunity — corrected from original PPT</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("#### 📐 TAM · SAM · SOM — Corrected")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="metric-card">
        <div style="font-size:0.7rem;color:#A4C3D2;text-transform:uppercase;letter-spacing:1px;">TAM — Total Addressable</div>
        <div class="metric-value" style="font-size:1.6rem;">₹2,000–3,500 Cr</div>
        <div class="metric-label">Online & semi-online digital platforms</div>
        <div style="font-size:0.72rem;color:#e74c3c;margin-top:0.5rem;">Was: ₹9,000 Cr ❌ (inflated)</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="metric-card">
        <div style="font-size:0.7rem;color:#A4C3D2;text-transform:uppercase;letter-spacing:1px;">SAM — Serviceably Available</div>
        <div class="metric-value" style="font-size:1.6rem;">₹800–1,400 Cr</div>
        <div class="metric-label">Smartphone-accessible urban & Tier-2 users</div>
        <div style="font-size:0.72rem;color:#f39c12;margin-top:0.5rem;">Was: ₹3,600 Cr ⚠️ (overstated)</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="metric-card">
        <div style="font-size:0.7rem;color:#A4C3D2;text-transform:uppercase;letter-spacing:1px;">SOM — Obtainable (Yr 1–3)</div>
        <div class="metric-value" style="font-size:1.6rem;">₹5–25 Cr</div>
        <div class="metric-label">AI-first early adopters, Tier 1 & 2</div>
        <div style="font-size:0.72rem;color:#e74c3c;margin-top:0.5rem;">Was: ₹180–720 Cr ❌ (fantasy)</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown("""<div style="background:#06182c;border:1px solid #c9a84c;border-radius:6px;padding:0.8rem 1.2rem;font-size:0.82rem;color:#A4C3D2;">
    📊 India matrimonial CAGR: 29%  ·  Digital penetration growing 40% YoY  ·  Tier 2/3 cities: fastest growing segment
    </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### ⚔️ Competitive Landscape")
    st.markdown("""
    <table>
    <tr>
      <th>Platform</th><th>AI Match</th><th>Vernacular</th><th>Verification</th><th>Family UX</th><th>Sangam Edge</th>
    </tr>
    <tr>
      <td>Matrimony.com</td><td>⚠️ Basic</td><td>⚠️ Partial</td><td>⚠️ Basic</td><td>❌ No</td><td>Full AI + Vernacular</td>
    </tr>
    <tr>
      <td>Shaadi.com</td><td>✅ Medium+</td><td>⚠️ Partial</td><td>⚠️ Basic</td><td>❌ No</td><td>Superior trust layer</td>
    </tr>
    <tr>
      <td>BharatMatrimony</td><td>⚠️ Growing</td><td>✅ Regional</td><td>⚠️ Manual</td><td>❌ No</td><td>Automated AI screen</td>
    </tr>
    <tr>
      <td>Jeevansathi</td><td>✅ Medium</td><td>❌ Hindi only</td><td>❌ Manual</td><td>⚠️ Partial</td><td>Pan-India language AI</td>
    </tr>
    <tr class="sangam-row">
      <td><strong>Sangam AI ✦</strong></td><td>✅ FULL</td><td>✅ 22 Lang</td><td>✅ AI+Video</td><td>✅ YES</td><td>— WE ARE THE EDGE</td>
    </tr>
    </table>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div style="background:#0A4D68;border:1px solid #c9a84c;border-radius:6px;padding:0.7rem 1rem;font-size:0.82rem;color:#c9a84c;text-align:center;">
    ✦ Sangam AI is the ONLY platform with Full AI + 22 Languages + Video KYC + Family Dashboard — all in one app
    </div>""", unsafe_allow_html=True)

# ─── PAGE: INVESTMENT PLAN ───────────────────────────────────────────────────
elif page == "Investment Plan":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 03</div>
    <div class="section-title">Phase-wise Investment Plan</div>
    <div class="section-sub">Start small. Scale smart. From ₹5 Lakh to ₹1 Crore+</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("#### 🚀 Phase 1 — MVP Launch (₹5–15 Lakhs) · Month 1–6")
    phase1 = [
        ("Company Registration","₹0.15L","Pvt Ltd via MCA + GST + PAN (one-time)"),
        ("Basic UI/UX Design","₹0.75L","Figma prototype + 1 designer (freelance, 1 month)"),
        ("Domain + Hosting Setup","₹0.30L","AWS/DigitalOcean 6-month server, domain, SSL, email"),
        ("Legal & Compliance","₹0.50L","Privacy policy, T&C, DPDP Act compliance drafting"),
        ("MVP App Development","₹4.00L","1 Freelance Full-Stack Dev + React Native app (3 months)"),
        ("Marketing — Launch","₹1.50L","Instagram + WhatsApp ads, Chennai launch"),
        ("AI/ML API Costs","₹0.50L","OpenAI API credits for matching (6 months)"),
        ("Contingency Buffer","₹0.80L","Unexpected server costs, bug fixes, misc ops"),
    ]
    c1, c2 = st.columns(2)
    for i, (item, cost, desc) in enumerate(phase1):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""<div class="slide-card" style="padding:0.8rem 1rem;margin-bottom:0.5rem;display:flex;justify-content:space-between;align-items:flex-start;">
            <div>
              <div style="font-weight:600;color:#fff;font-size:0.88rem;">{item}</div>
              <div style="font-size:0.78rem;color:#A4C3D2;margin-top:2px;">{desc}</div>
            </div>
            <div style="color:#c9a84c;font-weight:700;font-size:1rem;white-space:nowrap;margin-left:1rem;">{cost}</div>
            </div>""", unsafe_allow_html=True)
    st.markdown("""<div style="background:#06182c;border:1px solid #c9a84c;border-radius:6px;padding:0.7rem 1rem;font-size:0.82rem;color:#c9a84c;text-align:center;margin-top:0.5rem;">
    PHASE 1 TOTAL: ₹8.5 Lakhs (conservative)  ·  Target: 1,000–3,000 verified profiles  ·  Cities: Chennai, Hyderabad
    </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### 📈 Phase 2 & 3 — Growth & Scale")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="phase-box" style="border-top-color:#3498db;">
        <div style="color:#3498db;font-weight:700;font-size:0.9rem;margin-bottom:0.8rem;">PHASE 2 · ₹20–40L · Month 7–12</div>""", unsafe_allow_html=True)
        p2 = [("₹12L","Hire 2 Full-Time Devs"),("₹3L","AI Model Fine-tuning"),("₹4L","Android + iOS polish"),
              ("₹8L","Performance Marketing"),("₹3L","Customer Support Setup"),("₹4L","Premium Server Infra")]
        for cost, item in p2:
            st.markdown(f"""<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #144272;font-size:0.83rem;">
            <span style="color:#e0ddd8;">{item}</span><span style="color:#c9a84c;font-weight:600;">{cost}</span></div>""", unsafe_allow_html=True)
        st.markdown("""<div style="margin-top:0.6rem;font-size:0.78rem;color:#A4C3D2;">Target: 50,000 profiles · Revenue: ₹8L/mo</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="phase-box" style="border-top-color:#c9a84c;">
        <div style="color:#c9a84c;font-weight:700;font-size:0.9rem;margin-bottom:0.8rem;">PHASE 3 · ₹1 Cr+ · Month 13–24</div>""", unsafe_allow_html=True)
        p3 = [("₹36L","Full Engineering Team (8 devs)"),("₹12L","Proprietary AI Model Training"),("₹25L","Pan-India Marketing"),
              ("₹5L","Legal & IP Protection"),("₹10L","Office Space + Operations"),("₹7L","Investor Relations + Audit")]
        for cost, item in p3:
            st.markdown(f"""<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #144272;font-size:0.83rem;">
            <span style="color:#e0ddd8;">{item}</span><span style="color:#c9a84c;font-weight:600;">{cost}</span></div>""", unsafe_allow_html=True)
        st.markdown("""<div style="margin-top:0.6rem;font-size:0.78rem;color:#A4C3D2;">Target: 5L profiles · Revenue: ₹60L/mo</div></div>""", unsafe_allow_html=True)

# ─── PAGE: LEGAL SETUP ───────────────────────────────────────────────────────
elif page == "Legal Setup":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 04</div>
    <div class="section-title">Legal Setup & Registration</div>
    <div class="section-sub">Stay compliant. Stay trusted. Stay protected.</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("#### 🏢 Where & How to Register")
    steps = [
        ("1","Choose Business Structure","Via: Your decision","Private Limited Company (Pvt Ltd) recommended for fundraising + liability protection. Avoid sole prop for a tech platform."),
        ("2","Register on MCA Portal","Cost: ₹3,000–7,000 · Via: MCA India","Apply for DIN (Director ID), DSC (Digital Signature), and file SPICe+ form."),
        ("3","Get PAN & TAN","Cost: ₹110 each · Via: Income Tax Dept","PAN for the company entity. TAN needed if you'll deduct TDS on salaries."),
        ("4","GST Registration","Cost: Free · Via: GST Portal","Mandatory if annual turnover exceeds ₹20L. Register at gst.gov.in."),
        ("5","Startup India Registration","Cost: Free · Via: DPIIT","Tax exemptions (3 yr), easier patent filing, and credibility via DPIIT recognition."),
        ("6","Open Current Bank Account","Cost: ₹0–5,000 · Via: Your bank","HDFC / ICICI / Kotak for startup-friendly zero-balance accounts."),
    ]
    c1, c2 = st.columns(2)
    for i, (num, title, cost, desc) in enumerate(steps):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""<div class="slide-card" style="margin-bottom:0.5rem;">
            <div style="display:flex;align-items:flex-start;gap:0.8rem;">
              <div style="background:#c9a84c;color:#06182c;font-weight:700;font-size:0.9rem;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;">{num}</div>
              <div>
                <div style="font-weight:600;color:#fff;font-size:0.88rem;">{title}</div>
                <div style="font-size:0.72rem;color:#c9a84c;margin:2px 0;">{cost}</div>
                <div style="font-size:0.78rem;color:#A4C3D2;line-height:1.4;">{desc}</div>
              </div>
            </div></div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### 📋 Laws to Follow")
    laws = [
        ("DPDP Act 2023","CRITICAL","Digital Personal Data Protection Act. Require consent for every data field. Appoint a Data Protection Officer. Non-compliance: ₹250 Cr fine."),
        ("Aadhaar Data Rules","HIGH","You CANNOT store raw Aadhaar numbers. Use UIDAI-certified KYC gateway (DigiLocker / AuthBridge) for verification only."),
        ("IT Act 2000 + Amendments","HIGH","Must have T&Cs, privacy policy, and a grievance officer. Respond to takedown requests within 72 hours."),
        ("Consumer Protection Act 2019","HIGH","Any paid subscription must have clear refund policies. Auto-renewal requires explicit consent."),
        ("Anti-Discrimination Laws","MEDIUM","Caste/religion filters may attract scrutiny. Frame as 'community preference' not discrimination."),
        ("Contract Act 1872","MEDIUM","All B2B agreements, developer contracts, vendor NDAs must be properly executed."),
    ]
    badge_map = {"CRITICAL":"badge-critical","HIGH":"badge-high","MEDIUM":"badge-medium","LOW":"badge-low"}
    st.markdown("""<table><tr><th>Law</th><th>Severity</th><th>What to Do</th></tr>""", unsafe_allow_html=True)
    for law, sev, desc in laws:
        badge = badge_map.get(sev, "badge-low")
        st.markdown(f"""<tr><td style="font-weight:600;color:#fff;">{law}</td>
        <td><span class="{badge}">{sev}</span></td>
        <td style="font-size:0.8rem;">{desc}</td></tr>""", unsafe_allow_html=True)
    st.markdown("</table>", unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### ⚠️ Top Legal Issues & Mitigations")
    issues = [
        ("Fake Profile Lawsuits","Mandatory video KYC + Aadhaar-linked verification. 'User self-declared — not verified by Sangam AI' disclaimer on basic profiles."),
        ("User Harassment / Abuse","Hire a Grievance Officer (mandatory under IT Act). 24-hr block/report system. Female users get privacy mode by default."),
        ("Data Breach Liability","Purchase Cyber Insurance (₹50–80K/yr). AES-256 encryption. DPDP-compliant breach notification within 72 hours."),
        ("Refund Disputes","Crystal-clear refund policy in T&C. 7-day no-questions refund for all subscriptions."),
        ("Caste Filter Discrimination","Re-frame as 'community preference' with user-chosen filters, not platform defaults. Add explicit consent checkbox."),
        ("Defamation via Content","Strict content moderation using AI + human review. Clear platform disclaimer as intermediary, not publisher."),
    ]
    c1, c2 = st.columns(2)
    for i, (issue, mitigation) in enumerate(issues):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""<div class="slide-card" style="margin-bottom:0.5rem;">
            <div style="font-weight:600;color:#e74c3c;font-size:0.85rem;margin-bottom:0.4rem;">⚠️ {issue}</div>
            <div style="font-size:0.78rem;color:#A4C3D2;line-height:1.4;">✔ {mitigation}</div>
            </div>""", unsafe_allow_html=True)

# ─── PAGE: TECH STACK ────────────────────────────────────────────────────────
elif page == "Tech Stack":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 05</div>
    <div class="section-title">Tech Stack & Software</div>
    <div class="section-sub">The tools, platforms, and code that power Sangam AI</div>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="slide-title" style="color:#3498db;margin-bottom:0.8rem;">FRONTEND — What Users See</div>""", unsafe_allow_html=True)
        fe = [
            ("React Native (Expo)","One codebase → Android + iOS. Fastest cross-platform mobile development."),
            ("Next.js (Web Portal)","React framework for web app. Server-side rendering for SEO. Fast load times."),
            ("Tailwind CSS","Utility-first CSS. Rapid UI building. Mobile responsive by default."),
            ("Zustand / Redux","State management for user session, match queue, notifications."),
            ("i18next","Internationalisation library. Powers all 22 vernacular language UIs."),
            ("Figma → Storybook","Design system. All components documented and reusable."),
        ]
        for tech, desc in fe:
            st.markdown(f"""<div class="slide-card" style="margin-bottom:0.4rem;padding:0.7rem 1rem;">
            <div style="font-weight:600;color:#3498db;font-size:0.85rem;">{tech}</div>
            <div style="font-size:0.78rem;color:#A4C3D2;margin-top:2px;">{desc}</div>
            </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="slide-title" style="color:#c9a84c;margin-bottom:0.8rem;">BACKEND — The Engine Room</div>""", unsafe_allow_html=True)
        be = [
            ("Node.js + Express","Primary API server. Fast, non-blocking. REST + GraphQL APIs."),
            ("Python (FastAPI)","AI/ML microservices. Compatibility scoring, photo analysis, fraud detection."),
            ("PostgreSQL","Primary relational database. User profiles, subscriptions, match history."),
            ("Redis","Cache layer. Session storage, real-time match queue, rate limiting."),
            ("Firebase / Socket.IO","Real-time chat, push notifications, live match alerts."),
            ("Docker + Kubernetes*","Containerised deployment. *Phase 3 only — not needed for MVP."),
        ]
        for tech, desc in be:
            st.markdown(f"""<div class="slide-card" style="margin-bottom:0.4rem;padding:0.7rem 1rem;">
            <div style="font-weight:600;color:#c9a84c;font-size:0.85rem;">{tech}</div>
            <div style="font-size:0.78rem;color:#A4C3D2;margin-top:2px;">{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### 🤖 AI / ML & Cloud Infrastructure")
    ai_cols = [
        ("Compatibility Matching","OpenAI GPT-4 API + Custom ML","Analyses 40+ profile dimensions. Generates compatibility narrative."),
        ("Fake Profile Detection","Computer Vision + NLP (Python)","Detects stock photos, flags suspicious text. Fraud score per profile."),
        ("Vernacular NLP","Google Cloud Translation + Bhashini","India's Bhashini API for 22 official languages. Voice input transcription."),
        ("Photo Verification","AWS Rekognition","Detects real vs fake face. Liveness for video KYC."),
        ("Cloud Hosting","AWS (EC2, S3, RDS, Lambda)","1 EC2 t3.medium (~₹4,500/mo). S3 for photos. Auto-scale Phase 3."),
        ("CDN & Performance","Cloudflare + AWS CloudFront","Global CDN. DDoS protection. Image optimisation. ~₹1,500/mo."),
    ]
    c1, c2, c3 = st.columns(3)
    for i, (title, tech, desc) in enumerate(ai_cols):
        col = [c1, c2, c3][i % 3]
        with col:
            st.markdown(f"""<div class="rev-card" style="margin-bottom:0.5rem;">
            <div class="rev-title">{title}</div>
            <div class="rev-price" style="font-size:0.8rem;">{tech}</div>
            <div class="rev-desc" style="margin-top:0.3rem;">{desc}</div>
            </div>""", unsafe_allow_html=True)

# ─── PAGE: SUBSCRIPTIONS ─────────────────────────────────────────────────────
elif page == "Subscriptions & Tools":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 06</div>
    <div class="section-title">Subscriptions & Tools Needed</div>
    <div class="section-sub">Every tool you need — with exact monthly costs in Rupees</div>
    </div>""", unsafe_allow_html=True)

    categories = {
        "Hosting & Cloud": [
            ("AWS EC2 (t3.medium × 2)","₹9,000"),
            ("AWS S3 (500 GB photos)","₹1,200"),
            ("AWS RDS PostgreSQL","₹3,500"),
            ("DataDog (monitoring)","₹3,500"),
        ],
        "Dev & Security": [
            ("GitHub Pro (team)","₹1,700"),
            ("Cloudflare Pro","₹1,600"),
            ("Sentry (error tracking)","₹1,400"),
        ],
        "AI & APIs": [
            ("OpenAI GPT-4 API","₹6,000"),
            ("Bhashini API (language)","₹0 (gov free)"),
            ("AWS Rekognition (KYC)","₹2,500"),
            ("Google Maps API","₹1,500"),
        ],
        "Business Tools": [
            ("Razorpay (payments 2%)","₹0 + TXN fee"),
            ("Zoho Suite (CRM+mail)","₹2,000"),
            ("Slack (team comm.)","₹1,800"),
            ("Figma (design)","₹1,500"),
        ],
        "Communication": [
            ("Twilio (OTP SMS)","₹3,000"),
            ("SendGrid (emails)","₹1,500"),
            ("Firebase (push notif.)","₹0 (free tier)"),
        ],
        "Legal & Compliance": [
            ("Leegality (e-sign)","₹1,500"),
            ("AuthBridge (Aadhaar KYC)","₹2,500"),
            ("Cyber Insurance (annual)","₹5,500 (÷12)"),
        ],
    }
    c1, c2 = st.columns(2)
    for i, (cat, items) in enumerate(categories.items()):
        col = c1 if i % 2 == 0 else c2
        with col:
            html = f"""<div class="slide-card" style="margin-bottom:0.8rem;">
            <div class="slide-title">{cat}</div>"""
            for item, cost in items:
                html += f"""<div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #144272;font-size:0.82rem;">
                <span style="color:#e0ddd8;">{item}</span><span style="color:#c9a84c;font-weight:600;">{cost}</span></div>"""
            html += "</div>"
            st.markdown(html, unsafe_allow_html=True)

    st.markdown("""<div style="background:#06182c;border:1px solid #c9a84c;border-radius:6px;padding:0.7rem 1rem;font-size:0.82rem;color:#c9a84c;text-align:center;">
    PHASE 1 TOTAL MONTHLY CLOUD SPEND: ~₹45,000–55,000/month  ·  Scales to ₹2.5L/mo by Phase 3
    </div>""", unsafe_allow_html=True)

# ─── PAGE: TEAM ──────────────────────────────────────────────────────────────
elif page == "Team & Hiring":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 07</div>
    <div class="section-title">Team & Hiring Plan</div>
    <div class="section-sub">Who you need, when you need them, what to pay</div>
    </div>""", unsafe_allow_html=True)

    team = [
        ("P1","Co-Founder / CEO","Equity Only","Product vision, sales, fundraising","Day 1"),
        ("P1","Full-Stack Dev (Contract)","₹40–60K/mo","React Native, Node.js, PostgreSQL","Day 1"),
        ("P1","UI/UX Designer (Freelance)","₹25–35K/mo","Figma, mobile UX, vernacular UI","Day 1"),
        ("P2","Full-Stack Dev #2 (FT)","₹60–80K/mo","Backend APIs, AI integration","Month 6+"),
        ("P2","AI/ML Engineer","₹70–90K/mo","Python, TensorFlow, OpenAI","Month 6+"),
        ("P2","Marketing Manager","₹35–50K/mo","Digital ads, content, Tamil/Hindi","Month 6+"),
        ("P2","Customer Support Lead","₹20–30K/mo","CRM, grievance handling, Tamil","Month 6+"),
        ("P3","CTO (Co-Founder or Hire)","₹1.5–2.5L/mo","System design, team leadership","Month 12+"),
        ("P3","DevOps Engineer","₹80K–1.2L/mo","AWS, Docker, CI/CD pipelines","Month 12+"),
        ("P3","Data Protection Officer","₹60–80K/mo","DPDP Act compliance, legal-tech","Month 12+"),
    ]
    phase_colors = {"P1":"#27ae60","P2":"#3498db","P3":"#c9a84c"}
    st.markdown("""<table><tr><th>Phase</th><th>Role</th><th>Monthly Cost</th><th>Key Skills</th><th>When</th></tr>""", unsafe_allow_html=True)
    for phase, role, cost, skills, when in team:
        color = phase_colors.get(phase, "#fff")
        st.markdown(f"""<tr>
        <td><span style="background:{color};color:#000;padding:2px 8px;border-radius:3px;font-size:0.75rem;font-weight:700;">{phase}</span></td>
        <td style="font-weight:600;color:#fff;">{role}</td>
        <td style="color:#c9a84c;font-weight:600;">{cost}</td>
        <td style="font-size:0.8rem;color:#A4C3D2;">{skills}</td>
        <td style="font-size:0.8rem;">{when}</td>
        </tr>""", unsafe_allow_html=True)
    st.markdown("</table>", unsafe_allow_html=True)

# ─── PAGE: MARKETING ─────────────────────────────────────────────────────────
elif page == "Marketing & Growth":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 08</div>
    <div class="section-title">Marketing & Growth Strategy</div>
    <div class="section-sub">Getting your first 10,000 users without burning cash</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("#### 📢 Phase 1 Go-To-Market — ₹1.5L Budget · Max Impact")
    channels = [
        ("💬","Hyper-Local WhatsApp Groups","₹0","★★★★★","Share success stories in city-specific family groups. Tamil Nadu matrimony communities. Free and viral."),
        ("🛕","Community & Temple Tie-ups","₹10K","★★★★★","Partner with local temples, community centres, senior citizen groups. Offline flyers + QR code install."),
        ("📱","Instagram Reels + Tamil Content","₹40K/mo","★★★★☆","Short reels showcasing AI features, success stories, family testimonials. Paid boost on high performers."),
        ("🎓","College Alumni Referral Program","₹20K","★★★☆☆","NIT/IIT alumni networks. Offer 1 month premium for every successful referral."),
        ("🔍","Google Search Ads (Tamil Keywords)","₹30K/mo","★★★★☆","'Chennai matrimony', 'AI matchmaking', 'verified profiles' — high intent, low competition."),
        ("🎥","Influencer + YouTube (Tamil)","₹25K","★★★★☆","Micro-influencers (50K–200K followers). Marriage counsellors, family YouTubers."),
    ]
    c1, c2 = st.columns(2)
    for i, (icon, title, budget, roi, desc) in enumerate(channels):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""<div class="channel-card">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <div style="font-size:1.2rem;">{icon} <span class="channel-title">{title}</span></div>
              <div class="channel-budget">{budget}</div>
            </div>
            <div style="font-size:0.75rem;color:#f39c12;margin:3px 0;">ROI: {roi}</div>
            <div style="font-size:0.8rem;color:#A4C3D2;margin-top:4px;line-height:1.4;">{desc}</div>
            </div>""", unsafe_allow_html=True)

# ─── PAGE: FINANCIALS ────────────────────────────────────────────────────────
elif page == "Financial Projections":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 09</div>
    <div class="section-title">Financial Projections & KPIs</div>
    <div class="section-sub">Revenue roadmap — Month 1 to Month 36 (Conservative Model)</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("#### 📊 Monthly Revenue Growth (₹ Lakhs)")
    revenue_data = {
        "M6": 0.5, "M9": 2.0, "M12": 5.0, "M15": 10.0,
        "M18": 18.0, "M24": 35.0, "M30": 65.0, "M36": 120.0
    }
    # Simple bar chart using HTML
    max_val = 120.0
    bar_html = """<div style="background:#06182c;border:1px solid #144272;border-radius:8px;padding:1.5rem;">"""
    for month, val in revenue_data.items():
        pct = (val / max_val) * 100
        bar_html += f"""
        <div style="display:flex;align-items:center;margin-bottom:10px;gap:10px;">
          <div style="width:35px;font-size:0.75rem;color:#A4C3D2;text-align:right;">{month}</div>
          <div style="flex:1;background:#0A2647;border-radius:3px;height:24px;position:relative;">
            <div style="width:{pct}%;background:linear-gradient(90deg,#0A4D68,#c9a84c);height:100%;border-radius:3px;"></div>
          </div>
          <div style="width:65px;font-size:0.8rem;color:#c9a84c;font-weight:600;">₹{val}L</div>
        </div>"""
    bar_html += "</div>"
    st.markdown(bar_html, unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### 📋 3-Year KPI Table")
    st.markdown("""
    <table>
    <tr><th>Metric</th><th>Month 6</th><th>Month 12</th><th>Month 24</th></tr>
    <tr><td style="font-weight:600;">Registered Users</td><td>5,000</td><td>50,000</td><td>3,00,000</td></tr>
    <tr><td style="font-weight:600;">Verified Profiles</td><td>2,000</td><td>20,000</td><td>1,20,000</td></tr>
    <tr><td style="font-weight:600;">Paid Subscribers</td><td>100</td><td>1,000</td><td>8,000</td></tr>
    <tr><td style="font-weight:600;">Monthly Revenue</td><td style="color:#c9a84c;">₹50K</td><td style="color:#c9a84c;">₹5L</td><td style="color:#c9a84c;">₹35L</td></tr>
    <tr><td style="font-weight:600;">Monthly Burn</td><td style="color:#e74c3c;">₹4L</td><td style="color:#e74c3c;">₹12L</td><td style="color:#e74c3c;">₹28L</td></tr>
    <tr><td style="font-weight:600;">Net Profit/Loss</td><td style="color:#e74c3c;">-₹3.5L</td><td style="color:#e74c3c;">-₹7L</td><td style="color:#27ae60;">+₹7L</td></tr>
    <tr><td style="font-weight:600;">Break-even</td><td>—</td><td>—</td><td style="color:#27ae60;">Month 22</td></tr>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("""<div style="background:#06182c;border:1px solid #c9a84c;border-radius:6px;padding:0.7rem 1rem;font-size:0.82rem;color:#c9a84c;text-align:center;">
    Break-even at Month 22  ·  Profitable from Month 24  ·  Target ARR by Year 3: ₹14.4 Crore
    </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown("#### 🗺️ The 0 → 100 Roadmap")
    roadmap = [
        ("DAY 0","0","Register Pvt Ltd, open bank account, buy domain, set up GitHub"),
        ("MONTH 1","5","Wireframes done, hire 1 dev, begin MVP build, file DPDP compliance checklist"),
        ("MONTH 2–3","15","MVP app ready (Android beta), integrate Aadhaar KYC, soft launch Chennai with 500 users"),
        ("MONTH 4–5","30","1,000 verified profiles, launch paid subscriptions, first ₹10K revenue month"),
        ("MONTH 6–9","50","Expand to Hyderabad + Bangalore. 10,000 profiles. ₹1L+ MRR. Raise Angel round (₹20–50L)"),
        ("MONTH 10–15","70","iOS launch, 22-language support, family dashboard, 50,000 profiles, ₹10L MRR"),
        ("MONTH 16–24","85","Series A (₹2–5Cr). Pan-India launch. 3L profiles. Monthly break-even achieved."),
        ("MONTH 25–36","100","1M+ users. ₹1Cr+ MRR. NRI segment. B2B packages. Profitable. Series B ready."),
    ]
    c1, c2 = st.columns(2)
    for i, (period, score, desc) in enumerate(roadmap):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""<div class="roadmap-step">
            <div class="step-num">{period} · Progress: {score}/100</div>
            <div class="step-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)

# ─── PAGE: RISK REGISTER ─────────────────────────────────────────────────────
elif page == "Risk Register":
    st.markdown("""<div class="section-header">
    <div class="section-num">SECTION 10</div>
    <div class="section-title">Risk Register & Mitigation Plan</div>
    <div class="section-sub">Know your risks. Have the answer ready before launch.</div>
    </div>""", unsafe_allow_html=True)

    risks = [
        ("Trust in AI decisions","HIGH","Position AI as 'suggestion engine', not final authority. Family approval built in."),
        ("Cold-start (no users)","HIGH","Pre-seed 1,000 profiles via Chennai community partnerships BEFORE app launch."),
        ("Data breach","HIGH","Cyber insurance + AES-256 + ISO 27001 roadmap. DPDP breach protocol ready Day 1."),
        ("Fake profiles scale","MED","AI fraud score + manual review queue. No profile goes live without verification pass."),
        ("Caste filter legal risk","MED","User-chosen filters only. 'Community preference' framing. Legal counsel on retainer."),
        ("Cash runway running out","MED","Maintain 6-month runway always. Milestone-based fundraising. Revenue before Phase 2."),
        ("Competitor copy feature","LOW","Build moat via vernacular depth + family UX. Patent AI-Kundli hybrid matching method."),
        ("App Store rejection","LOW","Follow Apple/Google content policies. No adult content. Age verification in place."),
    ]
    sev_class = {"HIGH":"risk-high","MED":"risk-med","LOW":"risk-low"}
    st.markdown("""<table><tr><th>Risk</th><th>Severity</th><th>Mitigation Strategy</th></tr>""", unsafe_allow_html=True)
    for risk, sev, mit in risks:
        rc = sev_class.get(sev, "")
        st.markdown(f"""<tr class="{rc}"><td style="font-weight:600;color:#fff;">{risk}</td>
        <td>{sev}</td><td style="font-size:0.82rem;">{mit}</td></tr>""", unsafe_allow_html=True)
    st.markdown("</table>", unsafe_allow_html=True)

