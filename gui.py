import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
class GUI:

    # constructor
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

        self.flag = False

        self.file_path = filedialog.askdirectory()

        # checking if given path is dir
        if ( self.checking_dir_correct(self.file_path) ):
            print("Loaded path:" + self.file_path)
            self.flag = True

        else:
            messagebox.showerror("Error","Your path isn't dir filepath")


    
    # function for checking if dir is correct
    def checking_dir_correct(self,src_string):
        return os.path.isdir(src_string)

