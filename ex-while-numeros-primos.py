#Criar um while que imprima todos os número primos entre 0 e 300

i = 0  #inicializador
while (i <= 300): #comparando se o inicializador é maior ou igual a 300
    j = 1 #contador para os divisores
    divisivel = False #se for divisivel nao é um numero primo
    while (j < i -1): #se o contador é menor que o inicializador - 1 / looping
        j += 1
        if (i % j == 0): #divisao do inicializador pelo contador e caso for verdadeiro nao é um numero primo
            divisivel = True
            break  #parada de um looping (for/while)
    if (divisivel == False): #se for divisivel é um numero primo
        print i #imprime os numeros primos 
    i += 1




