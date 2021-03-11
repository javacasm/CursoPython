def factorial(N):
    '''
    calcula factorial: productos de los enteros hasta el 1
    5! = 5*4*3*2*1 = 5 * 4!
    
    param N: numero entero
    '''
    if N == 1:
        resultado = 1
    else:
        resultado = N * factorial(N-1)
    return resultado

factorial(5)
