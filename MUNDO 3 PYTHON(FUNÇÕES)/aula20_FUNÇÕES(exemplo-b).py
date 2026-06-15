def contador(*num):
    #print('-'*30)
    for valor in num:
        print(f' {valor} ',end='')
    print('Fim')


contador(2,3,6,7)
contador(8,0)
contador(4,7,0)
contador(1,0)
