
# Implementing a Priority Queue

## Problem

- You want to make a list of the largest or smallest N items in a collection.

## Solution
- You want to implement a queue that sorts items by a given priority and always returns the item with the highest priority on each pop operation.


```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
```

## Example use


```python
# Example use
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
```


```python
print("Should be bar:", q.pop())
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be grok:", q.pop())
```

    Should be bar: Item('bar')
    Should be spam: Item('spam')
    Should be foo: Item('foo')
    Should be grok: Item('grok')


## Undertand the priority queue

- In this recipe, the queue consists of tuples of the form (-priority, index, item). The priority value is negated to get the queue to sort items from highest priority to lowest priority.
- If you make (priority, item) tuples, they can be compared as long as the priorities are different. However, if two tuples with equal priorities are compared, the comparison fails as before.


```python
a = (1, Item('foo'))
b = (5, Item('bar'))
a < b
```




    True




```python
c = (1, Item('grok'))
a < c
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-914192ad79e6> in <module>()
          1 c = (1, Item('grok'))
    ----> 2 a < c
    

    TypeError: unorderable types: Item() < Item()


- By introducing the extra index and making `(priority, index, item)` tuples, you avoid this problem entirely since no two tuples will ever have the same value for index


```python
a = (1, 0, Item('foo')) 
b = (5, 1, Item('bar')) 
c = (1, 2, Item('grok')) 
a < b # True
```




    True




```python
a < c # True
```




    True


