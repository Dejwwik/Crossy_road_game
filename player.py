import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.75,0.75)
        self.setheading(90)
        self.color("black")
        self.penup()
        self.end_distance = FINISH_LINE_Y
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)