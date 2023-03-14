import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    if player.is_on_the_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.update_level()

    for car in car_manager.cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()