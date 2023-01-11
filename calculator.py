import tkinter as tk
from math import *
from tokens import Token
from lexer import Lexer
from _parser_ import Parser
from interpreter import Interpreter

# used to switch between units of rad, and deg
convert_constant = 1
inverse_convert_constant = 1
 
btn_params = {'padx': 16, 'pady': 1, 'bd': 4, 'fg': 'white', 'bg': 'black', 'font': ('arial', 18),
              'width': 2, 'height': 2, 'relief': 'flat', 'activebackground': "black"}
 
 
class CalcGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Scientific Calculator!")
        self.geometry("435x490+50+50")
        self.resizable(0, 0)
        # expression that will be displayed on screen
        self.expression = ""
        # be used to store data in memory
        self.recall = ""
        # self.answer
        self.sum_up = ""
        # create string for text input
        self.text_input = tk.StringVar()
        
        # set frame showing inputs and title
        top_frame = tk.Frame(self, width=600, height=10,
                             bd=10, relief='flat', bg='gray')
        top_frame.pack(side=tk.TOP)
        # set frame showing all buttons
        bottom_frame = tk.Frame(
            self, width=600, height=470, bd=2, relief='flat', bg='black')
        bottom_frame.pack(side=tk.BOTTOM)
       
        # Here is the code for Display of Calculator.
        # entry interface for inputs
        self.equation = tk.Entry(top_frame, font=('arial', 36), relief='flat', bg='black', fg='white', textvariable=self.text_input, width=15, bd=10, justify='right')
        self.equation.pack()
 
        # row 0
        self.btn_left_brack = tk.Button(
            bottom_frame, **btn_params, text="(", border=1, command=lambda: self.clickButton('(', ''))
        self.btn_left_brack.grid(row=0, column=0)
        
        self.btn_right_brack = tk.Button(
            bottom_frame, **btn_params, text=")", command=lambda: self.clickButton(')', ''))
        self.btn_right_brack.grid(row=0, column=1)

        self.btn_pi = tk.Button(
            bottom_frame, **btn_params, text="π", command=lambda: self.clickButton('pi', ''))
        self.btn_pi.grid(row=0, column=2)
       
        self.btn_sqrt = tk.Button(
            bottom_frame, **btn_params, text="sqrt", command=lambda: self.clickButton('sqrt(', ''))
        self.btn_sqrt.grid(row=0, column=3)
        
        self.btn_div = tk.Button(
            bottom_frame, **btn_params, text="/", command=lambda: self.clickButton('/', ''))
        self.btn_div.grid(row=0, column=4)
        
        self.btn_clear = tk.Button(
            bottom_frame, **btn_params, text="C", command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=5)
        
        # row 1
        self.btn_sqr = tk.Button(bottom_frame, **btn_params, text=u"x\u00B2", command=lambda: self.clickButton('**2', ''))
        self.btn_sqr.grid(row=1, column=0)
        
        self.btn_log = tk.Button(bottom_frame, **btn_params, text="log", command=lambda: self.clickButton('log(', ''))
        self.btn_log.grid(row=1, column=1)
        
        self.btn_7 = tk.Button(bottom_frame, **btn_params, text="7", command=lambda: self.clickButton('7', ''))
        self.btn_7.configure(activebackground="black", bg='black')
        self.btn_7.grid(row=1, column=2)
        
        self.btn_8 = tk.Button(bottom_frame, **btn_params, text="8", command=lambda: self.clickButton('8', ''))
        self.btn_8.configure(activebackground="black", bg='black')
        self.btn_8.grid(row=1, column=3)
        
        self.btn_9 = tk.Button(bottom_frame, **btn_params, text="9", command=lambda: self.clickButton('9', ''))
        self.btn_9.configure(activebackground="black", bg='black')
        self.btn_9.grid(row=1, column=4)
       
        self.btn_mult = tk.Button(bottom_frame, **btn_params, text="x", command=lambda: self.clickButton('*', ''))
        self.btn_mult.grid(row=1, column=5)
 
        # row 2
        self.btn_sin = tk.Button(
            bottom_frame, **btn_params, text="sin", command=lambda: self.clickButton('sin(', ''))
        self.btn_sin.grid(row=2, column=0)
    
        self.btn_cos = tk.Button(
            bottom_frame, **btn_params, text="cos", command=lambda: self.clickButton('cos(', ''))
        self.btn_cos.grid(row=2, column=1)
        
        self.btn_4 = tk.Button(bottom_frame, **btn_params, text="4", command=lambda: self.clickButton('4', ''))
        self.btn_4.configure(activebackground="black", bg='black')
        self.btn_4.grid(row=2, column=2)
        
        self.btn_5 = tk.Button(bottom_frame, **btn_params, text="5", command=lambda: self.clickButton('5', ''))
        self.btn_5.configure(activebackground="black", bg='black')
        self.btn_5.grid(row=2, column=3)
        
        self.btn_6 = tk.Button(bottom_frame, **btn_params, text="6", command=lambda: self.clickButton('6', ''))
        self.btn_6.configure(activebackground="black", bg='black')
        self.btn_6.grid(row=2, column=4)
        
        self.btnSub = tk.Button(bottom_frame, **btn_params, text="-", command=lambda: self.clickButton('-', ''))
        self.btnSub.grid(row=2, column=5)
        
        
        # row 3
        self.btn_sin_inverse = tk.Button(bottom_frame, **btn_params, text=u"sin-\u00B9", command=lambda: self.clickButton('arcsin(', ''))
        self.btn_sin_inverse.grid(row=3, column=0)
        
        self.btn_cos_inverse = tk.Button(bottom_frame, **btn_params, text=u"cos-\u00B9", command=lambda: self.clickButton('arccos(', ''))
        self.btn_cos_inverse.grid(row=3, column=1)
        
        self.btn_1 = tk.Button(bottom_frame, **btn_params, text="1", command=lambda: self.clickButton('1', ''))
        self.btn_1.configure(activebackground="black", bg='black')
        self.btn_1.grid(row=3, column=2)
        
        self.btn_2 = tk.Button(bottom_frame, **btn_params, text="2", command=lambda: self.clickButton("2", ''))
        self.btn_2.configure(activebackground="black", bg='black')
        self.btn_2.grid(row=3, column=3)
     
        self.btn_3 = tk.Button(bottom_frame, **btn_params, text="3", command=lambda: self.clickButton('3', ''))
        self.btn_3.configure(activebackground="black", bg='black')
        self.btn_3.grid(row=3, column=4)
       
        self.btn_add = tk.Button(
            bottom_frame, **btn_params, text="+", command=lambda: self.clickButton('+', ''))
        self.btn_add.grid(row=3, column=5)
        
 
        # row 4
        self.btn_tan = tk.Button(bottom_frame, **btn_params, text="tan", command=lambda: self.clickButton('tan(', ''))
        self.btn_tan.grid(row=4, column=0)
        
        self.btn_tan_inverse = tk.Button(bottom_frame, **btn_params, text=u"tan-\u00B9", command=lambda: self.clickButton('arctan(', ''))
        self.btn_tan_inverse.grid(row=4, column=1)
       
        self.btn_0 = tk.Button(bottom_frame, **btn_params, text="0", command=lambda: self.clickButton('0', ''))
        self.btn_0.configure(activebackground="black", bg='black', width=7, bd=5)
        self.btn_0.grid(row=4, column=2, columnspan=2)
       
        self.btn_eq = tk.Button(bottom_frame, **btn_params, text="=", command=lambda: self.clickButton('VALUE', ''))
        self.btn_eq.configure(bg='Gray', activebackground='#009999')
        self.btn_eq.grid(row=4, column=4)
       
        self.btn_dec = tk.Button(bottom_frame, **btn_params, text=".", command=lambda: self.clickButton('.', ''))
        self.btn_dec.grid(row=4, column=5)
 
 
    # functions
    # allows button you click to be put into self.expression
    def clickButton(self, value, text):
        current_equation = str(self.equation.get())
        text = current_equation
        
        if value == 'CLEAR':
            text = ""
            self.equation.delete(-1, tk.END)
        elif value == 'VALUE':
            text = self.mathematical_formula(text)
            current_equation = text
            lexer = Lexer(current_equation)
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            tree = parser.parse()
           
            if not tree:
                self.equation.insert(0, "Error")
            interpreter = Interpreter()
            answer = interpreter.visit(tree)
            self.equation.delete(-1, tk.END)
            self.equation.insert(0, answer)
        else:
            self.equation.delete(0, tk.END)
            self.equation.insert(-1, current_equation + value)


    def mathematical_formula(self, text):
        # short name use's for  math trigonometry functions 
        if(text.__contains__('arctan(')):
            text = text.replace('arctan', 'A')
        if(text.__contains__('arcsin(')):
            text = text.replace('arcsin', 'I')
        if(text.__contains__('arccos(')):
            text = text.replace('arccos', 'O')
        if(text.__contains__('tan(')):
            text = text.replace('tan', 'T')
        if(text.__contains__('sin(')):
            text = text.replace('sin', 'S')
        if(text.__contains__('cos(')):
            text = text.replace('cos', 'C')
        if(text.__contains__('**2')):
            text = text.replace('**2', '')
            text = f'E{text}'
        if(text.__contains__('pi')):
            text = text.replace('pi', '')
            text = f'P{text}'
        if(text.__contains__('sqrt(')):
            text = text.replace('sqrt', '')
            text = f'Q{text}'
        if(text.__contains__('log(')):
            text = text.replace('log', '')
            text = f'L{text}'
            
        return text
        
    
    # clears self.expression
    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")
        
    