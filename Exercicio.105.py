#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:

#– Quantidade de notas
# – A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)

def notas(*n, sit=False):
    retorno=dict()
    retorno['Quantidade de notas:']= len(n)
    retorno['Maior nota:']= max(n)
    retorno['Menor nota:']= min(n)
    retorno['Média de notas']= sum(n)/len(n)
    if sit:
        if sum(n)/len(n) >=6:
            print("APROVADO")
        if sum(n)/len(n)>=4 or sum(n)/len(n)<6:
            print("EXAME ESPECIAL")
        if sum(n)/len(n) <4:
            print("REPROVADO")
    return retorno

boletim=notas(5.5,.5,6.0,1.0, sit=True)
print(boletim)

