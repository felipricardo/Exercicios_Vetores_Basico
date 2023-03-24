"""
6) Faça um programa que receba dez números e armazene em uma lista. Em seguida solicite um outro número e armazene em uma variável chamada multiplicador. 
Percorra toda a lista e multiplique cada número pelo multiplicador e apresente em tela.
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
