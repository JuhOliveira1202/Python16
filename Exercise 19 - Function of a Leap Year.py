#Exercíco 19:
#Escreva a função bissexto que determina se um
#ano é bissexto.
#Divisível por 4 e não divisivel por 100, a não ser que seja divisível por 400
#Teste 1984 e 2000 é bissexto
#1100 não é bissexto

def bissexto(valor):

    if valor%4 == 0 and valor%100 !=0 or valor%400 == 0:
        return True
    
    else:
        return False

    
valor = int(input("introduza um número"))
resultado = bissexto(valor)
print(resultado)
