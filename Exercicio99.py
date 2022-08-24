#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep




def maior(*valores):
    sleep(0.5)
    cont=maior=0
    print("-=-"*15)
    for numero in valores:
        print(f"{numero}", end=" ")
        if cont==0:
            maior = numero
        else:
            if numero>maior:
                maior=numero
        cont+=1
    print(f"\nForam informados {cont} valores\nE o maior valor é {maior}")
    print("-=-" * 15)
    sleep(0.5)

print("ANALISANDO OS VALORES DO SISTEMA")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print()
maior(1,3,5,7)
maior(97,0,5,2,8,22,31,7,10)
maior(1,0,6,9,7)
maior(2,0,2,2)
maior(2,5)
maior(7)
maior()