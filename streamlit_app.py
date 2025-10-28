import streamlit as st
import random
import time

# ------------------------- PAGE CONFIG -------------------------
st.set_page_config(page_title="HR Triage Router (Demo)", page_icon="💜", layout="wide")

# ------------------------- CUSTOM CSS -------------------------
st.markdown("""
<style>
body {
    background-color: #f8f5ff;
    font-family: 'Segoe UI', sans-serif;
    color: #3b0066;
}
h1, h2, h3 {
    color: #4b0082;
}
.stButton > button {
    background-color: #c5a3ff;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    padding: 0.6em 1.2em;
    transition: all 0.3s ease-in-out;
}
.stButton > button:hover {
    background-color: #a774ff;
    transform: scale(1.05);
}
.stTextInput > div > div > input {
    border: 2px solid #d2b7ff;
    border-radius: 8px;
}
.category-box {
    background-color: #ede3ff;
    padding: 12px;
    border-radius: 8px;
    border-left: 4px solid #a774ff;
    margin-bottom: 10px;
    box-shadow: 0 2px 6px rgba(155, 89, 182, 0.15);
}
.reply-box {
    background-color: #ffffff;
    padding: 14px;
    border-radius: 8px;
    border-left: 4px solid #b67fff;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
}
.fade-in {
    animation: fadeIn 1s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
.typing {
    border-right: .15em solid #b67fff;
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
    "Hi, I haven’t received my salary yet. Can you check?",
    "Where can I find the company leave policy?",
    "My medical claim hasn’t been reimbursed for 2 months.",
    "I want to update my bank details for payroll.",
    "How many annual leaves do I have left?",
    "My manager is asking about my bonus payout details.",
    "Urgent: I was locked out of the HR portal, need help asap!"
]

faq_answers = {
    "leave": "You can check your leave balance and apply via the HR self-service portal under 'My Leave'.",
    "benefits": "You can view your benefits and claim submissions through the Benefits Portal.",
    "payroll": "Payroll-related details are handled by the Payroll team. You can check pay slips in the HRIS system."
}

# ------------------------- HEADER -------------------------
st.title("💜 HR Triage Router (Demo)")
st.subheader("AI Front Desk Assistant for HR Support")

st.markdown("""
This **AI-powered demo** shows how HR can use automation to triage mixed queries,  
provide instant answers, and route urgent issues to the right team.
""")

# ------------------------- SIDEBAR -------------------------
st.sidebar.header("📬 HR Inbox Simulator")
selected_query = st.sidebar.selectbox("Select an incoming query:", [""] + sample_queries)
st.sidebar.markdown("💡 Choose a sample query to simulate AI routing.")

# ------------------------- MAIN LOGIC -------------------------
if selected_query:
    with st.spinner("AI analyzing the message..."):
        time.sleep(1.2)

    st.markdown(f"### Incoming Message")
    st.write(f"💬 *{selected_query}*")

    # Routing Logic
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
        response = "⚠️ This message has been flagged as **urgent** and routed to HRBP."
    else:
        category = "General"
        team = "HR Helpdesk"
        response = "Your query has been received and logged. We'll respond shortly."

    # ------------------------- DISPLAY -------------------------
    st.markdown(f"#### 🧩 Routed Category")
    st.markdown(f"<div class='category-box fade-in'><b>Category:</b> {category}<br><b>Assigned To:</b> {team}</div>", unsafe_allow_html=True)

    st.markdown("#### 🤖 Suggested AI Reply")
    unique_id = f"reply_{random.randint(1000,9999)}"
    st.markdown(f"<div id='{unique_id}' class='reply-box typing fade-in'></div>", unsafe_allow_html=True)

    # Inject JS typing effect dynamically
    st.markdown(f"""
    <script>
    typeEffect("{unique_id}", `{response}`, 30);
    </script>
    """, unsafe_allow_html=True)

    # ------------------------- ESCALATION OPTION -------------------------
    if st.button("🚨 Mark as Urgent & Escalate"):
        st.warning("This ticket has been escalated to HRBP.")
        st.balloons()

# ------------------------- ADD NEW QUERY -------------------------
st.markdown("---")
st.markdown("### 💌 Submit a New HR Query")

user_query = st.text_input("Type your HR-related question (demo only):")

if st.button("🔍 Analyze"):
    if user_query.strip() == "":
        st.error("Please enter a query.")
    else:
        st.success("Simulating AI routing... Check above sections for demo output.")
        st.info("In a live version, this would connect to an LLM + Zendesk/Freshdesk integration.")

# ------------------------- FOOTER -------------------------
st.markdown("""
---
💼 **Demo App by HR Team**  
Built with 💜 using Streamlit | Phase 1 (UI + Interaction Prototype)
""")
