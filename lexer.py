# Lexer
from tokens import Token, TokenType


WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:   
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '%':
                self.advance()
                yield Token(TokenType.MODULO)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.EXPONENT)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.L_PARENTHESIS)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.R_PARENTHESIS)
            elif self.current_char == 'T':
                self.advance()
                yield Token(TokenType.TAN)
            elif self.current_char == 'A':
                self.advance()
                yield Token(TokenType.TAN_INVERSE)
            elif self.current_char == 'S':
                self.advance()
                yield Token(TokenType.SIN)
            elif self.current_char == 'I':
                self.advance()
                yield Token(TokenType.SIN_INVERSE)
            elif self.current_char == 'C':
                self.advance()
                yield Token(TokenType.COS)
            elif self.current_char == 'O':
                self.advance()
                yield Token(TokenType.COS_INVERSE)
            elif self.current_char == 'E':
                self.advance()
                yield Token(TokenType.SQUARE)
            elif self.current_char == 'P':
                self.advance()
                yield Token(TokenType.PI)
            elif self.current_char == 'Q':
                self.advance()
                yield Token(TokenType.SQRT)
            elif self.current_char == 'L':
                self.advance()
                yield Token(TokenType.LOG)
            else:
                return "Invalid Input"

    def generate_number(self):
        decimal_pts_count = 0
        number_string = self.current_char 
        self.advance() # .

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_pts_count += 1
                if decimal_pts_count > 1:
                    break

            number_string += self.current_char
            self.advance()

        if number_string.startswith('.'):
            number_string = '0' + number_string
        if number_string.endswith('.'): 
            number_string += '0'                

        return Token(TokenType.NUMBER, float(number_string))
