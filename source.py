# Developed By Toasty#0100 | Night Shift Studios


########################################################################################################################

import tkinter as tk
from tkinter import ttk
class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Siren Tool Converter")
        master.maxsize(900,600)
        master.config(bg = "black")
        
        frame = tk.Frame(master,width=800,height=300,bg="white")
        frame.grid(row = 0,column = 0,padx=10,pady=5)

        label = ttk.Label(frame, text='Enter Binary Number:').grid(row = 0,column =0,padx = 5,pady=5 )    
        button = ttk.Button(frame, text='Convert',command=self.generate).grid(row = 0,column = 4,padx = 5,pady = 5)
       
        self.username = tk.StringVar()
        self.results  = tk.StringVar()
        answer = ttk.Label(frame,textvariable=self.results).grid(row=1,column=1,padx = 5 ,pady = 5)
        name = ttk.Entry(frame, textvariable=self.username).grid(row = 0, column = 1,padx = 5,pady=5)
        print('Siren Tool Converter | Night Shift Studios\n')
        print('Developted By Toasty#0100\n\n\n')
        print('INSTRUCTIONS\n')
        print('1. Export your pattern')
        print('2. Find SirenExport.txt')
        print('3. Copy & Paste only one binary value at a time\n')
        print('P.S. Only convert UNIQUE BINARIES at bottom of the file')

    def generate(self,*args):
        value = str(self.username.get())
        try:
            value = str(self.username.get())
            self.results.set("Answer = {}".format(int(value,2)))
        except ValueError:
            self.results.set("Invalid Input {}".format(value))

root = tk.Tk()
app = Application(master=root)
app.mainloop()

########################################################################################################################

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg



class binary(qtg.QValidator):

    def validate(self,string,index):
        print(string,index)
        
        if all([i=="1" or i == "0" for i in str(string)]):
            state = qtg.QValidator.Acceptable
        elif string == "":
            state = qtg.QValidator.Intermediate
        else: 
            state = qtg.QValidator.Invalid
        return (state,string,index)

class MainWindow(qtw.QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__()
        self.setLayout(qtw.QGridLayout())
        

        label1 = qtw.QLabel("Enter a Binary Number")
        self.convert = qtw.QPushButton("Convert")
        self.answer = qtw.QLabel()
        self.line = qtw.QLineEdit()
        self.line.setValidator(binary()) 
        self.answer.setAlignment(qtc.Qt.AlignHCenter) 
        self.layout().addWidget(label1,0,1)
        self.layout().addWidget(self.line,0,2)
        self.layout().addWidget(self.answer,1,0,1,4)
        self.layout().addWidget(self.convert,0,4) 

        self.convert.clicked.connect(self.converter)
        
        self.show()

    def converter(self):
        decimal = self.line.text()
        binary = int(str(decimal),2)
        self.answer.setText(str(binary))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

########################################################################################################################