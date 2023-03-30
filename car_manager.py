import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.2

class CarManager(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.level = 1
        self.hideturtle()
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):

        for _ in range(35):
            new_car = turtle.Turtle()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x= random.randint(250, 1100), y= random.randint(-235, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            xcord = car.xcor() - self.move_distance
            ycord = car.ycor()
            car.goto(xcord, ycord)
        self.check_for_end_xcord()
    
    def next_level(self):
        self.level += 1
        self.move_distance += MOVE_INCREMENT
        for car in self.cars:
            self.reset_car(car)
    
    def check_for_end_xcord(self):
        for car in self.cars:
            if car.xcor() < -300:
                self.reset_car(car)
                
    def reset_car(self, car):
        car.goto(x= random.randint(300, 1100), y= random.randint(-235, 250))