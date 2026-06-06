import turtle
import pandas

screen = turtle.Screen()

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=600)

# dodavanje slika kao pozadine
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# all_states_upper = [s.upper() for s in all_states]
guessed_states = []

# dok je broj pogodjenih drzava manji od liste svih drzava igra traje
while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        #missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in guessed_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv", index=False)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())






# turtle.mainloop()
