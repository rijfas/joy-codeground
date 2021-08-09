# Joy CodeGround

## A simple wrapper for [joy library](https://github.com/fossunited/joy)
 
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