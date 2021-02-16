"""

NASA - MSC Houston, Texas
MSC MEMORANDUM
10 October 1966
SUBJECT: Buzzword Generator
1. The Buzzword Generator consists of three columns of buzzwords
numbered zero to nine.

Column 1
==========
integrated
total
systematized
parallel
functional
responsive
optimal
synchronized
compatible
balanced

Column 2
==========
management
organizational
monitored
reciprocal
digital
logistical
transitional
incremental
third-generation
policy


Column 3
==========
options
flexibility
capability
mobility
programming
concept
time-phase
projection
hardware
contingency


2.The procedure is simple. Think of any three digit number at random.
Then select the corresponding buzzword from each column.
Put them together and WHAM! POW! ZAP!
You sound just like you know what you're talking about.
3. Take for instance the number 257. Take word two from column one,
word five from column two and word seven from column three.
You now have "systematized logistical projection".
You don't know what it means but don't worry, reithe: do "they".
4. Would you prefer "balanced incremental flexibility".
Possibly "parallel reciprocal options".
Or maybe "integrated transitional contingency".
How about "functional third-generation hardware"
and "optimal management mobility. Now that ought to do the trick.
5. The important thing is that the Buzzword Generator
provides the user with the perfect aid for
preparing anything on the subject of spaceflight.
Automatically you have one thousand different combinations,
all of which will give you' that proper ring of decisive,
progressive, knowledgeable, authority.

"""

from random import randint

columna1 = ['integrated', 'total', 'systematized', 'parallel', 'functional',
            'responsive', 'optimal', 'synchronized', 'compatible', 'balanced']
columna2 = ['management', 'organizational', 'monitored', 'reciprocal',
            'digital', 'logistical', 'transitional', 'incremental',
            'third-generation', 'policy']
columna3 = ['options', 'flexibility', 'capability', 'mobility', 'programming',
            'concept', 'time-phase', 'projection', 'hardware', 'contingency']

# Genera 3 cifras aleatorias y obtiene el buzzword correspondiente
def generateRandomBuzzWord():
    col1 = randint(0, 10)  # genera un entero aleatorio entre 0 y 9
    col2 = randint(0, 10)  # genera un entero aleatorio entre 0 y 9
    col3 = randint(0, 10)  # genera un entero aleatorio entre 0 y 9
    return getBuzzWord(col1, col2, col3)


def generateBuzzWord(id):
    col1 = id // 100  # cifra de las centenas
    if col1 > 0:
        id = id - col1 * 100
    col2 = id // 10  # cifra de las decenas
    col3 = id % 10  # cifra de las unidades
    return getBuzzWord(col1, col2, col3)

def getBuzzWord(col1, col2, col3):
    # print(col1, col2, col3)
    buzzWord = columna1[col1] + ' ' + columna2[col2] + ' ' + columna3[col3]
    return buzzWord

def showAllBuzzword():
    print('Todas las buzzword')
    for i in range(0, 1000):
        print(generateBuzzWord(i))

print('Generando una BuzzWord: ' + generateRandomBuzzWord())



