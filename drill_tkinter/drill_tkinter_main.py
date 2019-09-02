#
# Python Ver:   3.7.3
#
# Author:       Mollie Zechlin
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 7.


from tkinter import *
import tkinter as tk
from tkinter import filedialog


# Be sure to import our other modules
# so we can have access to them
import drill_tkinter_gui
import drill_tkinter_func


# Frame is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(660, 240))
        self.master.title('Check files')
        self.master.config(bg='gray92')

        # load in the GUI widgets from a separate module,
        # keeping your code comparmentalized and clutter free
        drill_tkinter_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()




    

