import os
for f in os.listdir():
    if os.path.isfile(f): 
        print(f'"{f}" es fichero')
    else : 
        print(f'"{f}" es un directorio')
        