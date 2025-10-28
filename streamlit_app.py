import streamlit as st
import time
import random

# ------------------------- PAGE CONFIG -------------------------
st.set_page_config(page_title="HR Triage Router (AI Front Desk)", page_icon="🤖", layout="wide")

# ------------------------- ADVANCED CSS -------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f8f6ff, #f1ecff);
    font-family: 'Segoe UI', sans-serif;
    color: #2e004f;
}
h1, h2, h3, h4 {
    color: #4b0082;
}
.stButton>button {
    background: linear-gradient(90deg, #a774ff, #8250ff);
    color: white;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    font-weight: bold;
    transition: 0.3s ease;
    border: none;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #b98fff, #a06eff);
    transform: scale(1.05);
}
.query-card {
    display: inline-block;
    vertical-align: top;
    background-color: #ffffff;
    padding: 12px 16px;
    border-radius: 12px;
    box-shadow: 0 3px 8px rgba(140, 82, 255, 0.15);
    margin: 0 10px 10px 0;
    border-left: 4px solid #a774ff;
    width: 260px;
    transition: transform 0.3s ease;
}
.query-card:hover {
    transform: translateY(-2px);
}
.query-scroll {
    white-space: nowrap;
    overflow-x: auto;
    padding: 10px 5px;
}
.category-box {
    background-color: #f3eaff;
    padding: 12px;
    border-radius: 8px;
    border-left: 4px solid #a774ff;
    box-shadow: 0px 2px 4px rgba(100,0,200,0.1);
}
.chat-box {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 15px;
    border: 1px solid #e0caff;
    max-width: 85%;
    animation: fadeIn 1s ease;
}
.chat-human {
    text-align: right;
    margin: 10px 0;
}
.chat-ai {
    text-align: left;
    margin: 10px 0;
}
.metric-box {
    background-color: #ede3ff;
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(5px);}
    to {opacity: 1; transform: translateY(0);}
}
.typing {
    border-right: .15em solid #a774ff;
    white-space: nowrap;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# ------------------------- JAVASCRIPT -------------------------
st.markdown("""
<script>
function typeEffect(elementId, text, speed=35){
    let i = 0;
    let target = document.getElementById(elementId);
    target.innerHTML = "";
    let typer = setInterval(function(){
        if (i < text.length){
            target.innerHTML += text.charAt(i);
            i++;
        } else {
            clearInterval(typer);
        }
    }, speed);
}
</script>
""", unsafe_allow_html=True)

# ------------------------- SIMULATED DATA -------------------------
sample_queries = [
    {"sender": "employee1@company.com", "text": "Hi, I haven’t received my salary yet. Can you check?"},
    {"sender": "employee2@company.com", "text": "Where can I find the company leave policy?"},
    {"sender": "employee3@company.com", "text": "My medical claim hasn’t been reimbursed for 2 months."},
    {"sender": "employee4@company.com", "text": "Urgent: I was locked out of the HR portal, need help asap!"},
    {"sender": "employee5@company.com", "text": "Can I update my bank details for salary credit?"}
]

faq_answers = {
    "leave": "You can view your leave policy and balance via the HR Self-Service Portal → My Leave.",
    "benefits": "Check your benefits and medical claims in the Benefits Portal. Ensure your receipts are uploaded.",
    "payroll": "Payroll queries are handled by our Payroll team. Please check your HRIS for payslip release status."
}

# ------------------------- HEADER -------------------------
st.title("💜 HR Triage Router — AI Front Desk Assistant")
st.markdown("Empower your HR helpdesk with smart triage, instant replies, and escalation automation.")
st.markdown("---")

# ------------------------- INCOMING QUERY VIEWER (TOP) -------------------------
st.subheader("📥 Incoming Queries")
st.markdown('<div class="query-scroll">', unsafe_allow_html=True)

for msg in sample_queries:
    st.markdown(f"""
    <div class="query-card">
        <b>From:</b> {msg['sender']}<br>
        <b>Message:</b><br>{msg['text']}
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

selected_query = st.selectbox("🔍 Select a query to analyze:", [m["text"] for m in sample_queries])

# ------------------------- AI ROUTING LOGIC -------------------------
if selected_query:
    with st.spinner("AI analyzing message..."):
        time.sleep(1.3)

    if any(word in selected_query.lower() for word in ["salary", "bonus", "pay", "bank"]):
        category = "Payroll"
        team = "Payroll Support Team"
        response = faq_answers.get("payroll")
    elif any(word in selected_query.lower() for word in ["leave", "vacation", "holiday"]):
        category = "Leave"
        team = "Leave & Attendance Team"
        response = faq_answers.get("leave")
    elif any(word in selected_query.lower() for word in ["benefit", "medical", "claim"]):
        category = "Benefits"
        team = "Benefits Admin Team"
        response = faq_answers.get("benefits")
    elif "urgent" in selected_query.lower() or "asap" in selected_query.lower():
        category = "Escalation"
        team = "HR Business Partner (HRBP)"
        response = "⚠️ This message has been marked urgent and sent to HRBP."
    else:
        category = "General"
        team = "HR Helpdesk"
        response = "Your query has been received. We'll route it to the right department."

    st.markdown("---")
    st.subheader("🧠 AI Routing & Auto-Response")
    st.markdown(f"<div class='category-box'><b>Category:</b> {category}<br><b>Assigned To:</b> {team}</div>", unsafe_allow_html=True)

    st.markdown("##### 💬 Conversation Preview")
    st.markdown(f"<div class='chat-human chat-box'>👩‍💼: {selected_query}</div>", unsafe_allow_html=True)

    unique_id = f"reply_{random.randint(1000,9999)}"
    st.markdown(f"<div id='{unique_id}' class='chat-ai chat-box typing'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <script>
    typeEffect("{unique_id}", "🤖: {response}", 25);
    </script>
    """, unsafe_allow_html=True)

    if st.button("🚨 Escalate to HRBP"):
        st.warning("Escalation sent to HRBP successfully.")
        st.balloons()

# ------------------------- METRICS DASHBOARD -------------------------
st.markdown("---")
st.subheader("📊 Smart HR Dashboard (Demo Metrics)")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class='metric-box'>
        <b>Queries Processed Today</b><br>
        <h3>124</h3>
        <progress value="85" max="100"></progress><br>
        <small>85% Auto-Resolved</small>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='metric-box'>
        <b>Avg Response Time</b><br>
        <h3>1.8 min</h3>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class='metric-box'>
        <b>Escalations</b><br>
        <h3>6 Today</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("💼 **Developed by HR Innovation Lab | Phase 1 – Advanced Dashboard Prototype** 💜")
