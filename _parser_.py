from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
            
        return "Invalid Syntax"

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        try:
            if self.current_token == None:
                return None
            result = self.expression()
            if self.current_token != None:
                self.raise_error()
            return result
        except:
            return "Invalid Syntax"
        

    def expression(self):
        try:
            result = self.term_1()
            while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
                if self.current_token.type == TokenType.PLUS:
                    self.advance()
                    result = AddNode(result, self.term_1())
                elif self.current_token.type == TokenType.MINUS:
                    self.advance()
                    result = SubtractNode(result, self.term_1())
            return result
        except:
            return "Invalid Syntax"

    def term_1(self):
        try:
            result = self.term_2()
            while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
                if self.current_token.type == TokenType.MULTIPLY:
                    self.advance()
                    result = MultiplyNode(result, self.term_2())
                elif self.current_token.type == TokenType.DIVIDE:
                    self.advance()
                    result = DivideNode(result, self.term_2())
                elif self.current_token.type == TokenType.MODULO:
                    self.advance()
                    result = ModuloNode(result, self.term_2())
            return result
        except:
            return "Invalid Syntax"

    def term_2(self):
        try:
            result = self.factor()
            if self.current_token != None and self.current_token.type == TokenType.EXPONENT:
                self.advance()
                result = ExponentNode(result, self.factor())
            return result
        except:
            return "Invalid Syntax"

    def factor(self):
        try:
            token = self.current_token
            if token.type == TokenType.L_PARENTHESIS:
                self.advance()
                result = self.expression()
                if self.current_token.type != TokenType.R_PARENTHESIS:
                    self.raise_error()
                self.advance()
                return result
            elif token.type == TokenType.NUMBER:
                self.advance()
                return NumberNode(token.value)
            elif token.type == TokenType.PLUS:
                self.advance()
                return PlusNode(self.factor())
            elif token.type == TokenType.MINUS: 
                self.advance()
                return MinusNode(self.factor())
            elif token.type == TokenType.TAN: 
                self.advance()
                return TanNode(self.factor())
            elif token.type == TokenType.TAN_INVERSE: 
                self.advance()
                return TanInverseNode(self.factor())
            elif token.type == TokenType.SIN: 
                self.advance()
                return SinNode(self.factor())
            elif token.type == TokenType.SIN_INVERSE: 
                self.advance()
                return SinInverseNode(self.factor())
            elif token.type == TokenType.COS: 
                self.advance()
                return CosNode(self.factor())
            elif token.type == TokenType.COS_INVERSE: 
                self.advance()
                return CosInverseNode(self.factor())
            elif token.type == TokenType.SQUARE: 
                self.advance()
                return SquareNode(self.factor())
            elif token.type == TokenType.PI: 
                self.advance()
                return PiNode(self.factor())
            elif token.type == TokenType.SQRT: 
                self.advance()
                return SqrtNode(self.factor())
            elif token.type == TokenType.LOG: 
                self.advance()
                return LogNode(self.factor())

            self.raise_error()
        except:
            return "Invalid Syntax"
