#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
#‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt(‘Digite um n: ‘)


def leiaint(n):
    while True:
        num = input(n)
        if num.strip().isnumeric():
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
    return num

# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')