from rply import ParserGenerator
from ast import IntVal, Soma, Subtracao, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB','MULT','DIV']
        )

   