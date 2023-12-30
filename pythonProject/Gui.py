import PySimpleGUI as gui


def layout_generator(x=4):

    layout = [
        # rows and columns of the board
        [[gui.Text(" ☐ ") for col in range(x)] for row in range(x)],
        # Start and Rest buttons
        [gui.Button('start'), gui.Button('reset')]]
    return layout


window = gui.Window("Game", layout_generator())

# event that keeps the window open until user exits the game.
while True:
    event, values = window.read()
    if event == "OK" or event == gui.WIN_CLOSED:
        break

window.close()