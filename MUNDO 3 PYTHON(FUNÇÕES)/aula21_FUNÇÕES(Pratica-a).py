def fatorial(num=1):
    f = 1
    for c in range(num,1,-1):
        f *= c
    return f
f1=(fatorial(5))
f2=(fatorial(4))
f3=(fatorial())
print(f'Os resultados são {f1,f2,f3}')
print(f'O fatorial de {f1},{f2},{f3}')