from tkinter import *
from tkinter import filedialog

def askDirectory():
    try:
        text = filedialog.askdirectory()
        browseTxtField.delete(0, END)
        browseTxtField.insert(0, text)
        
    except ValueError:
        pass

root = Tk()
root.minsize(600, 100)
root.title('Browse folder')

browseBtn = Button(root,text='Browse',command=askDirectory)
browseBtn.grid(row=0,column=0,padx=(20,0),pady=(30,0),ipadx=30,ipady=4)

browseTxtField = Entry(root,text='')
browseTxtField.grid(row=0,column=1,padx=(35,0),pady=(30,0),ipadx=140,ipady=5)

if __name__ == "__main__":
    root.mainloop()
