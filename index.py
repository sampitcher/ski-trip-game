import streamlit as st
import json

st.set_page_config(
    page_title="Ski Game",
    page_icon="⛷️",
)
        
st.sidebar.success("Select a demo above.")

st.write("""
# Welcome to The Ski Trip Game
All you need to play is:
- Piste Map
- Counters
- Pen and Paper
""")

st.divider()

st.write("""
# Aim of the game
First player to 10 points is the winner, there are a number of ways to get points:
- 2 points when you get to a ski lift that is chosen for you
- 2 points when you get to a ski lift chosen for the group
- Points are awarded in the cards
""")
         
st.divider()

if 'cards' not in st.session_state:
    with open("cards.json") as cards_file:
        st.session_state.cards = json.loads(cards_file.read())
    with open("morzine_lifts.json") as morzine_lifts_file:
        st.session_state.morzine_lifts = json.loads(morzine_lifts_file.read())