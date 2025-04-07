import streamlit as st
import datetime
import random

# Set page config
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="centered")

# Header
st.title("🌱 Growth Mindset Challenge Web App")
st.subheader("Unlock Your Potential with a Growth Mindset!")

# Tabs for organization
tab1, tab2, tab3, tab4 = st.tabs(["📖 Learn", "📝 Reflect", "🎯 Set Goals", "🧠 Quiz Yourself"])

# TAB 1: LEARN
with tab1:
    st.header("What is a Growth Mindset?")
    st.write("""
    A **growth mindset** means believing you can improve your abilities through dedication and hard work.
    This view creates a love of learning and resilience that is essential for success.
    """)
    st.markdown("---")
    st.subheader("Core Beliefs of a Growth Mindset")
    st.markdown("""
    ✅ Challenges help me grow  
    ✅ Feedback is constructive  
    ✅ I can learn anything I want  
    ✅ My effort makes me stronger  
    ✅ I am inspired by others' success  
    """)
    st.image("https://i.imgur.com/F0l0gXS.png", caption="Growth Mindset vs Fixed Mindset")

# TAB 2: REFLECT
with tab2:
    st.header("Daily Reflection Journal")
    st.write("Reflect on your journey and how you've practiced a growth mindset today.")

    today = datetime.date.today()
    reflection = st.text_area(f"🗓️ {today} - What did you learn today? How did you overcome a challenge?", height=200)

    if st.button("💾 Save Reflection"):
        with open("reflections.txt", "a") as f:
            f.write(f"{today}: {reflection}\n")
        st.success("Reflection saved successfully!")

# TAB 3: GOAL SETTING
with tab3:
    st.header("Set a Learning Goal")
    st.write("Focus on what you'd like to improve or learn next.")

    goal = st.text_input("🎯 What's one skill or concept you'd like to improve this week?")
    deadline = st.date_input("⏳ Set a deadline", value=datetime.date.today() + datetime.timedelta(days=7))

    if st.button("✅ Set Goal"):
        st.success(f"Goal set: _{goal}_ by {deadline.strftime('%B %d, %Y')}. Stay committed!")

# TAB 4: QUIZ
with tab4:
    st.header("Test Your Growth Mindset Knowledge")

    quiz = {
        "You failed a math test. What do you do?": {
            "options": [
                "Give up. Math isn't for me.",
                "Learn from mistakes and try again.",
                "Ignore it and move on."
            ],
            "answer": 1
        },
        "Which statement reflects a growth mindset?": {
            "options": [
                "I'm just not a creative person.",
                "If I try hard enough, I can improve.",
                "Some people are just born smart."
            ],
            "answer": 1
        }
    }

    score = 0
    for question, content in quiz.items():
        user_answer = st.radio(question, content["options"], key=question)
        if st.button("Check Answer", key=question + "_btn"):
            correct = content["answer"]
            if content["options"].index(user_answer) == correct:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Oops! The right answer was: {content['options'][correct]}")

    st.markdown("🎉 Reflect on your answers and keep learning!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Growth Mindset Challenge 2025")

