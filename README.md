# APS LÓGICA

APS para criar própria linguagem de programação.

A minha linguagem terá o final .bbt e terá sua base voltada majoritariamente em C. Para esta primeira etapa o importante será esquematizar toda a EBNF para implementá-la até o final do semestre. 

Dessa forma, a primeira etapa da linguagem será definir a EBNF. Vamos iniciar a nossa gramática abaixo:

## EBNF


### program 
    : 
    statement +
    ;

### statement
    : 'if' p_expression statement
    | 'if' p_expression statement 'else' statement
    | 'while' p_expression statement
    | 'do' statement 'while' p_expression ';'
    | '{' statement* '}'
    | expression ';'
    | ';'
    ;

### p_expression
    : '(' expression ')'
    ;

### expression
    : compare_smaller 
    | id '=' expression
    ;

### compare_smaller 
    : sum
    | sum '<' sum
    ;

### op
    : term
    | op '+' term
    | op '-' term
    ;

### (falta colocar o factor para colocar * e /)

### term
    : id
    | integer
    | p_expression
    ;

id responsável por nomear as variáveis.

### id
    : STRING
    ;

### integer
    : INT
    ;

### STRING
    : [a-z]+
    ;

### INT
    : [0-9] +
    ;

## Segunda parte

#### Agora nosso foco será na construção desta linguagem em si. 

#### Para isso, utilizaremos o RPLY, uma ferramenta desenvolvida em python para facilitar a criação de uma lingaguem de programação do zero.

Com isso temos os seguinte .py:

    * main.py
    * lexer.py
    * parser.py
    * ast.py

Cada um destes scripts é responsável pelos processos léxicos e sintáticos da nossa linguagem. Isto é, o lexer.py será responsável por adicionar os tokens que temos em nossa linguagem , já a ast.py e o parser.py estão dentro da parte de análise sintática, já que eles irão verificar se a ordem em que os tokens estão correspondem as regras de produção feitas na parte 1. 
O legal do RPLY é que você consegue colocar as regras de produção dentro do seu parser, facilitando o processo. Por enquanto o parser.py ainda não possui sua integração completa mas a ideia é essa.

Por hora temos poucos tokens, o suficiente para fazer operações de + e - porém não para criar variáveis por exemplo. Esta parte já exige análise semântica com auxílio de um symbolTable. 
