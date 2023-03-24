"""
7)	Faça um programa que receba dez números e armazene em uma lista. Em seguida copie todos os números da primeira lista para uma segunda lista, 
mas na ordem invertida da primeira lista.
"""
lista = [0] * 5
inv = [0] * 5

for i in range (5):
  print("Digite um numero: ")
  lista [i] = int(input())

#for i in range (9,-1,-1):
#  print(lista [i])
for i in range (0,10):
  inv[i] = lista [9-i]
print(inv)
  
