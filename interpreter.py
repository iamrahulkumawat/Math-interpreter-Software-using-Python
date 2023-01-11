from nodes import *
from values import Number
from math import *

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        try:   
            return Number(node.value)
        except:
            
            return "Error in Calculation"

    def visit_AddNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
        except:
            
            return "Error in Calculation"

    def visit_SubtractNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
        except:
            
            return "Error in Calculation"

    def visit_MultiplyNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
        except:
            
            return "Error in Calculation"

    def visit_DivideNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            
            return "Error in Calculation"
    def visit_ModuloNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)
        except:
            
            return "Error in Calculation"

    def visit_ExponentNode(self, node):
        try:   
            return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
        except:
            
            return "Error in Calculation"
    
    def visit_PlusNode(self, node):
        try:   
            return self.visit(node.node_t).value
        except:
            
            return "Error in Calculation"

    def visit_MinusNode(self, node):
        try:   
            return Number(-self.visit(node.node_t).value)
        except:
            
            return "Error in Calculation"
    
    def visit_TanNode(self, node):
        try:   
           return tan(self.visit(node.node_t).value)
        except:
            
            return "Error in Calculation"
    
    def visit_TanInverseNode(self, node):
        try:   
           return atan(self.visit(node.node_t).value)
        except:
            
            return "Error in Calculation"
    
    def visit_SinNode(self, node):
        try:   
           return sin(self.visit(node.node_t).value)
        except:
            
            return "Error in Calculation"
        
    def visit_SinInverseNode(self, node):
        try:   
           return asin(self.visit(node.node_t).value)
        except:
            
            return "Error in Calculation"
        
    def visit_CosNode(self, node):
        try:   
           return cos(self.visit(node.node_t).value)
        except:
            
            return "Error in Calculation"
        
    def visit_CosInverseNode(self, node):
        try:   
           return acos(self.visit(node.node_t).value)
        except:
            
            return "Error in Calculation"
    
    def visit_SquareNode(self, node):
        try:   
           return Number(self.visit(node.node_t).value ** 2)
        except:
            
            return "Error in Calculation"

    def visit_PiNode(self, node):
        try:   
            try:
                return eval(str(self.visit(node.node_t).value * 3.1415926535))
            except:
                return 3.1415926535
        except:
            return "Error in Calculation"
        
    def visit_SqrtNode(self, node):
        try:   
            return eval(str(sqrt(self.visit(node.node_t).value)))
        except:
            return "Error in Calculation"
        
    def visit_LogNode(self, node):
        try:   
            return eval(str(log(self.visit(node.node_t).value)))
        except:
            return "Error in Calculation"