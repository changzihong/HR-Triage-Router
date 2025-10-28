import streamlit as st
import time
import random

# ------------------------- PAGE CONFIG -------------------------
st.set_page_config(page_title="Smart HR Dashboard - HR Triage Router", page_icon="🤖", layout="wide")

# ------------------------- CUSTOM CSS -------------------------
st.markdown("""
<style>
body {
    background-color: #f8f4ff;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3 {
    color: #5e35b1;
}
.metric-card {
    background: linear-gradient(145deg, #ede7f6, #d1c4e9);
    padding: 18px;
    border-radius: 14px;
    box-shadow: 3px 3px 8px rgba(0,0,0,0.1);
    text-align: center;
    transition: all 0.3s ease;
}
.metric-card:hover {
    transform: scale(1.03);
    box-shadow: 5px 5px 12px rgba(0,0,0,0.15);
}
.query-box {
    background-color: #ffffff;
    border-left: 6px solid #9575cd;
    border-radius: 10px;
    padding: 14px;
    margin: 10px 0;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
}
.reply-box {
    background: #f3e5f5;
    padding: 14px;
    border-radius: 10px;
    border-left: 5px solid #7e57c2;
    box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
}
.category-badge {
    background: #b39ddb;
    color: white;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------- JAVASCRIPT EFFECT -------------------------
st.markdown("""
<script>
function highlightBox() {
    const boxes = document.querySelectorAll('.query-box');
    boxes.forEach(box => {
        box.addEventListener('mouseenter', () => {
            box.style.boxShadow = '0px 4px 12px rgba(94,53,177,0.4)';
            box.style.transition = '0.3s';
        });
        box.addEventListener('mouseleave', () => {
            box.style.boxShadow = '0px 2px 5px rgba(0,0,0,0.1)';
        });
    });
}
window.addEventListener('load', highlightBox);
</script>
""", unsafe_allow_html=True)

# ------------------------- HEADER -------------------------
st.markdown("<h1 style='text-align:center;'>📊 Smart HR Dashboard (Demo Metrics)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#6a1b9a;'>AI-Powered Front Desk Assistant for HR Support Routing & Automation</p>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------- METRICS DASHBOARD -------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='metric-card'><h3>📨 Total Queries</h3><h2>152</h2><p>+12 today</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'><h3>⚡ Auto-Routed</h3><h2>86%</h2><p>AI handled without manual input</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-card'><h3>🚀 Avg Response Time</h3><h2>1.3 min</h2><p>LLM instant replies</p></div>", unsafe_allow_html=True)

st.markdown("---")

# ------------------------- SIMULATED DATA -------------------------
sample_queries = [
    "I haven’t received my salary yet. Can you check?",
    "Where can I find the company leave policy?",
    "My medical claim hasn’t been reimbursed for 2 months.",
    "I want to update my bank details for payroll.",
    "How many annual leaves do I have left?",
    "Urgent: Locked out of HR portal, need help asap!"
]

faq_answers = {
    "leave": "You can check your leave balance via the HR self-service portal under 'My Leave'.",
    "benefits": "Benefits and claims are managed through the Benefits Portal.",
    "payroll": "Payroll-related queries are handled by the Payroll team in HRIS.",
}

# ------------------------- INCOMING QUERIES (3 COLUMN LAYOUT) -------------------------
st.markdown("### 💬 Incoming Queries (Auto-Triage Simulation)")
query_cols = st.columns(3)

for i, q in enumerate(sample_queries[:3]):
    with query_cols[i]:
        st.markdown(f"<div class='query-box'><b>Query:</b> {q}</div>", unsafe_allow_html=True)

# ------------------------- SELECTION & TRIAGE -------------------------
st.markdown("---")
selected_query = st.selectbox("🔍 Choose a query to analyze:", [""] + sample_queries)

if selected_query:
    with st.spinner("🤖 AI analyzing query..."):
        time.sleep(1.5)

    st.markdown(f"<div class='query-box'><b>Incoming Message:</b><br>{selected_query}</div>", unsafe_allow_html=True)

    if any(w in selected_query.lower() for w in ["salary", "bonus", "bank", "pay"]):
        category = "Payroll"
        team = "Payroll Support Team"
        response = faq_answers["payroll"]
    elif any(w in selected_query.lower() for w in ["leave", "vacation", "holiday"]):
        category = "Leave"
        team = "Leave & Attendance Team"
        response = faq_answers["leave"]
    elif any(w in selected_query.lower() for w in ["benefit", "claim", "medical"]):
        category = "Benefits"
        team = "Benefits Admin Team"
        response = faq_answers["benefits"]
    elif "urgent" in selected_query.lower() or "asap" in selected_query.lower():
        category = "Escalation"
        team = "HR Business Partner (HRBP)"
        response = "⚠️ Urgent issue – escalated to HRBP immediately."
    else:
        category = "General"
        team = "HR Helpdesk"
        response = "Thank you. Your query has been received and will be routed shortly."

    st.markdown(f"#### 🧩 Routed Category: <span class='category-badge'>{category}</span>", unsafe_allow_html=True)
    st.markdown(f"**Assigned To:** {team}")
    st.markdown(f"<div class='reply-box'>{response}</div>", unsafe_allow_html=True)

    if st.button("🚨 Escalate to HRBP"):
        st.warning("This query has been escalated to HRBP.")
        st.balloons()

# ------------------------- NEW QUERY -------------------------
st.markdown("---")
st.markdown("### ✉️ Submit a New Query (Demo Mode)")
user_query = st.text_input("Enter your HR-related question:")

if st.button("📬 Send Query"):
    if user_query.strip():
        st.success("Query submitted for AI triage simulation!")
    else:
        st.error("Please enter a query before submitting.")

# ------------------------- FOOTER -------------------------
st.markdown("""
---
<p style='text-align:center;color:#9575cd;'>💼 Smart HR Dashboard Demo | Powered by Streamlit & LLM Mock Engine</p>
""", unsafe_allow_html=True)
