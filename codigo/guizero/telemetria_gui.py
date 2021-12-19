from guizero import App, Box, Text, TextBox
app = App(title="My app", height=300, width=400)

topics = {'uno':'valor1','dos':'valor2','tres':'valor3','cuatro':'valor4'}

boxValues = Box(app, align='left')

for item in topics.keys():
    box = Box(boxValues)
    text1 = Text(box, text=item, size=14, font="Arial",align="left")
    text2 = TextBox(box, text = topics[item], align="right")

app.display()