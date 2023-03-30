import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(fun= player.move_forward, key="w")

cars.create_cars()

game_is_on = True
while game_is_on:

    time.sleep(0.07)
    screen.update()

    cars.move_cars()

    #WINNING A LEVEL
    if player.end_distance <= player.ycor():
        player.next_level()
        score_board.update_level()
        cars.next_level ()
    
    #DETECt COLLISION WITH CAR
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()