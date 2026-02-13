import tkinter
from tkinter import font
import winsound

def play_click():
    try:
        winsound.PlaySound("moves.wav", winsound.SND_ASYNC)
    except:
        pass

def play_win():
    try:
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
    except:
        pass



def set_tile(row, column):
    global curr_turn

    if game_end:
        return

    if board[row][column]['text'] != "":
        return
    
    play_click()

    board[row][column]['text'] = curr_turn
    check_win()

    if curr_turn == oturn:
        curr_turn = xturn
    else:
        curr_turn = oturn

def check_win():
    global turns, game_end
    turns += 1

    # Horizontal
    for row in range(3):
        if (board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] 
            and board[row][0]['text'] != ""):
            label.config(text=board[row][0]['text'] + " wins!", foreground=color_bleu)
            play_win()
            for column in range(3):
                board[row][column].config(foreground=color_bleu, background='lightgray')
            game_end = True
            return

    # Vertical
    for column in range(3):
        if (board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] 
            and board[0][column]['text'] != ""):
            label.config(text=board[0][column]['text'] + " wins!", foreground=color_bleu)
            play_win()
            for row in range(3):
                board[row][column].config(foreground=color_bleu, background='lightgray')
            game_end = True
            return

    # Main diagonal
    if (board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] 
        and board[0][0]['text'] != ""):
        label.config(text=board[0][0]['text'] + " wins!", foreground=color_bleu)
        play_win()
        for i in range(3):
            board[i][i].config(foreground=color_bleu, background='lightgray')
        game_end = True
        return

    # Anti-diagonal
    if (board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] 
        and board[0][2]['text'] != ""):
        label.config(text=board[0][2]['text'] + " wins!", foreground=color_bleu)
        play_win()
        for i in range(3):
            board[i][2-i].config(foreground=color_bleu, background='lightgray')
        game_end = True
        return

    # Draw
    if turns == 9:
        label.config(text="It's a Draw!")
        game_end = True

           


def new_game():
    global turns, curr_turn, game_end

    play_click()

    turns = 0
    game_end = False
    
    label.config(text=curr_turn + "'s turn", foreground=color_pink) 

    for row in range(3):
        for column in range(3):
            board[row][column].config(text = "", foreground=color_bleu, background=color_pink)
            board[row][column].config(foreground='#FAA0A0', background=color_pink)


# setup
xturn = 'x'
oturn = 'o'
curr_turn = xturn
turns = 0
game_end = False

board = [[0, 0 , 0],
         [0, 0 , 0],
         [0, 0 , 0]]

color_bleu = "#5D768B"
color_beige = "#C8B39B"
color_gold = "#E3C9A4"
color_pink = "#F2D9C7"

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_turn + "'s turn", font=("Consolas", 20), background=color_beige, 
                      foreground=color_pink)
label.grid(row=0, column=0, columnspan=3, sticky="we")

label.grid(row=0, column=0)

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text= "", font=("Consolas", 50, 'bold'),
                                            background=color_pink, foreground='#FAA0A0', width=3, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)


button = tkinter.Button(frame, text="Reset", font=("Consolas", 20), background=color_beige, 
                        foreground=color_bleu, command=new_game)


button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# centralize the window on the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

windowX = int((screen_width / 2) - (window_width / 2))
windowY = int((screen_height / 2) - (window_height / 2))

# format the window position
window.geometry(f"{window_width}x{window_height}+{windowX}+{windowY}")


window.mainloop()


