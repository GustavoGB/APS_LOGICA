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
