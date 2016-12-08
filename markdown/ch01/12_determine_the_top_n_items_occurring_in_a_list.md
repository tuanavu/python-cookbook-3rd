
# Determining the Most Frequently Occurring Items in a Sequence

## Problem

- Determine the most frequently occurring items in the sequence.

## Solution

- `most_common()` method in `collections.Counter`


```python
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]
```


```python
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# outputs [('eyes', 8), ('the', 5), ('look', 4)]
```

    [('eyes', 8), ('the', 5), ('look', 4)]



```python
print(word_counts['not'])
print(word_counts['eyes'])
```

    1
    8


## Discussion

- Increment the count manually


```python
# morewords = ['why','are','you','not','looking','in','my','eyes']
# for word in morewords:
#     word_counts[word] += 1
```

- Update word counts using update()


```python
morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))
```

    [('eyes', 9), ('the', 5), ('look', 4)]


- You can use Counter to do mathematical operations.


```python
a = Counter(words)
b = Counter(morewords)

print(a)
print(b)
```

    Counter({'eyes': 8, 'the': 5, 'look': 4, 'my': 3, 'into': 3, 'around': 2, "don't": 1, "you're": 1, 'under': 1, 'not': 1})
    Counter({'are': 1, 'eyes': 1, 'why': 1, 'looking': 1, 'in': 1, 'you': 1, 'my': 1, 'not': 1})



```python
# Combine counts
c = a + b
c
```




    Counter({'are': 1,
             'around': 2,
             "don't": 1,
             'eyes': 9,
             'in': 1,
             'into': 3,
             'look': 4,
             'looking': 1,
             'my': 4,
             'not': 2,
             'the': 5,
             'under': 1,
             'why': 1,
             'you': 1,
             "you're": 1})




```python
# Subtract counts
d = a - b
d
```




    Counter({'around': 2,
             "don't": 1,
             'eyes': 7,
             'into': 3,
             'look': 4,
             'my': 2,
             'the': 5,
             'under': 1,
             "you're": 1})


