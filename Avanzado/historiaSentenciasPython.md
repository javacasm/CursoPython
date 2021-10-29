# Recuerar la historia de sentencias python ejecutadas

Las sentencias python ejecutadas en el intérprete python3 está en el fichero ~/.python_history

```python
import readline
for i in range(readline.get_current_history_length()):
    print(readline.get_history_item(i+1))
```
