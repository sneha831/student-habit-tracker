import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Student Habit Tracker", layout="centered")

# Title
st.title("📚 Student Habit Tracker")

# Section: Input Form
st.header("📝 Log Your Daily Habits")

# Input fields
name = st.text_input("Your Name:")
dob = st.date_input("Date")

study_hours = st.slider("How many hours did you study today?", 0, 12, 4)
sleep_hours = st.slider("How many hours did you sleep last night?", 0, 12, 7)
screen_time = st.slider("Screen Time today (in hours)", 0, 12, 5)
mood = st.selectbox("How do you feel today?", ["Happy", "Tired", "Stressed", "Motivated"])
stress = st.slider("Stress Level (1 = Low, 5 = High)", 1, 5, 3)

submit = st.button("Submit Entry")

# Submit logic
if submit:
    new_data = {
        "Name": name,
        "Date": date.today(),
        "Study Hours": study_hours,
        "Sleep Hours": sleep_hours,
        "Screen Time (hrs)": screen_time,
        "Mood": mood,
        "Stress Level (1-5)": stress
    }

    try:
        df = pd.read_csv("habit_log.csv")
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([new_data])

    df.to_csv("habit_log.csv", index=False)
    st.success("Your entry has been saved!")

# Show past logs
st.header("📅 Past Logs")
try:
    df = pd.read_csv("habit_log.csv")
    st.dataframe(df)
except:
    st.info("No data yet. Add your first entry above.")
