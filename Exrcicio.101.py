# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
# um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.
#dados['IDADE']=datetime.now().year - ano_nasc
from datetime import datetime

def voto(nasc):
    dados=datetime.now().year
    idade_votar= dados - nasc
    if idade_votar >=18 and idade_votar<65:
        print(f"Com {idade_votar} anos: OBRIGATÓRIO VOTAR")
    elif idade_votar>=16 or idade_votar <18 and idade_votar>=65:
            print(f"Com {idade_votar} anos: VOTO OPCIONAL")
    elif idade_votar < 16:
        print(f"Com {idade_votar} anos: NÃO É PERMITIDO VOTAR")



ano_nasc= (int(input("Digite o ano de nascimento: ")))
voto(ano_nasc)
