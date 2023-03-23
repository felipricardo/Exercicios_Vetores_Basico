"""
1) Faça um programa que receba dez números e armazene em uma lista. Em seguida percorra toda a lista mostrando apenas os números que cujo valor seja superior a 10.
"""
lista = [0] * 10
for i in range (0,10):
  print("Digite um numero")
  lista[i] = int (input())
print(lista)

for i in range (0, 10):
  if lista [i] > 10:
    print(lista[i])

"""
2) Faça um programa que receba dez números e armazene em uma lista. Em seguida conte quantos números são impar e quantos são par. Apresente os contadores na tela.
"""
#origem resposta
numeros = [0] * 10
contador_par = 0
contador_impar = 0

for i in range(10):
    numeros[i] = int(input(f"Digite o {i+1}º número: "))
    if numeros[i] % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print(f"Os números digitados foram: {numeros}")
print(f"Quantidade de números pares: {contador_par}")
print(f"Quantidade de números ímpares: {contador_impar}")



#correção do professor
contaimpar = 0
contapar = 0
lista = [0] * 10
for i in range (10):
  print("Digite um numero")
  lista[i] = int (input())

for i in range (10):
  if lista[i] % 2 == 1:
    contaimpar += 1
  else:
    contapar += 1
print("Numeros impares", contaimpar)
print("Numeros pares", contapar)

"""
3)	Faça um programa que receba dez números e armazene em uma lista. Em seguida, substitua todos os números cujo valor seja menor que 10 pelo valor ZERO. Imprima a lista em tela.
"""
# inicializa a lista vazia
lista = []

# laço de repetição para receber os 10 números do usuário
for i in range(10):
    num = int(input("Digite um número: "))
    lista = lista + [num] # concatena a lista com uma nova lista contendo o número

# laço de repetição para substituir os valores menores que 10 por zero
for i in range(len(lista)):
    if lista[i] < 10:
        lista[i] = 0

# imprime a lista final
print(lista)

"""
5)	Faça um programa que receba dez números e armazene em uma lista. Em seguida percorra toda a lista e procure qual o MAIOR valor dentro da lista e qual o MENOR valor dentro da lista. No final apresente o MAIOR e o MENOR valor.
"""
#ENTRADA
#omaior
#omenor

#PROCESSAMENTO

lista = [0] * 5
omaior = 0
omenor = 0 
for i in range (5):
  print("Digite um numero: ")
  num = int(input())
  lista [i] = num
  if omaior < num:
    omaior = num
  if i == 0:
    omenor = num
  else:
    if omenor > num:
      omenor = num
print("O maior numero é o: ", omaior)
print("O menor numero é o: ", omenor)

"""
6) Faça um programa que receba dez números e armazene em uma lista. Em seguida solicite um outro número e armazene em uma variável chamada multiplicador. Percorra toda a lista e multiplique cada número pelo multiplicador e apresente em tela.
"""
lista = [0] * 5
lista2 = [0] * 5
multip = 0

for i in range (5):
  print("Digite um numero: ")
  num = int(input())
  lista [i] = num
print("Digite o multiplicador: ")
multip = int(input())

for i in range (5):
  lista2 [i] = multip * lista [i]
print("O resultado é: ", lista2)
