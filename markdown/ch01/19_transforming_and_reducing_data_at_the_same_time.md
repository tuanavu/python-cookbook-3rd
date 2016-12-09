
# Transforming and Reducing Data at the Same Time

## Problem

- You need to execute a reduction function (e.g., `sum()`, `min()`, `max()`), but first need to transform or filter the data.

## Solution

- A very elegant way to combine a data reduction and a transformation is to use a generator-expression argument.


```python
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)
```

    55



```python
# Determine if any .py files exist in a directory
import os
files = os.listdir(os.path.expanduser('~'))
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
```

    Sorry, no python.
    ACME,50,123.45
    20


- Certain reduction functions such as `min()` and `max()` accept a key argument that might be useful in situations where you might be inclined to use a generator.


```python
# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)
```

    20
    {'name': 'AOL', 'shares': 20}

