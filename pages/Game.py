import streamlit as st
# from streamlit_card import card
import random
import json

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

    # my_card = card(
    #     title = chosen_card_elements[0],
    #     text = chosen_card_elements[1]
    # )

else:
    # st.write('Goodbye')
    pass