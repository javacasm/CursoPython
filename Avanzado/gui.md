## [pysimplegui](https://realpython.com/courses/simplify-gui-dev-pysimplegui/)

[Documentación](https://pysimplegui.readthedocs.io/en/latest/)

[Recetario/cookbook](https://pysimplegui.readthedocs.io/en/latest/cookbook/)

## Ejemplos:

### Ventana para recuperar un valor

```python
import PySimpleGUI as sg

event, values = sg.Window('Login Window',
                  [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

login_id = values['-ID-']

```
