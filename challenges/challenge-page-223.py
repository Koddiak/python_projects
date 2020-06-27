from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(600,210)
        self.master.maxsize(600,210)
        self.master.title("Check files")
        center_window(self, 600, 210)
        
        self.browseButton1 = Button(self.master,text="Browse...")
        self.browseButton1.grid(row=0,column=0,padx=(20,0),pady=(50,0),ipadx=30,ipady=4)

        self.browseTxtField1 = tk.Entry(self.master,text='')
        self.browseTxtField1.grid(row=0,column=1,padx=(35,0),pady=(50,0),ipadx=140,ipady=5)

        self.browseButton2 = Button(self.master,text="Browse...")
        self.browseButton2.grid(row=1,column=0,padx=(20,0),pady=(12,0),ipadx=30,ipady=4)

        self.browseTxtField2 = tk.Entry(self.master,text='')
        self.browseTxtField2.grid(row=1,column=1,padx=(35,0),pady=(12,0),ipadx=140,ipady=5)

        self.checkButton = Button(self.master,text="Check for files...")
        self.checkButton.grid(row=2,column=0,padx=(20,0),pady=(12,0),ipadx=12,ipady=10)

        self.closeButton = Button(self.master,text="Close Program")
        self.closeButton.grid(row=2,column=1,padx=(328,0),pady=(12,0),ipadx=12,ipady=10)

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

if __name__ == "__main__":
    root = tk.Tk()
    ParentWindow(root)
    root.mainloop()
