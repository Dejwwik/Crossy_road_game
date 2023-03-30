import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-210, 260)
        self.write_level()
    
    def write_level(self):
        self.clear()
        self.write(arg= f"Level: {self.level}", align= "center", font= FONT)
        
    def update_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0,0)
        self.write(arg= "GAME OVER!", align="center", font= FONT)