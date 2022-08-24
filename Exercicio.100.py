# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados
# pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    for c in range(0,5):
        numeros = randint(1, 10)
        print(f"{c+1}º SORTEIO: {numeros}")
        lista.append(numeros)
        sleep(0.5)
    print(f"LISTA GERADA PELO SORTEIO DOS 5 NUMEROS:  {sorted(lista)}")


def somaPar(lista):
    sleep(1.5)
    print("SOMA DOS VALORES PARES... ")
    sleep(0.5)
    soma=0
    for valor in lista:
        if valor%2==0:
            sleep(0.5)
            print(f"NUMERO PAR: {valor}")
            soma+= valor
            sleep(0.5)
    print(f"TOTAL PAR: {soma}")

numeros=list()
sorteia(numeros)
somaPar(numeros)