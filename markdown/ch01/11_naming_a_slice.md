
# Naming a Slice

## Problem

- Your program has become an unreadable mess of hardcoded slice indices and you want to clean it up.

## Solution

- Use __`slice()`__


```python
######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)
```

    51325.0



```python
SHARES = slice(20,32)
PRICE  = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
```

    51325.0


## Why use slice()

- If you have a slice instance s, you can get more information about it by looking at its s.start, s.stop, and s.step attributes, respectively


```python
a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
```

    10
    50
    2


- In addition, you can map a slice onto a sequence of a specific size by using its `indices(size)` method. 


```python
s = 'HelloWorld'
a = slice(5, 10, 2)
a.indices(len(s))
```




    (5, 10, 2)




```python
for i in range(*a.indices(len(s))):
    print(s[i])
```

    W
    r
    d

