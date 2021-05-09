## [pysimplegui](https://realpython.com/courses/simplify-gui-dev-pysimplegui/)

[Documentación](https://pysimplegui.readthedocs.io/en/latest/)

[Recetario/cookbook](https://pysimplegui.readthedocs.io/en/latest/cookbook/)

## Ejemplos:

### Ventana para recuperar un valor

```python
import PySimpleGUI as sg

event, values = sg.Window('Ventana para pedir un valor al usuario',
                  [[sg.T('Introduzca un valor'), sg.In(key='-valor1-')],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

login_id = values['-valor1-']

```


