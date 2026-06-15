def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma de {valores} temos {s}')
soma(2,5)
soma(4,5,6)
soma(7,8)