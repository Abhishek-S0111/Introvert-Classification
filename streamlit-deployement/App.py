import streamlit as st
import pandas as pd
import joblib

def map_bool(data):
    "Works only for Yes/No form of boolean data"
    for i in data.columns:
        if(type(data[i].iloc[0]) == str):
            data[i] = data[i].map({'Yes':1,'No':0})

st.title("Are you the life of the party or the one ghosting it? Find out here.")

st.caption("We made a model that tries to guess if you're an introvert or extrovert — just answer some questions and let the algorithm judge you.")


time_spent_alone = st.slider("How much time are you by yourself daily?", 0 , 24)
stage_fear = st.radio("Do you believe yourself to have stage fear?",['Yes','No'])
social_event_attendance = st.number_input("How many social events do you attend in a day?", 0, 50)
going_outside = st.number_input("How often do you go outside in a day?", 0, 1000)
drained_after_socializing = st.radio("Do you feel drained after attending any social event?",['Yes','No'])
friend_circle_size = st.number_input("How large is your circle of friends?", 0 , 1000)
post_frequency = st.number_input("How frequently do you post on social media in a day?", 0, 1000)

data = pd.DataFrame({
    "Time_spent_Alone":time_spent_alone,
    "Stage_fear":stage_fear,
    "Social_event_attendance":social_event_attendance,
    "Going_outside":going_outside,
    "Drained_after_socializing":drained_after_socializing,
    "Friends_circle_size":friend_circle_size,
    "Post_frequency":post_frequency
}, index = [1])

map_bool(data)

model = joblib.load("../model/introvert_classifier_model.pkl")

if st.button("Predict"):
    pred = model.predict(data)
    st.write(f"You are an {"Introvert" if pred == 1 else "Extrovert"}")