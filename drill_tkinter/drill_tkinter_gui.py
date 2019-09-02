
import tkinter
from tkinter import *

import drill_tkinter_main
import drill_tkinter_func

def load_gui(self):
    
    self.varSource = StringVar()
    self.varDestination = StringVar()


    self.txtSource = Entry(self.master, text=self.varSource, font=("Helvetica", 13), fg='black', bg='white', width=33)
    self.txtSource.grid(row=0, column=1, padx=(40,0), pady=(50,0))

    self.txtDestination = Entry(self.master, text=self.varDestination, font=("Helvetica", 13), fg='black', bg='white', width=33)
    self.txtDestination.grid(row=1, column=1,  padx=(40,0), pady=(20,0))

    self.btnBrowse = Button(self.master, text="Browse...", width=13, height=1, command=lambda: drill_tkinter_func.findSource(self))
    self.btnBrowse.grid(row=0, column=0,  padx=(20,0), pady=(50,0))

    self.btnBrowse = Button(self.master, text="Browse...", width=13, height=1, command=lambda: drill_tkinter_func.findDestination(self))
    self.btnBrowse.grid(row=1, column=0,  padx=(20,0), pady=(20,0))

    self.btnCheck = Button(self.master, text="Check for files...", width=13, height=2, command=lambda: drill_tkinter_func.checkFiles(self))
    self.btnCheck.grid(row=2, column=0,  padx=(20,0), pady=(20,0))

    self.btnCancel = Button(self.master, text="Close Program", width=13, height=2)
    self.btnCancel.grid(row=2, column=1,  padx=(0,0), pady=(20,0), sticky=NE)

    drill_tkinter_func.create_db(self)

if __name__ == "__main__":
    pass
