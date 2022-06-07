from turtle import Screen, Turtle
from frame import Frame
from scoreboard import Scoreboard
from nought import Nought
from cross import Cross
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Noughts and Crosses")
screen.bgcolor("black")
screen.tracer(2)

frame = Frame()
scoreboard = Scoreboard()
nought = Nought()
cross = Cross()
turtle = Turtle()


CLICKS_NO = 0
CROSS_COORDS_LIST = []
NOUGHT_COORDS_LIST = []

# Noughts and Crosses frame is divided into 9 sections. These are those sections centre coordinates
SECTION_CENTRE_COORDS = [(-100, 100), (0, 100), (100, 100), (-100, 0), (0, 0), (100, 0), (-100, -100),
                         (0, -100), (100, -100)]


# Goes through the list of winning coordinate combinations
def win(coords_list):
    winning_list = [[(-100, 100), (0, 100), (100, 100)], [(-100, 0), (0, 0), (100, 0)], [(-100, -100),
                    (0, -100), (100, -100)], [(-100, 100), (-100, 0), (-100, -100)], [(0, 100), (0, 0), (0, -100)],
                    [(100, 100), (100, 0), (100, -100)], [(-100, 100), (0, 0), (100, -100)], [(100, 100), (0, 0),
                    (-100, -100)]]
    for winner in winning_list:
        result = all(elem in coords_list for elem in winner)
        if result:
            return True


# Resets the game after crosses or noughts win or a draw.
def reset_game():
    global CLICKS_NO, CROSS_COORDS_LIST, NOUGHT_COORDS_LIST, SECTION_CENTRE_COORDS
    screen.onclick(None)
    time.sleep(2)
    nought.clear()
    cross.clear()
    CROSS_COORDS_LIST = []
    NOUGHT_COORDS_LIST = []
    CLICKS_NO = 0
    SECTION_CENTRE_COORDS = [(-100, 100), (0, 100), (100, 100), (-100, 0), (0, 0), (100, 0), (-100, -100),
                             (0, -100), (100, -100)]
    screen.onscreenclick(draw_on_click)


def draw_on_click(x, y):
    global CLICKS_NO, CROSS_COORDS_LIST, NOUGHT_COORDS_LIST
    click_coords = (x, y)
    distances = []
    for sec_coords in SECTION_CENTRE_COORDS:
        # Computes the distance between mouse click coordinates and SECTION_CENTRE_COORDINATES
        coords = ((click_coords[0] - sec_coords[0]) ** 2 + (click_coords[1] - sec_coords[1]) ** 2) ** 0.5
        distances.append(coords)
    # In the distances list finds min distance value
    min_distance = min(distances)
    #checks if min distance is within 50 points of SECTION_CENTRE_CORDINATES.
    if min_distance <= 100:
        # In the distances list finds min value and gets it's index. Then from SECTION_CENTRE_COORDINATES list
        # gets coordinates with the index
        new_coords = SECTION_CENTRE_COORDS[distances.index(min_distance)]
        # Deletes coordinates that have been used by cross or nought, so you couldn't draw on top of them
        del SECTION_CENTRE_COORDS[distances.index(min_distance)]
        if CLICKS_NO < 9:
            if CLICKS_NO % 2 == 0:
                cross.draw_cross(new_coords[0], new_coords[1])
                # Keeps a list of so far used crosses coordinates
                CROSS_COORDS_LIST.append(new_coords)
                # Checks if any of 3 coordinates in CROSS_COORDS_LIST are winning combination
                crosses_win = win(CROSS_COORDS_LIST)
                CLICKS_NO += 1
                if crosses_win:
                    scoreboard.crosses_won()
                    reset_game()
                    scoreboard.cross_point()
            elif CLICKS_NO % 2 != 0:
                nought.draw_nought(new_coords[0], new_coords[1])
                # Keeps a list of so far used noughts coordinates
                NOUGHT_COORDS_LIST.append(new_coords)
                # Checks if any of 3 coordinates in CROSS_COORDS_LIST are winning combination
                noughts_win = win(NOUGHT_COORDS_LIST)
                CLICKS_NO += 1
                if noughts_win:
                    scoreboard.noughts_won()
                    reset_game()
                    scoreboard.nought_point()
        if CLICKS_NO == 9:
            cross.draw_cross(new_coords[0], new_coords[1])
            scoreboard.draw()
            reset_game()
            scoreboard.draw_point()


screen.onscreenclick(draw_on_click)

screen.mainloop()

