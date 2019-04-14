from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pandas as pd
class Ipdr:

    def __init__(self,master):          #master = main window
        frame = Frame(master)
        frame.pack()
        myFont = Font(family ="Cambria", size =14)
        theLabel = Label(root, text = "IPDR Analysis tool",font = myFont)
        text = Text(root)   
        text.configure(font=myFont)
        theLabel.pack()

        #creating a button in class
        
    def dialog(self):
        self.filePath = filedialog.askopenfilename()
        self.df = pd.read_excel(self.filePath)
        print(df)
    def getFile(self):
        self.uploadButton = Button(frame, text = "Add file",fg = "aqua", command = self.dialog)
        self.uploadButton.pack(side = LEFT, padx = 300,pady = 200)
    def printName(self):
        print("You just clicked this button")
    def text(self):
    
        self.quitButton = Button(frame,text ="Quit",command = frame.quit)
        self.quitButton.pack(side="RIGHT")
                             
root = Tk() # declaring an object
obj = Ipdr(root)
root.mainloop() #to display main window
