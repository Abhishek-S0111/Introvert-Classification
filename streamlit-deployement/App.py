import streamlit as st
import pandas as pd

st.title("Are you the life of the party or the one ghosting it? Find out here.")

st.caption("We made a model that tries to guess if you're an introvert or extrovert — just answer some questions and let the algorithm judge you.")


time_spent_alone = st.slider("How much time are you by yourself daily?", 0 , 24)
stage_fear = st.radio("Do you believe yourself to have stage fear?",['Yes','No'])
social_event_attendance = st.number_input("How many social events do you attend in a day?", 0, 50)
going_outside = st.number_input("How often do you go outside in a day?", 0, 1000)
drained_after_socializing = st.radio("Do you feel drained after attending any social event?",['Yes','No'])
friend_circle_size = st.number_input("How large is your circle of friends?", 0 , 1000)
post_frequency = st.number_input("How frequently do you post on social media in a day?", 0, 1000)

