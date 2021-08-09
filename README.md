# Joy CodeGround

## A simple wrapper for [joy library](https://github.com/fossunited/joy) to render joy sketches in browser using vs code, (or in other words, for those who are allergic to Jupyter Notebook🥱) 
 
---
### How to use


1. Write your code in main.py
2. use ```render()``` instead of ```show()```
3. open ```index.html``` to view the svg, use [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) VS-code extension for realtime reload.

### Example
```python
from helpers import render
from joy import *

c = circle()
render(c)
```

### Usage
![usage](assets/usage.gif)
