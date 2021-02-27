from flask import Flask, render_template, request, Response

tramos = ((12450,  0.19),
          (20200,  0.24),
          (35200,  0.30),
          (60000,  0.37),
          (300000, 0.45),
          (10e20,  0.47)) # Ponemos un maximo ficticio

def calculoIRPF(sueldo):
    impuesto_a_pagar = 0 # Iremos sumando el pago de cada tramo
    ya_pagado = 0  # guardamos lo ya pagado hasta el tramo anterior
    filasDatos = []
    for max_tramo, tipo_tramo in tramos: # Iteramos en los tramos
        tope_tramo = min(sueldo, max_tramo)  # Sera lo maximo por lo que paguemos en el tramo
        importe_en_tramo = tope_tramo - ya_pagado  # Pagamos por esta cantidad en este tramo
        pago_tramo = importe_en_tramo * tipo_tramo # Pago en este tramo
        impuesto_a_pagar +=  pago_tramo      # Acumulamos en el pago total
        filasDatos.append((importe_en_tramo, 100 * tipo_tramo, pago_tramo))
        ya_pagado = tope_tramo # actualizamos lo pagado
        if ya_pagado == sueldo:
            break # es nuestro ultimo tramo
    return filasDatos, ya_pagado, impuesto_a_pagar*100/ya_pagado, impuesto_a_pagar
                               

app = Flask('Hello Flask')

@app.route('/',methods = ["GET", "POST"])
def index():
    resultado_msg = "Introduzca su sueldo bruto"
    if request.method == "POST":
        sueldo = int(request.form.get("sueldo"))
        fSueldo = float(sueldo)
        filasDatos, ya_pagado, porcentaje_efectivo, importe_pagado = calculoIRPF(fSueldo) 

        return render_template('index_resultado.html', 
            resultado_msg = resultado_msg,
            filasDatos = filasDatos,
            sueldo = ya_pagado,
            porcentaje_efectivo = porcentaje_efectivo,
            importe_pagado = importe_pagado)
    else:
        return render_template('index.html', resultado_msg = resultado_msg)
    

if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1') # solo acceso local y puerto 5000
