from parser import *
from ast import *
from lexer import *
from preprocess import * 

class Token:
    def __init__(self, token_type, token_value):
        self.token_type = token_type
        self.token_value = token_value


class Tokenizer:
    def __init__(self, origin, position, actual):
        self.origin = origin
        self.position = position
        self.actual = actual
        self.selectNext()

    def selectNext(self):

        num = ''
        bufer = ''
        last = ''
        variable = ''
        reservedKeyWord = [
            'show', 'if', 'while', 'else', 'readline', 'and', 'or', 'true',
            'false'
        ]

        if self.position == len(self.origin):
            self.actual = Token(type(""), "EOF")

        elif self.origin[self.position] == ' ':
            self.position += 1
            self.selectNext()

        elif self.position < len(
                self.origin) and self.origin[self.position] == '+':
            self.actual = Token(type("+"), "PLUS")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == '-':
            self.actual = Token(type("-"), "MINUS")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == '*':
            self.actual = Token(type("*"), "TIMES")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == '/':
            self.actual = Token(type("/"), "DIVIDES")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == '(':
            self.actual = Token(type("("), "Open_Parenthesis")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == ')':
            self.actual = Token(type(")"), "Closed_Parenthesis")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == '{':
            self.actual = Token(type(""), "Open_Brackets")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == '}':
            self.actual = Token(type("}"), "Closed_Brackets")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == ';':
            self.actual = Token(type(";"), "Point_virgula")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == '=':
            self.position += 1
            if self.origin[self.position] == '=':
                self.position += 1
                self.actual = Token(type("=="), "equal_compare")
            else:
                self.actual = Token(type("="), "equal")

        elif self.position < len(
                self.origin) and self.origin[self.position] == '!':
            self.actual = Token(type("!"), "not")
            self.position += 1

        elif self.position < len(
                self.origin) and self.origin[self.position] == '>':
            self.position += 1
            self.actual = Token(type(">"), "greater")

        elif self.position < len(
                self.origin) and self.origin[self.position] == '.':
            self.position += 1
            self.actual = Token(type("."), "concate")

        elif self.position < len(
                self.origin) and self.origin[self.position] == 'g':
            self.position += 1
            ## End of program
            if self.origin[self.position] == "g":
                self.position += 1
                self.actual = Token(type("gg"), "end_program")
            else:
                raise Exception("Token para finalizar programa invalido")

        elif self.position < len(
                self.origin) and self.origin[self.position] == '<':
            self.position += 1

            ## Begin of program
            if self.origin[self.position] == "b":
                self.position += 1

                if self.origin[self.position].lower() == "b":
                    self.position += 1

                    if self.origin[self.position].lower() == "t":
                        self.position += 1
                        self.actual = Token(type("<?php"), "begin_program")

            else:
                self.actual = Token(type("<"), "less")

        elif self.origin[self.position] == "\n":
            self.position += 1
            self.selectNext()

        ## String

        elif self.origin[self.position] == '"':
            palavra_string = ''
            self.position += 1
            while self.origin[self.position] != '"':
                palavra_string += self.origin[self.position]
                self.position += 1
            self.position += 1
            self.actual = Token("String", palavra_string)
            return self.actual

        ## Palavra reservada
        elif self.origin[self.position].isalpha():
            while self.origin[self.position].isalpha():
                bufer += self.origin[self.position]
                self.position += 1
                if last == self.position:
                    break
            #print(bufer.lower())
            if bufer.lower() in reservedKeyWord:

                if bufer.lower() == "show":
                    self.actual = Token("show", bufer.lower())
                elif bufer.lower() == "while":
                    self.actual = Token("while", bufer.lower())
                elif bufer.lower() == "if":
                    self.actual = Token("if", bufer.lower())
                elif bufer.lower() == "readline":
                    self.actual = Token("readline", bufer.lower())
                elif bufer.lower() == "true":
                    self.actual = Token("true", bufer.lower())
                elif bufer.lower() == "false":
                    self.actual = Token("false", bufer.lower())
                elif bufer.lower() == "and":
                    self.actual = Token(type("and"), "and")
                elif bufer.lower() == "or":
                    self.actual = Token(type("or"), "or")
                elif bufer.lower() == "else":
                    self.actual = Token(type("else"), "else")

            else:
                raise Exception(
                    "Não é uma palavra reservada, nem uma variável")

        ## Variavel
        elif self.origin[self.position] == '@':
            variable += self.origin[self.position]
            self.position += 1

            if self.origin[self.position].isalpha():
                variable += self.origin[self.position]
                self.position += 1
                while self.position < len(self.origin) and (
                        self.origin[self.position].isalpha()
                        or self.origin[self.position].isnumeric()
                        or self.origin[self.position] == '_'):
                    variable += self.origin[self.position]
                    self.position += 1
                self.actual = Token("variable", variable)
            else:
                raise Exception("Declaracao invalida de uma variavel")

        elif self.position <= len(self.origin) - 1 and self.origin[
                self.position].isnumeric():
            while (self.position <= len(self.origin) - 1
                   and self.origin[self.position].isnumeric()):
                num += self.origin[self.position]
                self.position += 1
            self.actual = Token(int, int(num))
        else:
            raise Exception("Caractere invalido")