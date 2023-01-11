import matplotlib.pyplot as plt
import tkinter as tk 
from tkinter.ttk import *
from numpy import *
 
class GraphGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Plot graph')
        self.geometry('450x270')
        self.resizable(0,0)
        self.equation_val = tk.StringVar()
        self.range_val = tk.StringVar()
        self.valid_exp = True
        
        main_lbl = Label(self, text="Plot Liner Graph based on input values", font=('calibri', 14))
        main_lbl.place(x=15, y=15, height=33)
        
        lbl_1 = Label(self, text="1) Please add equation for graph (Ex: x-5)", font=('calibri', 13))
        lbl_1.place(x=15, y=60)
        
        exprssion = Label(self, text="Expression: ", font=('calibri', 13))
        exprssion.place(x=15, y=91)
               
        expression_input = Entry(self, textvariable=self.equation_val, font = ('calibri', 13, ''), width=10)
        expression_input.place(x=110, y=90)
        
        self.exprssion_error = Label(self, text="( please add expression )", font=('calibri', 12), foreground='red')
        
        
        lbl_2 = Label(self, text="2) Add range of values for x or y (Ex: 2,9)", font=('calibri', 13))
        lbl_2.place(x=15, y=145)
        
        exprssion = Label(self, text="Range: ", font=('calibri', 13))
        exprssion.place(x=15, y=170)
        
        self.range_error = Label(self, text="( please add range )", font=('calibri', 12), foreground='red')
        
        
        range_input = Entry(self, textvariable=self.range_val, font = ('calibri', 13, ''), width=10)
        range_input.place(x=80, y=170)
        
        s = Style()
        s.configure('my.TButton', font=('calibri', 12) , background='#FFFA9B')
           
        
        rootpathBtn = Button(self, text='Plot Graph', command=self.run_plot, style='my.TButton')
        rootpathBtn.place(x=125, y=215, width=140, height=35)
        
    def run_plot(self):
        self.valid_exp = True
        equation = self.equation_val.get()
        rangeVal = self.range_val.get()
        if(equation == ''):
            self.exprssion_error.place(x=220, y=91)
            self.valid_exp = False
        
        if(rangeVal == ''):
            self.range_error.place(x=190, y=170)
            self.valid_exp = False
            
        if(self.valid_exp and not rangeVal.__contains__(",")):
            self.valid_exp = False
            self.range_error.place(x=190, y=170)
            self.range_error.configure(text="(invalid range add ',' separate value)")
            
        if(self.valid_exp and rangeVal.__contains__(",")):
            self.get_range = rangeVal.split(",")
            self.r1,self.r2 = self.get_range
            self.r1 = int(str(self.r1).strip())
            self.r2 = int(str(self.r2).strip())
        
        if(self.valid_exp and equation.__contains__("^3")):
            equation = equation.replace('^3', '**3')
            x=linspace(self.r1,self.r2)
            y=eval(equation)
            self.graph(x,y)
          
        elif(self.valid_exp and equation.__contains__("x") and equation.__contains__("-")):
            eq_val = equation.split('-')
            x = [i for i in range(int(self.r1), int(self.r2+1))]
            y = []
            if(eq_val[0].strip() == 'x'):
                for i in x:
                    y.append(i - int(eq_val[1].strip()))
            elif(eq_val[1].strip() == 'x'):
                for i in x:
                    y.append(int(eq_val[0].strip()) - i)
            
            if(len(x) != 0 and len(y) != 0):
                self.graph(x,y)
        elif(self.valid_exp and equation.__contains__("x") and equation.__contains__("+")):
            eq_val = equation.split('+')
            x = [i for i in range(int(self.r1), int(self.r2+1))]
            y = []
            if(eq_val[0].strip() == 'x'):
                for i in x:
                    y.append(i + int(eq_val[1].strip()))
            elif(eq_val[1].strip() == 'x'):
                for i in x:
                    y.append(int(eq_val[0].strip()) + i)
            
            if(len(x) != 0 and len(y) != 0):
                self.graph(x,y)
        elif(self.valid_exp and equation.__contains__("y") and equation.__contains__("-")):
            eq_val = equation.split('-')
            self.get_range = rangeVal.split(",")
            self.r1,self.r2 = self.get_range
            self.r1 = int(str(self.r1).strip())
            self.r2 = int(str(self.r2).strip())
            y = [i for i in range(int(self.r1), int(self.r2+1))]
            x = []
            if(eq_val[0].strip() == 'y'):
                for i in y:
                    x.append(i - int(eq_val[1].strip()))
            elif(eq_val[1].strip() == 'y'):
                for i in y:
                    x.append(int(eq_val[0].strip()) - i)
            
            if(len(x) != 0 and len(y) != 0):
                self.graph(x,y)
        elif(self.valid_exp and equation.__contains__("y") and equation.__contains__("+")):
            eq_val = equation.split('+')
            self.get_range = rangeVal.split(",")
            self.r1,self.r2 = self.get_range
            self.r1 = int(str(self.r1).strip())
            self.r2 = int(str(self.r2).strip())
            y = [i for i in range(int(self.r1), int(self.r2+1))]
            x = []
            if(eq_val[0].strip() == 'y'):
                for i in y:
                    x.append(i + int(eq_val[1].strip()))
            elif(eq_val[1].strip() == 'y'):
                for i in y:
                    x.append(int(eq_val[0].strip()) + i)
            
            if(len(x) != 0 and len(y) != 0):
                self.graph(x,y)        
                        
    def graph(self,x,y):
        plt.plot(x, y)
        plt.xlabel("X-axis")  # add X-axis label
        plt.ylabel("Y-axis")  # add Y-axis label
        plt.title("Equation Plot")  # add title
        plt.show()
        self.exprssion_error.place(x=-100,y=-100)
        self.range_error.place(x=-100,y=-100)
