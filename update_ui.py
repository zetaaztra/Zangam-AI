import sys

file_path = "c:/Users/hp/Desktop/Sangam-AI/sangam_ai_app.py"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Colors
text = text.replace("#0d3b35", "#0A2647")
text = text.replace("#082e29", "#06182c")
text = text.replace("#1d6557", "#144272")
text = text.replace("#0f4a41", "#0f385c")
text = text.replace("#0b5c4e", "#0A4D68")
text = text.replace("#a8c5be", "#A4C3D2")

# 2. Emojis
emojis_map = {
    "🏠 Cover & Overview": "Cover & Overview",
    "🎯 Vision & Business Model": "Vision & Business Model",
    "📊 Market Analysis": "Market Analysis",
    "🗺️ Investment Plan": "Investment Plan",
    "⚖️ Legal Setup": "Legal Setup",
    "💻 Tech Stack": "Tech Stack",
    "🛠️ Subscriptions & Tools": "Subscriptions & Tools",
    "👥 Team & Hiring": "Team & Hiring",
    "📣 Marketing & Growth": "Marketing & Growth",
    "💰 Financial Projections": "Financial Projections",
    "🚦 Risk Register": "Risk Register",
    "🔍 Audit Notes": "Audit Notes",
    "### 💍 SANGAM AI": "### SANGAM AI",
    "page_icon=\"💍\"": "page_icon=\"💎\""
}

for old, new in emojis_map.items():
    text = text.replace(old, new)


# 3. Add 'By Pravin A'
target_name = '''        <div style="font-size:1rem; color:#c9a84c; margin-top:0.5rem;">
            Pan-India AI-Powered Matrimonial Platform
        </div>'''
replacement_name = '''        <div style="font-size:1rem; color:#c9a84c; margin-top:0.5rem;">
            Pan-India AI-Powered Matrimonial Platform
        </div>
        <div style="font-size:1.2rem; color:#f0ede8; margin-top:1.5rem; font-weight:600; letter-spacing:1px; font-style:italic;">
            By Pravin A
        </div>'''
text = text.replace(target_name, replacement_name)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)
print("Changes applied!")
