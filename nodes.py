from dataclasses import dataclass

@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        try:   
            return f"{self.value}"
        except:
            return "Error in TreeNode"

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}+{self.node_b})"
        except:
            return "Error in TreeNode"

@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}-{self.node_b})"
        except:
            return "Error in TreeNode"

@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}*{self.node_b})"
        except:
            return "Error in TreeNode"
    
@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}/{self.node_b})"
        except:
            return "Error in TreeNode"

@dataclass
class ModuloNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}%{self.node_b})"
        except:
            return "Error in TreeNode"

@dataclass
class ExponentNode:
    node_a: any
    node_b: any

    def __repr__(self):
        try:   
            return f"({self.node_a}^{self.node_b})"
        except:
            return "Error in TreeNode"

@dataclass
class PlusNode:
    node_t: any  

    def __repr__(self):
        try:   
            return f"(+{self.node})"
        except:
            return "Error in TreeNode"

@dataclass
class MinusNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"(-{self.node})"
        except:
            return "Error in TreeNode"

@dataclass
class TanNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"
        
@dataclass
class TanInverseNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"
        
        
@dataclass
class SinNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"
        
        
@dataclass
class SinInverseNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"
        
        
@dataclass
class CosNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"
        
        
@dataclass
class CosInverseNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"
        
@dataclass
class SquareNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"

@dataclass
class PiNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"
        

@dataclass
class SqrtNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"
        
@dataclass
class LogNode:
    node_t: any

    def __repr__(self):
        try:   
            return f"({self.node_t})"
        except:
            return "Error in TreeNode"

