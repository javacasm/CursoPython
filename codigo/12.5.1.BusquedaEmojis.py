import request
r = requests.get('https://emoji-api.com/emojis?search=cloud&access_key=YOUR_API_KEY')
datos_json=r.json()
for code in datos_json:
    if code['subGroup'] == 'sky-weather':
        print(code['character'] + '    ' + code['slug'])