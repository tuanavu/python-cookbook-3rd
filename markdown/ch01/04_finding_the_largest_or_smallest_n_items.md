
# Finding the Largest or Smallest N Items

## Problem

- You want to make a list of the largest or smallest N items in a collection.

## Solution
- The __`heapq`__ module has two functions—__`nlargest()`__ and __`nsmallest()`__

## Example 1


```python
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2] 
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23] 
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
```

    [42, 37, 23]
    [-4, 1, 2]


## Example 2
- Use with key parameter


```python
portfolio = [
       {'name': 'IBM', 'shares': 100, 'price': 91.1},
       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
       {'name': 'FB', 'shares': 200, 'price': 21.09},
       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
       {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)
```

    [{'price': 16.35, 'name': 'YHOO', 'shares': 45}, {'price': 21.09, 'name': 'FB', 'shares': 200}, {'price': 31.75, 'name': 'HPQ', 'shares': 35}]
    [{'price': 543.22, 'name': 'AAPL', 'shares': 50}, {'price': 115.65, 'name': 'ACME', 'shares': 75}, {'price': 91.1, 'name': 'IBM', 'shares': 100}]


## Understand heap

- heap converts data into an ordered list


```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
heap
```




    [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]



- `heap[0]` is always the smallest item


```python
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
```

    -4
    1
    2


## Sorted
- You can also use `sorted()` function


```python
sorted(nums)[:3]
```




    [-4, 1, 2]


