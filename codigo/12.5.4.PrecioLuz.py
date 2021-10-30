import requests
import json
import statistics
'''
Based on:
    https://ipadbooks.contrataweb.com/2020/11/03/conocer-las-tarifas-de-luz-cada-hora-script-en-python/
    https://rpubs.com/AlbertoFuente/408243
    Cómo ver tu consumo https://www.xataka.com/basics/como-acceder-a-datos-nuestro-contador-luz-internet
    updated by @javacasm

    Puedes comprobar los resultados con https://tarifaluzhora.es

    Licencese CC by SA
'''
v = '0.8'

'''
email to consultasios@ree.es
subject: Personal Token Request
'''
# TOKEN = "PON_AQUI_TU_TOKEN"
TOKEN = "d423bf1d444dc1c935b6834c4486d868c90e2ad730ef986610ce5246fd7fc062"

# Api: https://api.esios.ree.es/
urlIndicadores = 'https://api.esios.ree.es/indicators'

urlDatosFechas = 'https://api.esios.ree.es/indicators/%s?start_date=%sT22:00:00Z&end_date=%sT21:00:00Z&time_trunc=hour'

urlPrecios_20TD = 'https://api.esios.ree.es/indicators/10391'

headers = {'Accept':'application/json; application/vnd.esios-api-v2+json',
           'Content-Type':'application/json',
           'Host':'api.esios.ree.es',
           'Authorization': f'Token token={TOKEN}' }

# codes meaning  https://developer.mozilla.org/es/docs/Web/HTTP/Status
errorCodesMeaning = { 401: 'Unauthorized', 402:'Payment Required', 403: 'Forbidden', 404: 'Not Found', 408: 'Request Timeout',
                      500: 'Internal Server Error', 302: 'Found', 301: 'Moved Permanently', 200:'OK'}


def getRequest(url,headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        return  json_data
    else:
        if response.status_code in errorCodesMeaning:
            print(errorCodesMeaning[response.status_code])
        else:
            print(f'Response.status: {response.status_code}')
            print(f'Response.text: {response.text}')        
        return None
    
'''   
print('Getting indicators')


status_code_indicadores, json_indicadores, responseIndicadores = getRequest(urlIndicadores,headers)
print(responseIndicadores.text)

for indicador in json_indicadores["indicators"]:
    print(indicador["name"],indicador["id"])
'''
print('Getting Prices')
json_precios = getRequest(urlPrecios_20TD, headers)

geoname = 'Península' 

if json_precios != None:
    valores = json_precios['indicator']['values']
    
    precios ={}
    for valor in valores:
        if valor['geo_name'] == geoname:
            strFecha =valor['datetime']
            fecha = strFecha[:10] +' ' + strFecha[11:13]
            precio = valor['value']/1000
            precios[fecha]= precio
            print(f'{fecha}  {precio:.4f}')
    
    # vamos a calcular estadísticas de los datos

    min_precio = min(precios.values())
    min_date =  min(precios,key=precios.get) # Otra forma [date for date in precios if precios[date] == min_precio][0]
    
    max_precio = max(precios.values())
    max_date = max(precios,key=precios.get) # Otra forma [date for date in precios if precios[date] == max_precio][0]

    print(f"Precio mínimo: {min_date} - {min_precio:.4f}")
    print(f"Precio máximo: {max_date} - {max_precio:.4f}")

