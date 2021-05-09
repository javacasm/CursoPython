## Generando gif
# From https://pythonprogramming.altervista.org/python-draws-in-colors-app-to-draw-with-pygame/?doing_wp_cron=1617650069.8141829967498779296875
Usamos PIL

```python

form PIL import Image
import glob

def generamosImages():
    # generamos imagenes con formato
    for i in range(50):
        # generanmos images
        pygame.display.flip()
        fichero = f'lorenz{counter:03d}.png'
        print(f'{fichero} saved')
        counter += 1
        pygame.image.save(screen,fichero)

# Inicializamos
pygame.init()

screen = pygame.display.set_mode((width,height))

frames = []
imgs = glob.glob('lorenz*.png')
imgs.sort()
print(imgs)
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('lorenz.gif', format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=100, loop=1000)
```

## Usando imageio

pip3 install imageio

```python
urlBase = 'https://pbs.twimg.com/media/{}?format=jpg&name=4096x4096'

# SpaceX SN10 awesome pictures
id_images=('EvmM_t7WgAMgASv','EvmM_t-XIAI4MWs','EvqxipXXMA8vE35','EvqxlsXXYAUuTEi')

from urllib.request import urlretrieve
for id in id_images:
    urlretrieve(urlBase.format(id),id)

import imageio
imagenes = [imageio.imread(fichero) for fichero in id_images]
imageio.mimsave('SN10.gif',imagenes,duration = 10)
```

