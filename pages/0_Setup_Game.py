import streamlit as st
import random

st.write("""
# How many players?
""")

number = st.number_input("Insert a number", value=2, format="%i", placeholder="How many players?")
st.write(f'There are {number} players!')

st.divider()

st.write("""
# Let's see where people need to go!
""")
         
if st.button('Generate a list of lifts', key="lifts"):
    lifts = []
    for i in range(5):
        generated_lift = random.choice(st.session_state.morzine_lifts)
        st.session_state.morzine_lifts.remove(str(generated_lift))
        st.write(f"{generated_lift}")