
# Calculating with Dictionaries

## Problem

- You want to perform various calculations on a dictionary of data.

## Solution
- In order to perform useful calculations on the dictionary contents, it is often useful to invert the keys and values of the dictionary using __`zip()`__.


```python
prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}
```


```python
# Find the minimum and maximum price and stock name
min_price = min(zip(prices.values(), prices.keys())) # min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys())) # max_price is (612.78, 'AAPL')

print(min_price)
print(max_price)
```

    (10.75, 'FB')
    (612.78, 'AAPL')



```python
# Ranking
prices_sorted = sorted(zip(prices.values(), prices.keys())) 
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]
print(prices_sorted)
```

    [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]


- Be aware that __`zip()`__ creates an iterator that can only be consumed once.


```python
prices_and_names = zip(prices.values(), prices.keys()) 
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

```

    (10.75, 'FB')



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-7-79e371c3f80e> in <module>()
          1 prices_and_names = zip(prices.values(), prices.keys())
          2 print(min(prices_and_names)) # OK
    ----> 3 print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
    

    ValueError: max() arg is an empty sequence

