
# Removing Duplicates from a Sequence while Maintaining Order

## Problem

- You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items.

## Solution
- If the values in the sequence are hashable, the problem can be easily solved using a set and a generator.

### Dedup list


```python
def dedupe(items): 
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
            seen.add(item)
```


```python
a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))
```




    [1, 5, 2, 9, 10]



### Dedup dict with key

- This only works if the items in the sequence are hashable. If you are trying to eliminate duplicates in a sequence of unhashable types (such as dicts), you can make a slight change to this recipe


```python
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
```


```python
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print(a)
print(list(dedupe(a, key=lambda a: (a['x'],a['y']))))
print(list(dedupe(a, key=lambda a: a['x'])))
```

    [{'y': 2, 'x': 1}, {'y': 3, 'x': 1}, {'y': 2, 'x': 1}, {'y': 4, 'x': 2}]
    [{'y': 2, 'x': 1}, {'y': 3, 'x': 1}, {'y': 4, 'x': 2}]
    [{'y': 2, 'x': 1}, {'y': 4, 'x': 2}]


### Dedup line in a file

- The use of a generator function in this recipe reflects the fact that you might want the function to be extremely general purpose—not necessarily tied directly to list process‐ ing. For example, if you want to read a file, eliminating duplicate lines, you could simply do this:
with open(somefile,'r') as f: 
    for line in dedupe(f):
        ...