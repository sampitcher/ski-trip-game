import streamlit as st
from streamlit_card import card
import random
import json

if 'cards' not in st.session_state:
    with open("cards.json") as cards_file:
        st.session_state.cards = json.loads(cards_file.read())
    with open("morzine_lifts.json") as morzine_lifts_file:
        st.session_state.morzine_lifts = json.loads(morzine_lifts_file.read())

st.write("""
# Welcome to The Ski Trip Game
Go and grab:
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

if st.button('Pick a card', key="pick"):
    if len(st.session_state.cards) == 0:
        with open("cards.json") as cards_file:
            st.session_state.cards = json.loads(cards_file.read())
    
    chosen_card = random.choice(st.session_state.cards)
    st.session_state.cards.remove(str(chosen_card))

    st.write(chosen_card)
    chosen_card_elements = chosen_card.split(" $ ")

    my_card = card(
        title = chosen_card_elements[0],
        text = chosen_card_elements[1]
    )

else:
    # st.write('Goodbye')
    pass