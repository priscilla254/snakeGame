from turtle import Turtle


FONT=('Montserrat', 24, 'normal')
ALIGN='center'
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"score:{self.current_score}", align=ALIGN, font= FONT)
    def increase_score(self):
        self.current_score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGN,font=FONT)
