## Scrapping

¿Qué es?

### Beautiful soup



### Newspaper

Parseador de artículos en la web


```sh
pip3 install newspaper
```

```python
>>> url="https://www.instructables.com/CNC-Pen-Lift-1/"
>>> from newspaper import Article
>>> article = Article(url)
>>> article.download()
>>> article.parse()
>>> article.title
'CNC Pen Lift'
>>> article.authors
['More About Lingib']
>>> article.top_image
'https://content.instructables.com/ORIG/F88/CNC1/L3PVYZ4C/F88CNC1L3PVYZ4C.jpg?auto=webp&frame=1'
>>> article.top_img
'https://content.instructables.com/ORIG/F88/CNC1/L3PVYZ4C/F88CNC1L3PVYZ4C.jpg?auto=webp&frame=1'
```

Instalamos punkt que es un sentence tokenizer

[NLTK: Natural Language Toolkit](https://www.nltk.org/_modules/nltk/tokenize/punkt.html)

Lo instalamos

```python
>>> import nltk
>>> nltk.download('punkt')
```

Y ahora podemos parsear el texto

```python
>>> article.keywords
['toolsall', 'usdimages', 'suppliedthe', '3d', 'cnc', 'x', 'penlift', 'stl', 'teaching', 'lift', 'workshop', 'pen']
>>> article.summary
'More by the author:This instructable explains how to make a CNC pen-lift from an SG90 servo, two 4mm x 100mm nails, the spring from a ball-point pen, and a 3D printer.\nThe design accommodates pen diameters up to 14mm.\nThere is no pen-wobble when the pen is raised and lowered.\nConstruction is easy … all you need is access to a 3D printer, and basic workshop tools.\nThe estimated cost to build this pen-lift is less than $5.00 USDImages'
```

Pero no todos  los artículos están bien formados

```python
>>> url_princ = "https://principia.io/2020/06/29/perseverance-hubo-vida-en-marte.IjEyMTEi/"
>>>  art_princ=Article(url_princ)
>>> art_princ.download()
>>> art_princ.parse()
>>> art_princ.title
'Perseverance, ¿hubo vida en Marte?'
>>> art_princ.authors
[]
>>> art_princ.keywords
[]
>>> art_princ.summary
''
```



### Más 

https://www.youtube.com/watch?v=CCVg-M0E-xM

https://mobile.twitter.com/python_tip/status/1362776037428502534?s=19