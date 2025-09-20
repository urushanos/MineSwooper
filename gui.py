import tkinter
from tkinter.ttk import Label

m= tkinter.Tk(className='MineSwooper')

welcome="Happy Sweeping gang!"
title=Label(m, text=welcome)
title.pack()

m.mainloop()