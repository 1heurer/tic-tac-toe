from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap('game.ico')

counter = 0
win = False

# field location and possible win combinations | v:vertical, h: horizontal, d: diagonal
fields = {
    1: ["field1", 0, 0, "v1", "h1", "d1"],
    2: ["field2", 0, 2, "v2", "h1"],
    3: ["field3", 0, 4, "v3", "h1", "d2"],
    4: ["field4", 2, 0, "v1", "h2"],
    5: ["field5", 2, 2, "v2", "h2", "d1", "d2"],
    6: ["field6", 2, 4, "v3", "h2"],
    7: ["field7", 4, 0, "v1", "h3", "d2"],
    8: ["field8", 4, 2, "v2", "h3"],
    9: ["field9", 4, 4, "v3", "h3", "d1"]
}

# keeps track of entries and will increase by 1 if corresponding field is clicked. If a entry == 3 -> win
tracker = {
    "playerO": {
        # vertical rows
        "v1": 0,
        "v2": 0,
        "v3": 0,
        # horizontal rows
        "h1": 0,
        "h2": 0,
        "h3": 0,
        # diagonal rows
        "d1": 0,
        "d2": 0
    },
    "playerX": {
        # vertical rows
        "v1": 0,
        "v2": 0,
        "v3": 0,
        # horizontal rows
        "h1": 0,
        "h2": 0,
        "h3": 0,
        # diagonal rows
        "d1": 0,
        "d2": 0
    }
}


# resets the game
def reset():
    global tracker
    global counter
    global win

    # resets tracker entries
    for i in tracker:
        for k in tracker[i]:
            tracker[i][k] = 0

    # resets buttons
    field1_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(1))
    field2_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(2))
    field3_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(3))
    field4_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(4))
    field5_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(5))
    field6_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(6))
    field7_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(7))
    field8_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(8))
    field9_r = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(9))

    field1_r.grid(row=0, column=0)
    field2_r.grid(row=0, column=2)
    field3_r.grid(row=0, column=4)
    field4_r.grid(row=2, column=0)
    field5_r.grid(row=2, column=2)
    field6_r.grid(row=2, column=4)
    field7_r.grid(row=4, column=0)
    field8_r.grid(row=4, column=2)
    field9_r.grid(row=4, column=4)

    win = False


def click(field_num):
    global counter
    global win
    print(fields)

    if counter <= 9:
        # checks for current player
        if counter % 2 == 0:
            player_symbol = "X"
            player = "playerX"
        else:
            player_symbol = "O"
            player = "playerO"

        counter += 1

        # updates field with player symbol and disables it
        field_update = Button(root, text=player_symbol, height=10, width=22, bg="#E1FFFB", command=lambda: click(field_num), state=DISABLED)
        field_update.grid(row=fields[field_num][1], column=fields[field_num][2])

        # adds entry to tracker
        for i in fields[field_num][3::]:
            tracker[player][i] += 1

        print(f"{player}: {tracker[player]}")

        # checks if any of player entries in tracker == 3 -> win
        for i in tracker[player]:
            # if true -> win
            if tracker[player][i] == 3:
                print(f"Game ended! {player} wins the game!")
                messagebox.showinfo("Game ended", f"{player} wins the game!")
                win = True
                counter = 0
                reset()
            else:
                pass

        print(counter)

        # checks for draw
        if counter == 9 and win is False:
            messagebox.showinfo("Game ended", "It's a draw!")
            counter = 0
            reset()


# creating fields
field1 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(1))
field2 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(2))
field3 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(3))
field4 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(4))
field5 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(5))
field6 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(6))
field7 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(7))
field8 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(8))
field9 = Button(root, height=10, width=22, bg="#E1FFFB", command=lambda: click(9))

# creating grid
grid_vertical1 = Frame(root, height=161, width=15, bg="black")
grid_vertical2 = Frame(root, height=161, width=15, bg="black")
grid_vertical3 = Frame(root, height=161, width=15, bg="black")
grid_vertical4 = Frame(root, height=161, width=15, bg="black")
grid_vertical5 = Frame(root, height=161, width=15, bg="black")
grid_vertical6 = Frame(root, height=161, width=15, bg="black")

grid_horizontal1 = Frame(root, height=15, width=522, bg="black")
grid_horizontal2 = Frame(root, height=15, width=522, bg="black")

# placing first row
field1.grid(row=0, column=0)
grid_vertical1.grid(row=0, column=1)
field2.grid(row=0, column=2)
grid_vertical2.grid(row=0, column=3)
field3.grid(row=0, column=4)

# first horizontal line
grid_horizontal1.grid(row=1, column=0, columnspan=5)

# placing second row
field4.grid(row=2, column=0)
grid_vertical3.grid(row=2, column=1)
field5.grid(row=2, column=2)
grid_vertical4.grid(row=2, column=3)
field6.grid(row=2, column=4)

# second horizontal line
grid_horizontal2.grid(row=3, column=0, columnspan=5)

# placing third row
field7.grid(row=4, column=0)
grid_vertical5.grid(row=4, column=1)
field8.grid(row=4, column=2)
grid_vertical6.grid(row=4, column=3)
field9.grid(row=4, column=4)


root.mainloop()
