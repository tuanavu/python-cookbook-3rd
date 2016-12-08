
# Sorting a List of Dictionaries by a Common Key

## Problem

- Sort the entries according to one or more of the dictionary values.

## Solution

- Sorting this type of structure is easy using the operator module’s __`itemgetter`__ function.


```python
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid')) 
rows_by_fname
```




    [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]




```python
rows_by_uid
```




    [{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]



- The `itemgetter()` function can also accept multiple keys.


```python
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
rows_by_lfname
```




    [{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]



- The functionality of `itemgetter()` is sometimes replaced by lambda expressions.


```python
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_fname
```




    [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]


