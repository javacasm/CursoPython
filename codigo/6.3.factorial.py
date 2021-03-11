def factorial(N):
    '''
    calcula factorial: productos de los enteros hasta el 1
    5! = 5*4*3*2*1
    
    param N: numero entero
    '''
    resultado = 1
    for numero in range(N,1,-1):
        resultado *= numero
    return resultado
