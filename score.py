from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
COLOR = "white"
POS_X = 0
POS_Y = 268
START_X = 0
START_Y = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.highscore = int(file.read())
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.goto(POS_X, POS_Y)
        self.text = f"Score: {self.score}  High Score: {self.highscore}"
        self.write(self.text, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.text = f"Score: {self.score}  High Score: {self.highscore}"
        self.write(self.text, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.highscore}")
            self.score = 0
            self.update_scoreboard()

    # def game_over(self):
    #     self.goto(START_X, START_Y)
    #     self.text = "Game over."
    #     self.write(self.text, align=ALIGNMENT, font=FONT)

