import shutil, os
from datetime import *
from tkinter import *
from tkinter import filedialog

source = ''
destination = ''
files = None

def centerWindow(root, w, h):
    x = int(root.winfo_screenwidth()/2 - w/2)
    y = int(root.winfo_screenheight()/2.5 - h/2)
    return root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

def setSource():
    global source
    global files
    try:
        source = '{}/'.format(filedialog.askdirectory())
        sourceField.delete(0, END)
        sourceField.insert(0, source)
        files = os.listdir(source)
        
    except ValueError:
        pass
    
def setDestination():
    global destination
    try:
        destination = '{}/'.format(filedialog.askdirectory())
        destinationField.delete(0, END)
        destinationField.insert(0, destination)
        
    except ValueError:
        pass

def initialize():
    for i in files:
        dateModified = datetime.fromtimestamp(os.path.getmtime(source+i))
        dateCreated = datetime.fromtimestamp(os.path.getctime(source+i))
        yesterday = datetime.now() - timedelta(days=1)
        
        if dateModified > yesterday and dateCreated > yesterday:
            print('{} was moved.'.format(i))
            shutil.move(source+i,destination)
        else:
            print('{} was not moved.'.format(i))
            continue

root = Tk()
root.title('File Transfer')
root.minsize(650,200)
root.maxsize(650,200)
root.resizable(0,0)
root.configure(bg='#f9f9fa')
centerWindow(root,650,250)

info = Label(root,bg='#f9f9fa',text='This program checks if the .txt files in a specified source folder were modified or \ncreated in the last 24 hours. It then sends those files to a specified destination folder.')
info.grid(row=0,column=0,columnspan=3,padx=(35,0),pady=(15,0))

sourceBtn = Button(root,text='Source',command=setSource)
sourceBtn.grid(column=0,row=1,padx=(38,10),pady=(15,5),ipadx=29,ipady=4)

sourceField = Entry(root,width=75)
sourceField.grid(column=1,row=1,columnspan=2,pady=(11,0),ipady=4)

destinationBtn = Button(root,text='Destination',command=setDestination)
destinationBtn.grid(column=0,row=2,padx=(38,10),pady=(5,10),ipadx=17,ipady=4)

destinationField = Entry(root,width=75)
destinationField.grid(column=1,row=2,columnspan=2,pady=(0,3),ipady=4)

initiateBtn = Button(root,text='Start',command=initialize)
initiateBtn.grid(column=2,row=3,ipadx=35,ipady=5,sticky='E')

if __name__ == "__main__":
    root.mainloop()
