import tkinter as tk
from tkinter.ttk import *
from gui import MainGUI
from graph import GraphGUI
from calculator import CalcGUI

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Math Interpreter")
        self.geometry("360x230")
        self.resizable(0,0)
        
        calc_lbl = tk.Label(self, text="1) Open Calculator: ", font=('calibri', 14))
        calc_lbl.place(x=100, y=50, width=200, height=50, anchor="center")
        
        s = Style()
        s.configure('my.TButton', font=('calibri', 12))   
                    
        calc_btn = Button(self, text="Open", style='my.TButton', command=self.open_calculator)
        calc_btn.place(x=210, y=32, height=35)
        
        graph_lbl = tk.Label(self, text="2) Open Graph: ", font=('calibri', 14))
        graph_lbl.place(x=85, y=110, width=200, height=50, anchor="center")
                    
        graph_btn = Button(self, text="Open", style='my.TButton', command=self.open_graph)
        graph_btn.place(x=210, y=92, height=35)
        
        formula_lbl = tk.Label(self, text="3) Variable Calculation: ", font=('calibri', 14))
        formula_lbl.place(x=111, y=170, width=200, height=50, anchor="center")
                    
        formula_btn = Button(self, text="Open", style='my.TButton', command=self.open_formula)
        formula_btn.place(x=210, y=154, height=35)
    
    def open_calculator(self):
        CalcGUI(self)
    
    def open_graph(self):
        GraphGUI(self)
    
    def open_formula(self):
        MainGUI(self)

if __name__ == "__main__":
    app = Main()
    app.mainloop()