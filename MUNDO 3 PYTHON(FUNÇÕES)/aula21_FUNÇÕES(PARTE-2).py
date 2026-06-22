def contador(i, f, P):
    """

           — > fAZ UMA CONTAGEM NA TELA (docstring).
           :param i:Inicio da contagem
           :param f:fim da contagem
           :param P:passo da contagem
           :return:sem retorno
        """
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += P
    print('FIM')

help(contador)
contador(2,10,2)
