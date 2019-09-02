
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Be sure to import our other modules
# so we can have access to them
import drill_tkinter_main
import drill_tkinter_gui

# Ask Directory
def findDir1(self):
    filePath = tk.filedialog.askdirectory()
    self.txtDir1.insert(0,filePath)

def findDir2(self):
    filePath = tk.filedialog.askdirectory()
    self.txtDir2.insert(0,filePath)
    


if __name__ == "__main__":
    pass
                    





            






















        
