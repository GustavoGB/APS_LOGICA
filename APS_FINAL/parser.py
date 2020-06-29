from parser import *
from ast import *
from lexer import *
from preprocess import * 

class Parser:
    tokens = None

    @staticmethod
    def parserProgram():

        if Parser.tokens.actual.token_value == "begin_program":
            Parser.tokens.selectNext()
            program = Parser.parserStatement()

            if Parser.tokens.actual.token_value == "end_program":
                Parser.tokens.selectNext()
                return program
            else:
                raise Exception("O token de Begin-progam nao foi encontrado")

        else:
            raise Exception("O token do End-program nao foi encontrado")

    @staticmethod
    def parserBlock():

        if Parser.tokens.actual.token_value == "Open_Brackets":
            Parser.tokens.selectNext()
            commands = []
            while Parser.tokens.actual.token_value != "Closed_Brackets":
                commands.append(Parser.parserStatement())
            Parser.tokens.selectNext()
            return Commands(commands)

    @staticmethod
    def parserStatement():
        ##node = None
        ## Identifier
        if (Parser.tokens.actual.token_type == "variable"):
            nome_variavel = Parser.tokens.actual.token_value
            Parser.tokens.selectNext()
            if (Parser.tokens.actual.token_value == "equal"):
                Parser.tokens.selectNext()
                node = Assignment(
                    nome_variavel,
                    [Identifier(nome_variavel),
                     Parser.parseRelexPr()])
                ## Ponto e virgula
            if Parser.tokens.actual.token_value == "Point_virgula":
                Parser.tokens.selectNext()
                return node
        ## Echo
        elif Parser.tokens.actual.token_value == "show":
            Parser.tokens.selectNext()
            node = Echo([Parser.parseRelexPr()])
            ## Ponto e virgula
            if Parser.tokens.actual.token_value == "Point_virgula":
                Parser.tokens.selectNext()
                return node
            ## While
        elif Parser.tokens.actual.token_value == "while":
            Parser.tokens.selectNext()

            if Parser.tokens.actual.token_value == "Open_Parenthesis":
                Parser.tokens.selectNext()
                node = While([Parser.parseRelexPr()])

                if Parser.tokens.actual.token_value == "Closed_Parenthesis":
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parserStatement())
                    return node
                else:
                    raise Exception("Faltou o elemento -> ')' ")
            else:
                raise Exception("Faltou o elemento -> '(' ")
            ## If
        elif Parser.tokens.actual.token_value == "if":
            Parser.tokens.selectNext()

            if Parser.tokens.actual.token_value == "Open_Parenthesis":
                Parser.tokens.selectNext()
                node = If([Parser.parseRelexPr()])

                if Parser.tokens.actual.token_value == "Closed_Parenthesis":
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parserStatement())

                    if Parser.tokens.actual.token_value == 'else':
                        Parser.tokens.selectNext()
                        node.children.append(Parser.parserStatement())
                        return node
                    return node
                else:
                    raise Exception("Faltou o elemento -> ')' ")
            else:
                raise Exception("Faltou o elemento -> '(' ")

        elif Parser.tokens.actual.token_value == "Point_virgula":
            Parser.tokens.selectNext()
            return NoOp(None)
        ## Cai em um else
        else:
            node = Parser.parserBlock()
            return node

    @staticmethod
    def parseExpression():
        node = Parser.parseTerm()
        while Parser.tokens.actual.token_value == "PLUS" or Parser.tokens.actual.token_value == "MINUS" or Parser.tokens.actual.token_value == "or" or Parser.tokens.actual.token_value == "concate":
            if Parser.tokens.actual.token_value == "PLUS":
                Parser.tokens.selectNext()
                node = BinOp("+", [node, Parser.parseTerm()])
            elif Parser.tokens.actual.token_value == 'MINUS':
                Parser.tokens.selectNext()
                node = BinOp("-", [node, Parser.parseTerm()])
            elif Parser.tokens.actual.token_value == 'or':
                Parser.tokens.selectNext()
                node = BinOp("or", [node, Parser.parseTerm()])
            elif Parser.tokens.actual.token_value == "concate":
                Parser.tokens.selectNext()
                node = BinOp(".", [node, Parser.parseTerm()])
        return node

    @staticmethod
    def parseRelexPr():
        node = Parser.parseExpression()
        while (Parser.tokens.actual.token_value == "equal_compare"
               or Parser.tokens.actual.token_value == "greater"
               or Parser.tokens.actual.token_value == "less"):
            if (Parser.tokens.actual.token_value == "equal_compare"):
                Parser.tokens.selectNext()
                node = BinOp("==", [node, Parser.parseExpression()])
            elif (Parser.tokens.actual.token_value == 'greater'):
                Parser.tokens.selectNext()
                node = BinOp(">", [node, Parser.parseExpression()])
            elif (Parser.tokens.actual.token_value == 'less'):
                Parser.tokens.selectNext()
                node = BinOp("<", [node, Parser.parseExpression()])
        return node

    @staticmethod
    def parseTerm():
        node = Parser.parseFactor()
        while (Parser.tokens.actual.token_value == "TIMES"
               or Parser.tokens.actual.token_value == "DIVIDES"
               or Parser.tokens.actual.token_value == "and"):
            if Parser.tokens.actual.token_value == "TIMES":
                Parser.tokens.selectNext()
                node = BinOp("*", [node, Parser.parseFactor()])
            elif Parser.tokens.actual.token_value == 'DIVIDES':
                Parser.tokens.selectNext()
                node = BinOp("/", [node, Parser.parseFactor()])
            elif Parser.tokens.actual.token_value == "and":
                Parser.tokens.selectNext()
                node = BinOp("and", [node, Parser.parseFactor()])
        return node

    @staticmethod
    def parseFactor():

        node = Parser.tokens.actual.token_value
        ## Number
        if Parser.tokens.actual.token_type is int:
            node = IntVal(Parser.tokens.actual.token_value, "int")
            Parser.tokens.selectNext()
            return node
        ## Identifier
        elif (Parser.tokens.actual.token_type == "variable"):
            node = Identifier(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            return node
        ## Unary op
        elif Parser.tokens.actual.token_value == "PLUS":
            Parser.tokens.selectNext()
            node = UnOp("+", [Parser.parseFactor(), None])
            return node

        elif Parser.tokens.actual.token_value == "MINUS":
            Parser.tokens.selectNext()
            node = UnOp("-", [Parser.parseFactor(), None])
            return node

        elif Parser.tokens.actual.token_value == "not":
            Parser.tokens.selectNext()
            node = UnOp("!", [Parser.parseFactor(), None])
            return node

        elif Parser.tokens.actual.token_type == "true":
            Parser.tokens.selectNext()
            node = BoolVal(True)
            return node

        elif Parser.tokens.actual.token_type == "false":
            Parser.tokens.selectNext()
            node = BoolVal(False)
            return node

        elif Parser.tokens.actual.token_value == "Open_Parenthesis":
            Parser.tokens.selectNext()
            node.children.append(Parser.parseRelexPr())

            if (Parser.tokens.actual.token_value != "Closed_Parenthesis"):
                Parser.tokens.selectNext()
                raise Exception("Símbolo inválido -> esperado ')' ")

            Parser.tokens.selectNext()
            return node

        elif Parser.tokens.actual.token_type == "String":
            node = StringVal(Parser.tokens.actual.token_value, str)
            Parser.tokens.selectNext()
            return node

        # echo
        elif Parser.tokens.actual.token_value == "readline":
            Parser.tokens.selectNext()
            node = (ReadLine())

            if Parser.tokens.actual.token_value == "Open_Parenthesis":
                Parser.tokens.selectNext()

                if Parser.tokens.actual.token_value == "Closed_Parenthesis":
                    Parser.tokens.selectNext()
                    return node
                else:
                    raise Exception("Faltou algum parenteses! -> (")
            else:
                raise Exception("Faltou algum parenteses! -> ")

    @staticmethod
    def runCode(codigo):
        Cod_PrePro = PrePro.filter(codigo)
        Parser.tokens = Tokenizer(Cod_PrePro, 0, Token(int, 0))
        r = Parser.parserProgram()
        table = SymbolTable()

        if (Parser.tokens.actual.token_value == "EOF"):
            return r.Evaluate(table)
        else:
            raise EOFError
def main():
    f = open(sys.argv[1], "r")
    file = f.read()
    if sys.argv[1].endswith(".php"):
        Parser.runCode(file)
    else:
        raise Exception("Voce deveria tentar colocar arquivos do tipo .php!")

if __name__ == "__main__":
    main()