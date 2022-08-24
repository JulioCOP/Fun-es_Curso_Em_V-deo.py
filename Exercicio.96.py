# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

print()
print(f'{"CONTROLE DE TERRENO":>15}')
print("-"*25)

def area():
    area= comp*larg
    print(f"A area do terreno informado, com "
          f"comprimento  e largura é: \n{area:.2f}m²")

while True:
    comp=float(input("COMPRIMENTO DO TERRENO EM METROS: "))
    larg=float(input("LARGURA DO TERRENO EM METROS: "))
    area()
    resp = str(input("Deseja adicionar algum terreno [S] / [N] ?")).strip().upper()
    while resp not in 'SN':
        resp = str(input("Deseja adicionar algum terreno [S] / [N] ?")).strip().upper()
    if resp == 'N':
        break
print("FIM DO PROGRAMA")