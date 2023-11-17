import streamlit as st
import random
import json

if 'cards' not in st.session_state:
    with open("cards.json") as cards_file:
        st.session_state.cards = json.loads(cards_file.read())

if st.button('Pick a card', key="pick"):
    if len(st.session_state.cards) == 0:
        with open("cards.json") as cards_file:
            st.session_state.cards = json.loads(cards_file.read())
    
    chosen_card = random.choice(st.session_state.cards)
    st.session_state.cards.remove(str(chosen_card))

    chosen_card_elements = chosen_card.split(" $ ")
    st.write(f"""
    # {chosen_card_elements[0]}
    ## {chosen_card_elements[1]}
             """)

st.divider()

if st.button('Random button', key="rand"):
    points_list = ["You got a point!", "Better luck next time!"]
    chosen_points = random.choice(points_list)
    st.write(f"""
    ## {chosen_points}
             """)

st.divider()

if st.button('Random number', key="rand_num"):
    rand_number = random.choice(range(10))
    st.write(f"""
    ## {rand_number}
             """)