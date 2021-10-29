# Movie clasiffiers

## Getting data from imdb 

https://imdbpy.github.io/

pip3 install imdbpy 

[repositorio](https://github.com/alberanid/imdbpy)

[Documentación](https://imdbpy.readthedocs.io/en/latest/)


Podemos instalar la última versión en github con 

```sh
pip3 install git+https://github.com/alberanid/imdbpy
```

## Ejemplos

### Ejemplo de películas

```python
import imdb 

ia = imdb.IMDb() # creamos el acceso
titulo = 'matrix'
movies = ia.search_movie(titulo) # buscamos por títulos 
print(f'Encontradas {len(movies)} películas con {titulo} en su título') # obtenemos varias
for movie in movies:  # iteramos
    print(f"{movie['title']} - ID:{movie.movieID} - year:{movie['year']}mov ") # o movie.getID()
    # podemos obtener las claves con movie.keys()
    for key in movie.keys():
        print(f"{key} - {movie[key]}")
    print('Directores')
    for d in movie['directors']:
        print(d)
```

### Ejemplo de personas

```python
import imdb 

ia = imdb.IMDb() # creamos el acceso

people = ia.search_person('Mel Gibson')
for person in people:
   print(person.personID, person['name'])

```


## Mis datos

Podemos añadir valores a myID y myTitle ¿usarlos con los ficheros?