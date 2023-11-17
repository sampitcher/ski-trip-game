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
Once a player takes all their ski lifts and returned to their starting point, the game ends. Then all points are tallied up and the player with the most points is the winner.
""")
         
st.divider()

st.write("""
# Game play
## A turn consists of either:
- Taking a lift
- Skiing a piste
When you take a lift, you must first pick a random card in the Game section on the left.
You finish your go either at the top or the bottom of a ski piste.
You cannot ski down a piste that is closed.
Every time you ski a piste, tally a mark in the appropriate piste colour section in the Piste Tally column.
         
## Ski Level
Every player starts at blue level. This means they can *only* ski down blue pistes.
After skiing a green or blue piste 5 times, this player is now red level and can now also ski down red pistes.
After skiing a red piste 5 times, this player is now black level and can now also ski down black pistes.
A played can never level down, but may level up from game cards.
Every time you ski a piste, take a tally in the Piste Tally column next to the colour you have skied.

## Wining points
There are 3 types of points in the game.
- Piste Points:
Tally each piste you ski throughout the game in the correct section.
At the end of the game, count up each coloured section.
Blue/Green pistes = 2 points each;
Red pistes = 3 points each;
Black pistes = 5 points each
- Lift Points:
Tally each lift you take from your Lift List.
At the end of the game, each lift you take from your list is worth 5 points.
- Card Points:
You may receive points throughout the game from cards you pick up before taking a lift.

# Game setup
There is a menu on the left with 2 other sections.
### Setup Game
Use this to choose your map and set up the board and playing bits.
### Game
Use this to play the game, here you can:
- Pick a card
- Hit a random button to see if you get a point or not
- Random number generator

# Winning the game
When someone takes all the lifts in their list, the game ends and everyone tallies their points, being sure to multiply the coloured tallies correctly as described in the Winning Points section above.
""")
         
st.divider()
    
    # with open("lifts.json") as lifts_file:
    #     st.session_state.lifts = json.loads(lifts_file.read())
    
    # with open("morzine_lifts.json") as morzine_lifts_file:
    #     st.session_state.morzine_lifts = json.loads(morzine_lifts_file.read())