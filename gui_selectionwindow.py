import tkinter as tk
from tkinter import messagebox

# class creating object for naming 
class Gui_selectionwindow:
    
    # function for getting data from entry 
    def get_data(self):
        if self.entry.get() != "":
            print("Selected name: " + self.entry.get())

            self.return_data = self.entry.get()
            self.root.dispose()
        else:
            messagebox.showerror("Input error","Your input is blank!")
            pass

    # constructor
    def __init__(self,string_prompt,string_title,string_button,width_px,height_px):
        # field for user input
        self.return_data = ""

        self.window_message = string_prompt
        self.window_title = string_title
        self.button_title = string_button

        self.width_px_entry = width_px/2
        self.height_px_entry = height_px/2

        # setting root window
        self.root = tk.Tk()

        # getting canvas on the root window
        self.main_canvas = tk.Canvas(self.root,width = width_px,height = height_px)
        self.main_canvas.pack()

        # setting input box
        self.entry = tk.Entry(self.root)

        # creating window
        self.main_canvas.create_window(self.width_px_entry,self.height_px_entry,window=self.entry)

        self.button1 = tk.Button(self.root,text=self.button_title,command = self.get_data,
                        bg = "black",fg = "white", font = ("helvetica",9,"bold"))
        
        self.main_canvas.create_window(self.width_px_entry,self.height_px_entry+50,window = self.button1)

        self.root.mainloop()




