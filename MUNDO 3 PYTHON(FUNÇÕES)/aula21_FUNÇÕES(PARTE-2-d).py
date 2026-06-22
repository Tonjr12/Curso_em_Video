def teste(b):
    global a
    a = 8
    b += 4
    c = 10


    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 1
teste(a)
print(f'A dentro vale {a}')


