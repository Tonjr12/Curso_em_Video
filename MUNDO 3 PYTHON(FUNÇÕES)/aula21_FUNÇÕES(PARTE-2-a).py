#agora a função está com parâmetros opcionais:
def soma(a=0,b= 0,c=0):
    s = a+b+c
    print(f'A soma de {a} e {b} e {c}: {s}')

soma(3,2,5)
soma(2,5)
soma()
soma(b= 2 , c= 3)
soma(c=1,a=1)