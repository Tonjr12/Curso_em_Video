def par(n=0):
    if n%2==0:
        return  True
    else:
        return False

def impar(n=0):
    if n%2!=0:
        return True
    else:
        return False
num = int(input('Digite um numero: '))
if par(num):
    print('Este numero par')
if impar(num):
    print('Este numero impar')



