
# Keeping Dictionaries in Order

## Problem

- You want to create a dictionary, and you also want to control the order of items when iterating or serializing.

## Solution
- To control the order of items in a dictionary, you can use an __`OrderedDict`__ from the __`collections`__ module.


```python
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d: 
    print(key, d[key])
```

    foo 1
    bar 2
    spam 3
    grok 4


- An `OrderedDict` can be particularly useful when you want to build a mapping that you may want to later serialize or encode into a different format. For example, if you want to precisely control the order of fields appearing in a JSON encoding, first building the data in an `OrderedDict` will do the trick:


```python
import json
json.dumps(d)
```




    '{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'



- An OrderedDict internally maintains a doubly linked list that orders the keys according to insertion order.
- Be aware that the size of an OrderedDict is more than twice as large as a normal dic‐ tionary due to the extra linked list that’s created.
