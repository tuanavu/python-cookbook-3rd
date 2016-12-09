
# Filtering Sequence Elements

## Problem

- You have data inside of a sequence, and need to extract values or reduce the sequence using some criteria.

## Solution

- The easiest way to filter sequence data is often to use a list comprehension.


```python
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# All positive values
pos = [n for n in mylist if n > 0]
print(pos)

# All negative values
neg = [n for n in mylist if n < 0]
print(neg)

# Negative values clipped to 0
neg_clip = [n if n > 0 else 0 for n in mylist]
print(neg_clip)

# Positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print(pos_clip)
```

    [1, 4, 10, 2, 3]
    [-5, -7, -1]
    [1, 4, 0, 10, 0, 2, 3, 0]
    [0, 0, -5, 0, -7, 0, 0, -1]


- You can use generator expressions to produce the filtered values iteratively.


```python
pos = (n for n in mylist if n > 0)
pos
```




    <generator object <genexpr> at 0x106b93c50>




```python
for x in pos:
    print(x)
```

    1
    4
    10
    2
    3


## Discussion

### Filtering

- The filtering criteria cannot be easily expressed in a list comprehension or generator expression. For example, suppose that the filtering process involves exception handling or some other complicated detail. You need to use `filter()` function.


```python
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val): 
    try:
        x = int(val)
        return True
    except ValueError:
        return False
    
ivals = list(filter(is_int, values)) 
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']
```

    ['1', '2', '-3', '4', '5']


### Using itertools
- Another notable filtering tool is `itertools.compress()`, which takes an iterable and an accompanying Boolean selector sequence as input. As output, it gives you all of the items in the iterable where the corresponding element in the selector is True. This can be useful if you’re trying to apply the results of filtering one sequence to another related sequence.


```python
addresses = [
    '5412 N CLARK',
    '5148 N CLARK', 
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
```


```python
from itertools import compress

more5 = [ n > 5 for n in counts ]
a = list(compress(addresses, more5))
print(a)
```

    ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']

