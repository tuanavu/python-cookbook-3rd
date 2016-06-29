
# Table of Contents
 <p><div class="lev1"><a href="#1.3.-Keeping-the-Last-N-Items">1.3. Keeping the Last N Items</a></div><div class="lev2"><a href="#Problem">Problem</a></div><div class="lev2"><a href="#Solution">Solution</a></div><div class="lev2"><a href="#Example-1">Example 1</a></div><div class="lev2"><a href="#Example-2">Example 2</a></div><div class="lev2"><a href="#Example-3">Example 3</a></div>

# 1.3. Keeping the Last N Items

## Problem
You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.

## Solution
Keeping a limited history is a perfect use for a `collections.deque`.

Using `deque(maxlen=N)` creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is automatically removed

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


```python
q = deque()
q.append(1)
q.append(2)
q.append(3)
q
```




    deque([1, 2, 3])




```python
q.appendleft(4)
q
```




    deque([4, 1, 2, 3])




```python
q.pop()
```




    3




```python
q
```




    deque([4, 1, 2])




```python
q.popleft()
```




    4



## Example 3
- The following code performs a simple text match on a sequence of lines and yields the matching line along with the previous N lines of context when found:


```python
# %load ../code/03_keeping_the_last_n_items/example.py
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

```
