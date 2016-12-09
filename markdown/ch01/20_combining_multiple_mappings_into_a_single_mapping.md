
# Combining Multiple Mappings into a Single Mapping

## Problem

- You have multiple dictionaries or mappings that you want to logically combine into a single mapping to perform certain operations, such as looking up values or checking for the existence of keys.

## Solution

- An easy way to do this is to use the `ChainMap` class from the `collections` module.


```python
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }    
```


```python
from collections import ChainMap

c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a) 
print(c['y']) # Outputs 2 (from b) 
print(c['z']) # Outputs 3 (from a)
```

    1
    2
    3


## Discussion

- A ChainMap takes multiple mappings and makes them logically appear as one. However, the mappings are not literally merged together. 
- If there are duplicate keys, the values from the first mapping get used. Thus, the entry `c['z']` in the example would always refer to the value in dictionary a, not the value in dictionary b.
- Operations that mutate the mapping always affect the first mapping listed.


```python
c['z'] = 10
c['w'] = 40

del c['x']

print(a)
print(b)
```

    {'z': 10, 'w': 40}
    {'y': 2, 'z': 4}



```python
del c['y']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    /Users/tvu/anaconda/envs/py35/lib/python3.5/collections/__init__.py in __delitem__(self, key)
        928         try:
    --> 929             del self.maps[0][key]
        930         except KeyError:


    KeyError: 'y'

    
    During handling of the above exception, another exception occurred:


    KeyError                                  Traceback (most recent call last)

    <ipython-input-7-df3e26fa6544> in <module>()
    ----> 1 del c['y']
    

    /Users/tvu/anaconda/envs/py35/lib/python3.5/collections/__init__.py in __delitem__(self, key)
        929             del self.maps[0][key]
        930         except KeyError:
    --> 931             raise KeyError('Key not found in the first mapping: {!r}'.format(key))
        932 
        933     def popitem(self):


    KeyError: "Key not found in the first mapping: 'y'"


- As an alternative to ChainMap, you might consider merging dictionaries together using the `update()` method.


```python
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)

print(merged['x'])
print(merged['y'])
print(merged['z'])
```

    1
    2
    3


- This works, but it requires you to make a completely separate dictionary object (or destructively alter one of the existing dictionaries). Also, if any of the original diction‐ aries mutate, the changes don’t get reflected in the merged dictionary.


```python
a['x'] = 13
merged['x']
```




    1



- A ChainMap uses the original dictionaries, so it doesn’t have this behavior. 


```python
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

merged = ChainMap(a, b)
print(merged['x'])
```

    1



```python
a['x'] = 42
print(merged['x']) # Notice change to merged dicts
print(a['x'])
```

    42
    42

