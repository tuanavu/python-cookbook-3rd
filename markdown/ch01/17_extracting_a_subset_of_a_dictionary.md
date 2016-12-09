
# Extracting a Subset of a Dictionary

## Problem

- This is easily accomplished using a dictionary comprehension.

## Solution

- The easiest way to filter sequence data is often to use a list comprehension.


```python
from pprint import pprint

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }

print("All prices over 200")
pprint(p1)
```

    All prices over 200
    {'AAPL': 612.78, 'IBM': 205.55}



```python
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }

print("All techs")
pprint(p2)
```

    All techs
    {'AAPL': 612.78, 'HPQ': 37.2, 'IBM': 205.55}


## Discussion

- You can also use `tuple()` or another rewrite of dict comprehension


```python
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
```

    {'IBM': 205.55, 'AAPL': 612.78}



```python
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:prices[key] for key in prices.keys() & tech_names }
print(p2)
```

    {'IBM': 205.55, 'HPQ': 37.2, 'AAPL': 612.78}

