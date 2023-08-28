from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())

        self.penup()
        self.hideturtle()
        self.pencolor('white')

    def board(self):
        self.clear()
        self.goto(0,280)
        self.write(f'Score: {self.score}. High Score: {self.high_score}',move=True, align = 'center')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.board()



    # def game_over(self):
    #     self.goto(-30,0)
    #     self.write('Game Over')