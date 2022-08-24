#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através
# da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


from time import sleep

def contador(inicio,fim,passo):
    if passo<0:
        passo=-1
    if passo==0:
        print("ERRO... NÃO TEM COMO CONTAR DE 0 EM 0 UM INTERVELO")
        print("O PROGRAMA IRA FAZER A CONVERSÃO DESSE INTERVALO PARA 1")
        passo=1

    print(f" \nContagem de {inicio} até {fim} de {passo} em {passo}")
    cont=inicio
    sleep(2)
    if inicio<fim:
        while cont<=fim:
            sleep(0.5)
            print(f"{cont}", end=" ")
            cont+=passo
    else:
        cont=inicio
        while cont>=fim:
            sleep(0.5)
            print(f"{cont}", end=" ")
            cont-=passo
        print("\nFIM !")
contador(1,10,1)
contador(10,0,2)
print()
print("APÓS O EXEMPLO, INFORME O INICIO,FIM E O INTERVALO DE CONTAGEM")
ini=int(input("INICIO: "))
fin=int(input("FIM: "))
pas= int(input("INTERVALO: "))
contador(ini,fin,pas)




