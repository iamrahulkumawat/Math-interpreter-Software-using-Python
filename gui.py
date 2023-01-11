import tkinter as tk
from tkinter.ttk import *

class MainGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # root = tk.Tk()
        # b = MainGUI(root)
        self.title("Mathemetic Equation!")
        self.geometry("900x600")
        self.resizable(0,0)
        
        # gui variables
        self.equation = tk.StringVar()
        self.variables = {}
        self.display_var = 0
        self.var_name_1 = tk.Label()
        self.var_val_1 = tk.Label()
        self.data = []
        self.dis_data = []
        self.dis_variable = {}
        
        # implement UI 
        self.top_frame = tk.Frame(self, width=200, height=700,
                                bd=10, relief='flat', bg='cadet blue')
        self.top_frame.place(x=0,y=0)
        
        variables = tk.Label(self.top_frame, text="Variables", font=('calibri', 13), bg='lightgray').place(x=90, y=13, width=200, height=50, anchor="center")
        
        var_name_lbl = tk.Label(self.top_frame, text="Name", font=('calibri', 13), bg='white').place(x=40, y=50, width=100, height=30, anchor="center")
        var_val_lbl = tk.Label(self.top_frame, text="Value", font=('calibri', 13), bg='white').place(x=140, y=50, width=100, height=30, anchor="center")
        
        equation_lbl = tk.Label(self, text="Equation : ", font=('calibri', 16)).place(x=257, y=570, anchor="center")
        
        equation_input = Entry(self, textvariable=self.equation, font = ('calibri', 16, ''), width=25)
        equation_input.place(x=310, y=554)
        
        s = Style()
        s.configure('my.TButton', font=('calibri', 12))   
                    
        submit = Button(self, text="Submit",style='my.TButton', command=self.submit)
        submit.place(x=600, y=553, height=35)
        
        clear = Button(self, text="Clear",style='my.TButton', command=self.clear)
        clear.place(x=700, y=553, height=35)
        
        self.eq_frame = tk.Frame(self, width=700, height=510,
                                bd=10, relief='flat')
        self.eq_frame.place(x=200,y=15)
        
    def submit(self):
        eq = self.equation.get()
        if(eq):
            self.equation.set('')
            self.display_var = 0
            self.display_varx = 10
            # Variable setup
            if(eq.__contains__("->")):
                try:
                    var_name, var_value = eq.split('->')
                    if(var_name.isalpha() and var_value.isdigit()):
                        self.variables[var_name.strip()] = var_value
                        for i in self.data:
                            i.destroy()
                        self.var_name_x = 41
                        self.var_name_y = 82
                        self.var_value_x = 140
                        self.var_value_y = 82
                        count = 1
                        for var_key, var_val in self.variables.items():
                            if(count > 1):
                                self.var_name_y += 31
                                self.var_value_y += 31
                                
                            var_name_1 = tk.Label(self.top_frame, text=var_key, borderwidth=3, relief="groove", font=('calibri', 13), bg='grey88')
                            var_name_1.place(x=self.var_name_x, y=self.var_name_y, width=98, height=30, anchor="center")
                            
                            var_val_1 = tk.Label(self.top_frame, text=var_val, borderwidth=3, relief="groove", font=('calibri', 13), bg='grey88')
                            var_val_1.place(x=self.var_value_x, y=self.var_value_y, width=98, height=30, anchor="center")
                            
                            self.data.append(var_name_1)
                            self.data.append(var_val_1)
                            
                            count += 1
                        
                        self.display_variable(var_name, var_value, equation=None)
                            
                    else:
                        print("Invalid variable declaration equation")
                except Exception as error:
                    print(error)
                    print('Invalid Equation')
            
            else:
                self.display_variable(var_name=None, var_value=None, equation=eq)
                    
    def display_variable(self, var_name, var_value, equation):
        new_eq = equation
        if(equation):
            for eq_key, eq_val in self.variables.items():
                new_eq = new_eq.replace(eq_key, eq_val)
                if(new_eq.__contains__('^')):
                    new_eq = new_eq.replace('^', '**')
            
            var_value = eval(new_eq) 
            self.dis_variable[equation] = var_value
        else:
            equation = f"{var_name.strip()} -> {var_value}"
            self.dis_variable[equation] = var_value
        
        for i in self.dis_data:
            i.destroy()
        
        count = 0
        for key_name, key_value in self.dis_variable.items():
            if(count == 10):
                self.display_varx += 300
                self.display_var = 0
                
            eq_1 = tk.Label(self.eq_frame, text=f"> {key_name}", font=('calibri', 14))
            eq_1.place(x=self.display_varx,y=self.display_var)
            
            eq_2 = tk.Label(self.eq_frame, text=f"= {key_value}", font=('calibri', 14))
            eq_2.place(x=self.display_varx,y=self.display_var+26)
                
            self.dis_data.append(eq_1)
            self.dis_data.append(eq_2)
            
            self.display_var += 54
            count += 1
            
    def clear(self):
        self.dis_variable = {}
        for i in self.dis_data:
            i.destroy()


    