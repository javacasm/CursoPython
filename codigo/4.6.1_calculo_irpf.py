"""
Tabla con los tramos del IRPF
https://www.finect.com/usuario/Josetrecet/articulos/como-funciona-renta-tramos-irpf


Tramos IRPF 2021  Tipos a aplicar

0 - 12.450€              19%              
12.450€ - 20.200€        24%
20.200€ - 35.200€        30%
35.200€ - 60.000€        37%
60.000€ - 300.000€       45%
Más de 300.000€          47%

"""

tramos = [(12450,  0.19),
          (20200,  0.24),
          (35200,  0.30),
          (60000,  0.37),
          (300000, 0.45),
          (10e20,  0.47)] # Ponemos un maximo ficticio

def calculoIRPF(sueldo):
    impuesto_a_pagar = 0 # Iremos sumando el pago de cada tramo
    ya_pagado = 0  # guardamos lo ya pagado hasta el tramo anterior
    for max_tramo, tipo_tramo in tramos: # Iteramos en los tramos
        tope_tramo = min(sueldo, max_tramo)  # Sera lo maximo por lo que paguemos en el tramo
        importe_en_tramo = tope_tramo - ya_pagado  # Pagamos por esta cantidad en este tramo
        pago_tramo = importe_en_tramo * tipo_tramo # Pago en este tramo
        impuesto_a_pagar +=  pago_tramo      # Acumulamos en el pago total
        print('{:7} * {:5}% = {:8}'.format(  importe_en_tramo, 100 * tipo_tramo, pago_tramo))
        ya_pagado = tope_tramo # actualizamos lo pagado
        if ya_pagado == sueldo:
            break # es nuestro ultimo tramo
        
    print('----------------------------')
    print('{:7}            {:8}'.format(  ya_pagado, impuesto_a_pagar))
    print('Neto {} pagas el {:2.2f}%'.format(sueldo - impuesto_a_pagar, impuesto_a_pagar*100/sueldo))
                                
    
while True:
    sueldo = float(input('¿Cual es tu sueldo? '))
    calculoIRPF(sueldo)
