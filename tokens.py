# Creates tokens
from nodes import *
from dataclasses import dataclass
from enum import Enum

# class for tokentypes
class TokenType(Enum):
    NUMBER          = 0
    PLUS            = 1
    MINUS           = 2
    MULTIPLY        = 3
    DIVIDE          = 4
    L_PARENTHESIS   = 5
    R_PARENTHESIS   = 6
    MODULO          = 7
    EXPONENT        = 8
    TAN             = 9
    TAN_INVERSE     = 10
    SIN             = 11
    SIN_INVERSE     = 12
    COS             = 13
    COS_INVERSE     = 14
    SQUARE          = 15
    PI              = 16
    SQRT            = 17
    LOG             = 18


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        try:   
            return self.type.name + (f":{self.value}" if self.value != None else "")
        except:
            
            return "Error in Token"
        
