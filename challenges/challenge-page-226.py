from tkinter import *
from tkinter import filedialog

filename = ''
userText = 'Stay tuned for our amazing summer sale!'
file = None

def centerWindow(root, w, h):
    x = int(root.winfo_screenwidth()/2 - w/2)
    y = int(root.winfo_screenheight()/2.5 - h/2)
    centerGeo = root.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def save():
    while True:
        try:
            userText = textField.get('1.0',END)
            filename = filedialog.asksaveasfilename(initialdir = '/',title = 'Save file',defaultextension=".html",filetypes = (('html files','*.html'),('all files','*.*')))
            file = open(filename, 'x')
            file.write('<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t</head>\n\t<body>\n\t\t<p>{}</p>\n\t</body>\n</html>'.format(userText.strip()))
            file.close()
        except FileExistsError:
            print('\nError! File already exists.\n')
            continue
        break

root = Tk()
root.title('HTML File Generator')
root.minsize(650,445)
root.maxsize(650,445)
root.resizable(0,0)
centerWindow(root,650,445)

info = Label(root,justify=LEFT,text='This program generates a basic HTML file that displays a paragraph. \nYou can customize the text in said paragraph by typing your desired text below.')
info.grid(row=0,column=0,padx=33,pady=(15,0))

scrollbar = Scrollbar(root,orient=VERTICAL)

textField = Text(root,width=72,height=20,yscrollcommand=scrollbar.set)
textField.grid(row=1,column=0,padx=(35,0),pady=(15,10))
textField.insert('1.0',userText)

scrollbar.config(command=textField.yview)
scrollbar.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(0,0),pady=(15,10),sticky=N+E+S)

generateBtn = Button(root,text='Generate',command=save)
generateBtn.grid(row=2,column=0,ipadx=40,ipady=5,sticky='e')

if __name__ == "__main__":
    root.mainloop()
