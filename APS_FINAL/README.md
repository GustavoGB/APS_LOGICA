# Compilador Lógica

## Roteiro 0 - Calculadora Simples

A ideia deste primeiro roteiro é entender um pouco mais sobre como todos os papeis da compilação funcionam e iniciar nosso projeto. 
    Nossa primeira tarefa será receber uma string como "1 + 1"
    ou "1-1+2" e realizar o cálculo pedido. Existem exceções de error necessárias para lembrar, todas elas serão listadas abaixo:
        Caso a string seja " 1+1" ela deve ignorar este espaço e realizar a conta de qualquer forma.
        Entretando, caso seja "1+" deverá soltar um erro já que a operação de + não tem nenhuma função. 
        Outro caso que deve ser visto é quando a string está vazia "   " ou simplesmente com algum sinal "   +  -"
        ou até apenas com um número "1".

## Método para solucionar o problema

Escolheu-se a linguagem Python por ser pratica e também porque possui dicionários e OOP, que serão essenciais mais para frente. 

O método de resolução para este caso foi de: Separar dois arrays, um para os números encontrados na String e outro array para guardar os símbolos(+ e -). É possível realizar este tratamento com as expressões regulares, que serão responsáveis por identificar tanto os números presentes quanto os operadores matemáticos em que estamos interessados.
    Após separar estes dois arrays, é possível realizar um cálculo muito comum quando se fala no conceito de pilha, chamado de reverse polish notation, "Notação Polonesa reversa". Ela é extremamente interessante pois consegue realizar os cálculos em forma de cadeias, pois seu conceito se baseia em colocar os dois números e depois realizar a conta (inicialmente tratando de + e -). Assim, garante-se que a cadeia ao longo da string estará correta e economiza-se memoria ja que as contas serao feitas aos poucos, liberando espaco na pilha rapidamente. 