import tkinter as tk
from tkinter import Tk, Label, Button, Menu, filedialog,N , S, E, W


class MyFirstGUI:
    def __init__(self,master):
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text = "This is my first GUI!")
        self.label.grid(columnspan = 2, sticky = N)
        self.hello_button = Button(master,text = "Hello",command = self.hello)
        self.hello_button.grid(row = 1, column = 0, sticky = W)
        self.label2 = Label(master, text = "There is an Analyze Button!")
        self.label2.grid(columnspan = 2, sticky = S)
        self.close_button = Button(master,text = "Close",command = master.quit) 
        self.close_button.grid(row = 1, column = 1, sticky = E)
        
    def hello(self):
        print("Hello!")
    
root = Tk()
my_gui = MyFirstGUI(root)

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('{}: "{}"'.format(field, text))
        

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


def Analyze():
    print("Analyzing time.")
    fields = ['Start Date:(DD/MM/YY)', 'End Date:(DD/MM/YY)']
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='Show', command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    #b2 = tk.Button(root, text='Return to Menu', command=root.quit)
    #b2.pack(side=tk.LEFT, padx=5, pady=5)
    
def OpenFile():
    name = filedialog.askopenfilename()
    print(name)
def About():
    print("This is my assignment.")
    

menu = Menu(root)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
# configure File menu items
filemenu.add_command(label="Analyzeee", command=Analyze)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Close", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
#configure Help menu items
helpmenu.add_command(label="About...", command=About)

root.config(menu=menu)
root.mainloop()

root.destroy()
