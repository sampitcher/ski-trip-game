import streamlit as st
import random
import json

st.write("""
# Let's setup the game
""")

st.divider()
st.write(
    """
    ### 0. Initial set up
    - Lay a piste map on the table, this is the board
    - Each player needs 2 counters (beer caps, coins anything.) One is for the player, one is to close a piste.
    - Each player need a pen and paper, explained below
    """)

st.divider()
st.write("### 1. Which resort are you in?")

option = st.selectbox(
    'Ski Resorts:',
    ('Morzine Les Gets', 'Avoriaz', 'Portes du Soleil', 'Grand Massif'))

# st.write('You are in', option)
options = {
    'Morzine Les Gets': 'morzine_les_gets',
    'Avoriaz': 'avoriaz',
    'Portes du Soleil': 'portes_du_soleil',
    'Grand Massif': 'grand_massif'
}

st.divider()
st.write("### 2. Each player grab a pen and paper. Divide it into 3 columns to look like this:")
col1, col2, col3 = st.columns(3)

with col1:
   st.write("#### My points!")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.write("#### List of ski lifts")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.write(
       """
       #### My level
       - Blue
       - Red
       - Black
       """)
#    st.image("https://static.streamlit.io/examples/owl.jpg")

st.divider()
st.write("""
         ### 3. Grab your paper and pen, then click below to generate a list of ski lifts you need to get to.
         Each player has their own list that they can choose to hide from the other players. Each player takes it in turns to generate a list for themselves. Note: players could share the same lifts they need to take.
         """)

with open("lifts.json") as lifts_file:
    lifts = json.loads(lifts_file.read())
         
if st.button('Generate a list of lifts', key="lifts"):
    try:
        selected_station_lifts = lifts[options[option]]
        st.write("Here are the lifts that each player needs to get to, when you get there you get 2 points.")
        st.write(random.sample(selected_station_lifts, 6))
        st.write("Write them down in the middle column!")
    except:
        st.write("resort not available")

st.divider()
st.write("""
         ### 4. Each player can put their playing token at any starting point on the map
         A starting point is any lift at the bottom of the map that is accessible. This is normally a car park or bus stop.
         """)

st.divider()
st.write("### 5. Each player can put their barrier token on a ski lift of their choice to close the lift")

st.divider()
st.write("""
         ### 6. Head to the Game section in the menu on the left and HIT THE SLOPES!
         Youngest player goes first and then play clockwise.
         """)