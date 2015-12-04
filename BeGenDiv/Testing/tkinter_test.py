'''
Created on 06.03.2015

@author: maxdriller
'''

from Tkinter import Tk, BOTH, Frame
from ttk import Button, Style

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="red")   
         
        self.parent = parent
        
        self.initUI()
    
    def initUI(self):
      
        self.parent.title("FirstGUI")
        self.pack(fill=BOTH, expand=1)
        
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=100, y=100)
        

def main():
  
    root = Tk()
    root.geometry("300x300+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  


