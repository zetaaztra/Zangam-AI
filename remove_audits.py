import re

file_path = "c:/Users/hp/Desktop/Sangam-AI/sangam_ai_app.py"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Remove sidebar link
text = text.replace('        "Audit Notes",\n', '')

# 2. Remove all standalone st.markdown audit boxes
pattern = r'(\s*st\.markdown\("""\s*<div class="audit-box".*?</div>\s*""", unsafe_allow_html=True\))'
text = re.sub(pattern, '', text, flags=re.DOTALL)

# 3. Remove the entire PAGE: AUDIT NOTES section at the end
page_pattern = r'\n# ─── PAGE: AUDIT NOTES ───────────────────────────────────────────────────────.*'
text = re.sub(page_pattern, '\n', text, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Audit notes removed.")
