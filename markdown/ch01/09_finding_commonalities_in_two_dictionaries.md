
# Finding Commonalities in Two Dictionaries

## Problem

- You have two dictionaries and want to find out what they might have in common (same keys, same values, etc.).

## Solution
- Perform common set operations using the `keys()` or `items()` methods


```python
a = {
'x' : 1,
'y' : 2,
'z' : 3 }

b = {
'w' : 10,
'x' : 11,
'y' : 2 }
```


```python
# Find keys in common
a.keys() & b.keys() # { 'x', 'y' }
```




    {'x', 'y'}




```python
# Find keys in a that are not in b 
a.keys() - b.keys() # { 'z' }
```




    {'z'}




```python
# Find (key,value) pairs in common 
a.items() & b.items() # { ('y', 2) }
```




    {('y', 2)}



- These kinds of operations can also be used to alter or filter dictionary contents. For example, suppose you want to make a new dictionary with selected keys removed. 


```python
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}} 
# c is {'x': 1, 'y': 2}
print(c)
```

    {'y': 2, 'x': 1}

