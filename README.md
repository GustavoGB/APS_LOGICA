# APS LÓGICA

APS para criar própria linguagem de programação.

A minha linguagem terá o final .bbt e terá sua base voltada majoritariamente em C.

Dessa forma, a primeira etapa da linguagem será definir a EBNF. Vamos iniciar a nossa gramática abaixo:

## EBNF


### program 
    : 
    statement +
    ;

### statement
    : 'if' paren_expression statement
    | 'if' paren_expression statement 'else' statement
    | 'while' paren_expression statement
    | 'do' statement 'while' paren_expression ';'
    | '{' statement* '}'
    | expression ';'
    | ';'
    ;

### paren_expression
    : '(' expression ')'
    ;

### expression
    :
