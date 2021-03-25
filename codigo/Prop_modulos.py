'''
Modulo de prueba
'''


try:
    print(f'__name__: {__name__}')
    print(f'__file__: {__file__}')
    print(f'__loader__: {__loader__}')
    print(f'__package__: {__package__}')
    print(f'__path__: {__path__}')    
except Exception as e:
    print(f'Error: {e}')
