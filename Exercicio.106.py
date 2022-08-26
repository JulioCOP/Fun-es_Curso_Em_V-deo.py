from time import sleep

c=('\033[m',        #cor(0) - sem cor
   '\033[0;30;41m',    #cor(1) - vermelho
   '\033[0;30;42m',  #cor(2)- verde
   '\033[0;30;43m', #cor(3) - amarelo
   '\033[0;30;44m', #cor(4) - azul
   '\033[0;30;45m', # cor(5) - roxo
   '\033[1;40m'    #cor(6)- branco
   )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 5)
    print(c[6], end="")
    help(com)
    print(c[0],end="")
    sleep(2)
def titulo(msg,cor=0):
    tam=len(msg) + 4
    print(c[cor], end="")
    print("-"*tam)
    print(msg)
    print("-"*tam)
    print(c[0], end="")
    sleep(1.5)
#Programa Principal
comando=''
while True:
    titulo(" SISTEMA DE AJUDA PYHELP",3)
    comando=str(input('FUNÇÃO OU BIBLIOTECA -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('  ATÉ LOGO',1)