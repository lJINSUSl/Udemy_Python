import turtle
import pandas as pd
from name import Name
from scoreboard import Scoreboard

name = Name()
scoreboard = Scoreboard()

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pd.read_csv('50_states.csv')

guessed_states = []
all_states = data.state.to_list()
print(all_states)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{scoreboard.score}/50 Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if (data['state'] == answer_state).any():
        answer = data[data['state'] == answer_state]
        coor = (int(answer.x), int(answer.y))
        print(coor, answer.state)

        name.city_write(f"{answer_state}",coor)
        scoreboard.reset_score()
        guessed_states.append(answer_state)
    if answer_state == 'Exit':
        break
remains = [x for x in all_states if x not in guessed_states]
remains = pd.DataFrame(remains)
remains.to_csv('remain.csv')
turtle.mainloop()