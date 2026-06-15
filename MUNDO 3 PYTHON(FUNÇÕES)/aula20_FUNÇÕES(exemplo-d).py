def dobro(num):
    posicao = 0
    while posicao < len(num):
        num[posicao] *= 2
        posicao+=1
valores = [1,2,3,4,5,6,7,8,9,10]
dobro(valores)
print(valores)

