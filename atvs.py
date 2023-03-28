# # lê interios e flutuantes
# n = float(input('Numero: '))
# # converte pra inteiro
# n = round(n)
# # mostra antecessor e sucessor
# print(n-1, n, n+1)

######################################
# a = float(input('1º Numero: '))
# b = float(input('2º Numero: '))

# if a == b:
#     print('Números iguais')
#     exit()

# c = a
# if b > a: 
#     c = b

# print(c)


######################################
a = float(input('1º Numero: '))
b = float(input('2º Numero: '))
c = float(input('3º Numero: '))

if a + b <= c or a + c <= b or c + b <= a:
    print("Não é triangulo")
    exit()

if a == b and a == c and c == b:
    print("É equilátero")
    exit()

if a == b or a == c or c == b:
    print("É isósceles")
    exit()

print("É escaleno")