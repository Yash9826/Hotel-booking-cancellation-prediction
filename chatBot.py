
# code with simple
import streamlit as st
import requests

st.set_page_config(page_title="Hotel Chatbot", page_icon="🏨")

st.title("🏨 Hotel Booking Prediction Chatbot")

# Define questions (only numeric + text as plain input)
questions = [
    ("lead_time", "How many days before arrival is the booking?", "number"),
    ("stays_in_weekend_nights", "How many weekend nights?", "number"),
    ("stays_in_week_nights", "How many week nights?", "number"),
    ("adults", "Number of adults?", "number"),
    ("children", "Number of children?", "number"),
    ("meal", "Meal plan (BB, HB, FB, SC)", "text"),
    ("market_segment", "Market segment (Direct, Corporate, Online TA, Offline TA/TO)", "text"),
    ("is_repeated_guest", "Repeated guest? (0=No, 1=Yes)", "number"),
    ("deposit_type", "Deposit type (No Deposit, Non Refund, Refundable)", "text"),
    ("previous_cancellations", "Previous cancellations?", "number"),
    ("total_of_special_requests", "Number of special requests?", "number"),
    ("adr", "Average Daily Rate (ADR)?", "number")
]

if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

# Ask one question at a time
if st.session_state.current_q < len(questions):
    key, question, qtype = questions[st.session_state.current_q]
    st.write(f"**Bot:** {question}")
    user_input = st.text_input("Your answer:", key=f"q_{st.session_state.current_q}")

    if st.button("Submit"):
        if user_input.strip():
            # Convert number if required
            if qtype == "number":
                try:
                    user_input = float(user_input)
                except:
                    st.error("Please enter a valid number")
                    st.stop()

            st.session_state.answers[key] = user_input
            st.session_state.current_q += 1
            st.rerun()

else:
    # All questions answered
    st.write("✅ All questions answered. Sending to backend...")

    payload = {"features": st.session_state.answers}
    try:
        response = requests.post("http://localhost:5000/chat", json=payload)
        result = response.json()

        if "error" in result:
            st.error(result["error"])
        else:
            pred = "Cancelled" if result["prediction"] == 1 else "Not Cancelled"
            prob = result["probability"]
            explanation = result["explanation"]

            st.success(f"Prediction: {pred} (prob={prob:.2f})")
            st.info(explanation)

        if st.button("Restart"):
            st.session_state.answers = {}
            st.session_state.current_q = 0
            st.rerun()

    except Exception as e:
        st.error(f"Backend error: {e}")
