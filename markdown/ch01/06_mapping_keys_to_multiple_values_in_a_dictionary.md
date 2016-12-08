
# Mapping Keys to Multiple Values in a Dictionary

## Problem

- You want to make a dictionary that maps keys to more than one value (a so-called “multidict”).

## Solution
- If you want to map keys to multiple values, you need to store the multiple values in another container such as a list or set.
- To easily construct such dictionaries, you can use __`defaultdict`__ in the __`collections`__ module. A feature of __`defaultdict`__ is that it automatically initializes the first value so you can simply focus on adding items.


```python
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
```

    defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})



```python
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(2)
d['b'].add(4)

print(d)
```

    defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})


## Discussion
- We compare 2 ways of constructing a multivalued dictionary.
d = {}
for key, value in pairs:
    if key not in d: 
        d[key] = []
    d[key].append(value)
- The `defauldict` is much simpler
d = defaultdict(list) 
for key, value in pairs: 
    d[key].append(value)