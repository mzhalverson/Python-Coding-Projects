
import os
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import shutil

# Be sure to import our other modules
# so we can have access to them
import drill_tkinter_main
import drill_tkinter_gui

# Ask Directory
def findSource(self):
    filePath = tk.filedialog.askdirectory()
    self.txtSource.insert(0,filePath)

def findDestination(self):
    filePath = tk.filedialog.askdirectory()
    self.txtDestination.insert(0,filePath)
    
def checkFiles(self):

    var_source = self.txtSource.get()
    var_destination = self.txtDestination.get()
    
    if (len(var_source) > 0) and (len(var_destination) > 0) : # enforce the user to provide both names
        conn = sqlite3.connect('moved_files.db')
        with conn:
            cursor = conn.cursor()

            file_list = os.listdir(var_source)
            for file in file_list:
                name, ext = os.path.splitext(file)        
                if ext == '.txt':
                    abspath = os.path.join(var_source, file)
                    last_rev = os.path.getmtime(abspath)
                    print(abspath, '\n', last_rev)

                    cursor.execute("""INSERT INTO tbl_files (col_file, col_time_stamp) VALUES (?,?)""",(file,last_rev))
                    shutil.move(abspath, var_destination)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")


def create_db(self):
    conn = sqlite3.connect('moved_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file TEXT, \
            col_time_stamp TEXT \
            );")
        # You must commit() to save changes & close th database connection
        conn.commit()
    conn.close()


if __name__ == "__main__":
    pass
                    





            






















        
