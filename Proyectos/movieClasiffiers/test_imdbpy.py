import imdb 

ia = imdb.IMDb() # creamos el acceso
titulo = 'Gordos'
movies = ia.search_movie(titulo) # buscamos por títulos 
print(f'Encontradas {len(movies)} películas con "{titulo}"" en su título') # obtenemos varias
for m in movies:  # iteramos
    print('=====================================================')
    print(f"\r{m['title']} - ID:{m.movieID} - year:{m['year']}") # o m.getID()
    answer = input('more details?')
    if answer == 's':
        print('getting details...')
        movie = ia.get_movie(m.movieID)
        # podemos obtener las claves con movie.keys()
        for key in movie.keys():
            if key == 'directors':
                print('Directores')
                for d in movie['directors']:
                    print(f'      - {d}')        
            elif key == 'cast':
                print(f'  Hay {len(movie[key])} participantes')
            elif type(movie[key]) == type(list()):
                if len(movie[key])>1:
                    print(f'  Hay {len(movie[key])} elementos  de "{key}"')
                else:
                    print(f"{key} - (list) - {movie[key][0]}")
            else:
                print(f"{key} - {movie[key]}")
        print('--------------------------------------------------------')
    if answer == 's':
        answer = input('¿Next?')
        if answer != '':
            print('bye')
            quit()
