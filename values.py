from dataclasses import dataclass

@dataclass
class Number:
    value: float
    
    def __repr__(self):
        try:   
            return f"{self.value}"
        except:
            
            return "Error in Value Calculation"
        