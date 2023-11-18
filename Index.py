import streamlit as st
import json
from PIL import Image

st.set_page_config(
    page_title="Ski Game",
    page_icon="⛷️"
)
        
st.sidebar.success("⛷️")

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
Embark on the ski trip of a life time across any resort in the world. Play against your family and friends to ski hard and take 6 lifts that are specifc to each player.
As part of the game setup, each player will be given a list of ski lifts that they need to naviagate to around the resort. Once a player takes all their designated ski lifts and returned to their starting point, the game ends. Then all points are tallied up and the player with the most points is the winner.
""")

st.write("""
On the left of this page there is a navigation bar with 3 pages:
- Index. You are here now! The instructions of the game.
- Setup Game. Here you set up the game board and the scoresheet.
- Game. Navigate here when you start playing the game. Here you randomly generate the game cards.
""")

st.divider()

st.write("""
# Game play

## Wining points
In the game setup you will create or print out your score sheet where you can tally points. There are 3 types of points in the game.
- Piste Points:
Tally each piste you ski down throughout the game in the Piste Points section.
At the end of the game, count up each coloured section.
Blue/Green pistes = 2 points each;
Red pistes = 3 points each;
Black pistes = 5 points each
- Lift Points:
Mark off each lift you take from your Lift List.
At the end of the game, each lift you take from your list is worth 5 points.
- Card Points:
You may receive points throughout the game from cards you pick up before taking a lift. The ammount of points is displayed on the card.

Here is an example scoresheet at the end of the game.
""")
image = Image.open('example_scoresheet.png')
st.image(image, caption='Score Sheet')

st.write("""
## Ski Level
Every player starts at blue level. This means they can *only* ski down blue pistes.
After skiing a green or blue piste 5 times, this player is now red level and can now also ski down red pistes.
After skiing a red piste 5 times, this player is now black level and can now also ski down black pistes.
A player can never level down, but may also level up from game cards. (Note the example sheet leveled up to black level having only skied 4 red pistes).
Every time you ski a piste, take a tally in the Piste Points column next to the colour you have skied.

## A players turn
A turn consists of either taking a lift *or* skiing a piste:
- Taking a lift.
When you take a lift, you must first pick a random card in the Game section before taking the lift. If you take a lift on your list, you can cross that lift out and you get 5 points at the end of the game. You don't need to say which lift you want to take.
- Skiing a piste.
You finish your go either at the top or the bottom of a ski piste.
You cannot ski down a piste that is closed.
Every time you ski a piste, tally a mark in the appropriate piste colour section in the Piste Points column on your scoresheet.
When skiing, you may continue to ski as far as you want before stopping at a lift. When doing so, tally a mark for every colour of piste that you touch.
""")

st.write("""
## Game setup
There is a menu on the left with 2 other sections:
#### Setup Game
Use this to choose your resort map and set up the board and playing pieces.
#### Game
Use this to play the game, here you can:
- Pick a card
- Random number generator

# Winning the game
When someone takes all the lifts in their list, the game ends and everyone tallies their points, being sure to multiply the coloured tallies correctly as described in the Winning Points section above. Happy skiing!!
""")
         
st.divider()
    
    # with open("lifts.json") as lifts_file:
    #     st.session_state.lifts = json.loads(lifts_file.read())
    
    # with open("morzine_lifts.json") as morzine_lifts_file:
    #     st.session_state.morzine_lifts = json.loads(morzine_lifts_file.read())