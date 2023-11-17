import streamlit as st
import json

st.set_page_config(
    page_title="Ski Game",
    page_icon="⛷️",
)
        
st.sidebar.success("Enjoy.")

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
- 2 points when you get to a ski lift that is chosen from the setup
- Points are awarded in the random cards
""")
         
st.divider()

st.write("""
# Game play
## A turn consists of either:
- taking a lift
- skiing a piste
When you take a lift, you must first pick a random card in the Game section on the left.
You finish your go either at the top or the bottom of a ski run.
""")
         
st.divider()

if 'cards' not in st.session_state:
    with open("cards.json") as cards_file:
        st.session_state.cards = json.loads(cards_file.read())
    
    # with open("lifts.json") as lifts_file:
    #     st.session_state.lifts = json.loads(lifts_file.read())
    
    # with open("morzine_lifts.json") as morzine_lifts_file:
    #     st.session_state.morzine_lifts = json.loads(morzine_lifts_file.read())