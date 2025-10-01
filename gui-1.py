import tkinter as tk
from tkinter.ttk import Label
from model import *

root = tk.Tk()
root.title("Minesweeper")

height= 1
width= 3
buttons = [[None for _ in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        btn = tk.Button(root, width=3, height=1)
        btn.grid(row=i,column=j)
        btn.bind("<Button-1>", lambda e, r=i, c=j: on_left_click(r, c))
        btn.bind("<Button-3>", lambda e, r=i, c=j: on_right_click(r, c))

'''
def on_left_click(r, c):
    if grid[r][c] == '*':
        buttons[r][c].config(text="*", bg="red")
        # TODO: reveal all mines & disable buttons
    else:
        buttons[r][c].config(text=str(grid[r][c]), state="disabled")
'''

def on_left_click(row, col):
    row = row+1
    col = col+1
    if 0 <= row <= size and 0 <= col <= size:
        print(f"Left click on cell: ({row}, {col})")
        check_mine(row, col)

def on_right_click(row, col):
    row = row + 1
    col = col + 1
    if 0 <= row < size and 0 <= col < size:
        print(f"right click on cell: ({row}, {col})")

root.mainloop()