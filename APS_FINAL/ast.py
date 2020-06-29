from parser import *
from ast import *
from lexer import *
from main import *

class Node():
    def __init__(self, value, children):
        self.value = None
        self.children = children

    def Evaluate(self, SymbolTable):
        pass


class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, SymbolTable):
        if self.value == "+":
            return (+self.children[0].Evaluate(SymbolTable), "int")
        elif self.value == "-":
            return (-self.children[0].Evaluate(SymbolTable), "int")
        elif self.value == "!":
            return (not self.children[0].Evaluate(SymbolTable), "bool")


class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, SymbolTable):

        if self.value == ".":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str and (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:

                return ((str(self.children[0].Evaluate(SymbolTable)[0]) +
                         str(self.children[1].Evaluate(SymbolTable)[0])),
                        "string")
            else:
                raise Exception("Operação não aceita ")

        elif self.value == "+":

            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (int(self.children[0].Evaluate(SymbolTable)[0]) +
                    int(self.children[1].Evaluate(SymbolTable)[0]), "int")

        elif self.value == "-":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (int(self.children[0].Evaluate(SymbolTable)[0]) -
                    int(self.children[1].Evaluate(SymbolTable)[0]), "int")

        elif self.value == "/":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (int(self.children[0].Evaluate(SymbolTable)[0]) //
                    int(self.children[1].Evaluate(SymbolTable)[0]), "int")

        elif self.value == "*":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (int(self.children[0].Evaluate(SymbolTable)[0]) *
                    int(self.children[1].Evaluate(SymbolTable)[0]), "int")

        elif self.value == "or":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (bool(self.children[0].Evaluate(SymbolTable)[0])
                    or bool(self.children[1].Evaluate(SymbolTable)[1]), "bool")

        elif self.value == "and":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (bool(self.children[0].Evaluate(SymbolTable)[0])
                    and bool(self.children[1].Evaluate(SymbolTable)[1]),
                    "bool")

        elif self.value == "<":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (bool(self.children[0].Evaluate(SymbolTable)[0]) < bool(
                self.children[1].Evaluate(SymbolTable)[1]), "bool")

        elif self.value == ">":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[1].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (bool(self.children[0].Evaluate(SymbolTable)[0]) > bool(
                self.children[1].Evaluate(SymbolTable)[1]), "bool")

        elif self.value == "==":
            if (self.children[0].Evaluate(SymbolTable)[1]) == str or (
                    self.children[0].Evaluate(SymbolTable)[1]) == str:
                raise Exception("Operação não aceita ")

            return (bool(self.children[0].Evaluate(SymbolTable)[0]) == bool(
                self.children[1].Evaluate(SymbolTable)[1]), "bool")


class IntVal(Node):
    def __init__(self, value, tipo):
        self.value = value

    def Evaluate(self, SymbolTable):
        return (self.value, int)


class StringVal(Node):
    def __init__(self, value, tipo):
        self.value = value

    def Evaluate(self, SymbolTable):
        return (self.value, str)


class BoolVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, SymbolTable):
        return (self.value, bool)


class NoOp(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, SymbolTable):
        pass


class Commands(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, SymbolTable):
        for n in self.children:
            n.Evaluate(SymbolTable)


class Echo(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, SymbolTable):
        print(self.children[0].Evaluate(SymbolTable))


class Assignment(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, SymbolTable):
        SymbolTable.Setter(self.value, self.children[1].Evaluate(SymbolTable))


class Identifier(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, SymbolTable):
        return SymbolTable.Getter(self.value)


class SymbolTable:
    def __init__(self):
        self.table = {}

    def Setter(self, s_name, value):
        self.table[s_name] = (value)

    def Getter(self, s_name):
        return self.table[s_name]


class While(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, SymbolTable):

        while self.children[0].Evaluate(SymbolTable):
            self.children[1].Evaluate(SymbolTable)


class If(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self, SymbolTable):
        if self.children[0].Evaluate(SymbolTable):
            return self.children[1].Evaluate(SymbolTable)
        else:
            if len(self.children) == 3:
                return self.children[2].Evaluate(SymbolTable)


class ReadLine():
    def __init__(self):
        pass

    def Evaluate(self, SymbolTable):
        return int(input())

