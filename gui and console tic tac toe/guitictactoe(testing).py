import tkinter as tk
import winsound


a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '


marked_list = []
xWin = False
game_end = False
xturn = True
draw = False
oturn = False

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")
root.resizable(False, False)
status_label = tk.Label(root, text="x turn", font=("Quicksand", 16))
status_label.grid(row=3, column=0, columnspan=3)



buttons = {}

def update_turn():
    buttons['a1'].config(text=a1)
    buttons['a2'].config(text=a2)
    buttons['a3'].config(text=a3)
    buttons['b1'].config(text=b1)
    buttons['b2'].config(text=b2)
    buttons['b3'].config(text=b3)
    buttons['c1'].config(text=c1)
    buttons['c2'].config(text=c2)
    buttons['c3'].config(text=c3)


    for pos, btn in buttons.items():
        value = globals()[pos]
        btn.config(text=value)

        if value == 'x':
            btn.config(bg='pink')
        elif value == 'o':
            btn.config(bg='purple')
        else:
            btn.config(bg='SystemButtonFace')


def x_changeboard(m):
    global a1, a2, a3, c1, c2, c3, b1, b2, b3, xturn, oturn, marked_list
    valid_input = True

    if m in marked_list:
        print("position taken")
        return

    if game_end == False and valid_input == True:
        if m == 'a1':
            a1 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m)       
        if m == 'a2':
            a2 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m) 
        if m == 'a3':
            a3 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m)
        if m == 'b1':
            b1 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m) 
        if m == 'b2':
            b2 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m) 
        if m == 'b3':
            b3 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m) 
        if m == 'c1':
            c1 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m) 
        if m == 'c2':
            c2 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m) 
        if m == 'c3':
            c3 = 'x'
            xturn = False
            oturn = True
            marked_list.append(m)

    winsound.PlaySound("moves.wav", winsound.SND_ASYNC)

def o_changeboard(m):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, xturn, oturn, marked_list
    valid_input = True

    if m in marked_list:
        print("position taken")
        return

    if game_end == False and valid_input == True:
        if m == 'a1':
            a1 = 'o'
            oturn = False
            xturn = True       
            marked_list.append(m)       
        if m == 'a2':
            a2 = 'o'
            oturn = False
            xturn = True
            marked_list.append(m) 
        if m == 'a3':
            a3 = 'o'
            oturn = False
            xturn = True
            marked_list.append(m)
        if m == 'b1':
            b1 = 'o'
            oturn = False
            xturn = True
            marked_list.append(m) 
        if m == 'b2':
            b2 = 'o'
            oturn = False
            xturn = True
            marked_list.append(m) 
        if m == 'b3':
            b3 = 'o'
            oturn = False
            xturn = True
            marked_list.append(m) 
        if m == 'c1':
            c1 = 'o'
            oturn = False
            xturn = True
            marked_list.append(m) 
        if m == 'c2':
            c2 = 'o'
            oturn = False
            xturn = True
            marked_list.append(m) 
        if m == 'c3':
            c3 = 'o'
            oturn = False
            xturn = True
            marked_list.append(m)

    winsound.PlaySound("moves.wav", winsound.SND_ASYNC)


           



def check_winner():
    global game_end


    if (
        (a1 == 'x' and a2 == 'x' and a3 == 'x') or
        (b1 == 'x' and b2 == 'x' and b3 == 'x') or
        (c1 == 'x' and c2 == 'x' and c3 == 'x') or
        (a1 == 'x' and b1 == 'x' and c1 == 'x') or
        (a2 == 'x' and b2 == 'x' and c2 == 'x') or
        (a3 == 'x' and b3 == 'x' and c3 == 'x') or
        (a1 == 'x' and b2 == 'x' and c3 == 'x') or
        (a3 == 'x' and b2 == 'x' and c1 == 'x')
    ):
        print("X wins")
        game_end = True
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
        return

    
    if (
        (a1 == 'o' and a2 == 'o' and a3 == 'o') or
        (b1 == 'o' and b2 == 'o' and b3 == 'o') or
        (c1 == 'o' and c2 == 'o' and c3 == 'o') or
        (a1 == 'o' and b1 == 'o' and c1 == 'o') or
        (a2 == 'o' and b2 == 'o' and c2 == 'o') or
        (a3 == 'o' and b3 == 'o' and c3 == 'o') or
        (a1 == 'o' and b2 == 'o' and c3 == 'o') or
        (a3 == 'o' and b2 == 'o' and c1 == 'o')
    ):
        print("O wins")
        game_end = True
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
        return

def button_click(position):
    global xturn, oturn, game_end

    if xturn:
        x_changeboard(position)
        status_label.config(text="o turn")
        update_turn()
    elif oturn:
        o_changeboard(position)
        status_label.config(text="x turn")
        update_turn()        

    check_winner()

position = [
    ['a1', 'a2', 'a3'],
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3']
]      

for row in range(3):
    for col in range(3):
        pos = position[row][col]
        btn = tk.Button(root, text=' ', font=('Quicksand', 20), width = 5, height = 2, command=lambda p=pos: button_click(p))
        btn.grid(row=row, column=col)
        buttons[pos] = btn

root.mainloop()        

