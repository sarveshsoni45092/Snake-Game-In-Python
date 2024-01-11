from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",12,'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day20/snakegame/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score : {self.score} | High Score {self.high_score}",move=False,align=ALIGNMENT,font=FONT)

    # def check_high_score(self):
    #     with open("Day20/snakegame/data.txt") as high_score_file:
    #         self.new_high_score = int(high_score_file.read())
    #         return self.new_high_score
        
    def reset(self):
        self.clear()
        if self.score > self.high_score :
            self.high_score = self.score

            with open("Day20/snakegame/data.txt","w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER !! Your Score is : {self.score}",move=False,align=ALIGNMENT,font=FONT)
    
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        