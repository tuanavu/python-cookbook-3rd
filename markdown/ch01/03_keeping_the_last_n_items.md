
# Keeping the Last N Items

## Problem

- You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.

## Solution
- Keeping a limited history is a perfect use for a __`collections.deque`__.
- Using __`deque(maxlen=N)`__ creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is automatically removed

## Example 1


```python
from collections import deque

q = deque(maxlen=3) 
q.append(1)
q.append(2)
q.append(3)
q
```




    deque([1, 2, 3])




```python
q.append(4)
q
```




    deque([2, 3, 4])




```python
q.append(5)
q
```




    deque([3, 4, 5])



## Example 2
- The following code performs a simple text match on a sequence of lines and yields the matching line along with the previous N lines of context when found


```python
import os

file_dir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.abspath(os.path.join(file_dir, "../..", "src/1/keeping_the_last_n_items/somefile.txt"))
```


```python
!head $filename
```

    
    
    
    
    
    
    
    
    
    



```python
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history) 
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
        
# Example use on a file
if __name__ == '__main__':
    with open(filename) as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='') 
            print(line, end='') 
            print('-'*20)
```

    Keeping a limited history is a perfect use for a `collections.deque`.
    For example, the following code performs a simple text match on a
    sequence of lines and prints the matching line along with the previous
    N lines of context when found:
    
    [source,python]
    --------------------
            previous_lines.append(line)
    
    # Example use on a file
    if __name__ == '__main__':
        with open('somefile.txt') as f:
             search(f, 'python', 5)
    --------------------

