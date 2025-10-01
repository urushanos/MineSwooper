import tkinter as tk
from model import *

root = tk.Tk()
root.title("Minesweeper")


buttons = [[None for _ in range(size)] for _ in range(size)]
place_mines()
place_numbers()

# build UI and store button refs
for i in range(size):
    for j in range(size):
        btn = tk.Button(root, width=3, height=1, text="")
        btn.grid(row=i, column=j)
        # note: lambda captures i,j as defaults so each button gets its own coords
        btn.bind("<Button-1>", lambda e, r=i, c=j: on_left_click(r, c))
        btn.bind("<Button-3>", lambda e, r=i, c=j: on_right_click(r, c))
        buttons[i][j] = btn

def refresh_ui():
    """Update all buttons from model state: grid, grid_hash, grid_flag."""
    for r in range(size):
        for c in range(size):
            b = buttons[r][c]
            val = grid_hash[r][c]
            flagged = grid_flag[r][c]

            if val == '#':
                # hidden cell
                if flagged == 1:
                    b.config(text="F", state=tk.NORMAL, bg="SystemButtonFace")
                else:
                    b.config(text="", state=tk.NORMAL, bg="SystemButtonFace")
            elif val == "F":
                # (In case your model uses 'F' in grid_hash)
                b.config(text="F", state=tk.NORMAL, bg="SystemButtonFace")
            else:
                # revealed (either '0' or '1'..'8')
                # show numbers as disabled (revealed)
                if val == '0':
                    b.config(text="", state=tk.DISABLED, relief=tk.SUNKEN)
                else:
                    b.config(text=val, state=tk.DISABLED, relief=tk.SUNKEN)

def reveal_all_mines():
    """Reveal all mines in the UI using the model grid."""
    for r in range(size):
        for c in range(size):
            if grid[r][c] == '*':
                buttons[r][c].config(text="*", bg="red", state=tk.DISABLED)

# Handler for left click: open cell
def on_left_click(row, col):
    # row,col are already 0-based because lambda passed i,j
    # If cell is flagged, ignore left click
    if grid_flag[row][col] == 1:
        return

    # if clicked a mine -> reveal all mines and game over behavior
    if grid[row][col] == '*':
        reveal_all_mines()
        buttons[row][col].config(bg="darkred")
        # optionally disable all buttons
        for r in range(size):
            for c in range(size):
                buttons[r][c].unbind("<Button-1>")
                buttons[r][c].unbind("<Button-3>")
        # you can also pop up a message here
        return

    # otherwise call model flood-fill (check_mine expects 0-based indices)
    check_mine(row, col)

    # refresh ui from grid_hash
    refresh_ui()

# Handler for right click: toggle flag
def on_right_click(row, col):
    # toggle flag only if cell not revealed
    if grid_hash[row][col] != '#':
        # already revealed -> ignore flagging
        return

    if grid_flag[row][col] == 0:
        grid_flag[row][col] = 1
        grid_hash[row][col] = "F"   # keep UI consistent with your textual model
    else:
        grid_flag[row][col] = 0
        grid_hash[row][col] = "#"

    refresh_ui()

# initial UI refresh (all hidden)
refresh_ui()

root.mainloop()
