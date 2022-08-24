def escreva(msg):
    tamanho=len(msg)
    print("\033[1;30m-\033[m"*tamanho)
    print(f"   {msg}")
    print("\033[1;30m-\033[m"*tamanho)


escreva('\033[1;33mOLÁ MUNDO\033[m')
escreva(("\033[1;33mSEJA GRATO SEMPRE E JAMAIS DESISTA.\033[m"
         "\033[1;33mLEMBRE-SE, OS VITORIOSOS FORAM AQUELES QUE NÃO DESISTIRAM DE LUTAR\033[m"))
escreva("\033[1;33mTENHA UM DIA EXECELENTE E VAMOS PRA CIMA\033[m")