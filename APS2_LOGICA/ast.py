class IntVal():
    def __init__(self, value):
        self.value = value

    def Eval(self):
        return int(self.value)


class BinOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Soma(BinOp):
    def Eval(self):
        return self.left.Eval() + self.right.Eval()

class Multiplicao(BinOp):
    def Eval(self):
        return self.left.Eval() * self.right.Eval()

class Divisao(BinOp):
    def Eval(self):
        return self.left.Eval() // self.right.Eval()

class And(BinOp):
    def Eval(self):
        return self.left.Eval() and self.right.Eval()
        
class Or(BinOp):
    def Eval(self):
        return self.left.Eval() or self.right.Eval()


class Print():
    def __init__(self, value):
        self.value = value

    def Eval(self):
        print(self.value.Eval())