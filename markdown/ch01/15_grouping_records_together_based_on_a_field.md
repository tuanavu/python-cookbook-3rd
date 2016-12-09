
# Grouping Records Together Based on a Field

## Problem

- The `itertools.groupby()` function is particularly useful for grouping data together like this.

## Solution

- The built-in __`sorted()`__ function takes a key argument that can be passed a callable that will return some value in the object that sorted will use to compare the objects. 


```python
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from itertools import groupby

# Sort by the desired field first
rows.sort(key=lambda r: r['date'])

# Iterate in groups
for date, items in groupby(rows, key=lambda r: r['date']):
    print(date)
    for i in items:
        print('    ', i)
```

    07/01/2012
         {'date': '07/01/2012', 'address': '5412 N CLARK'}
         {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
    07/02/2012
         {'date': '07/02/2012', 'address': '5800 E 58TH'}
         {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}
         {'date': '07/02/2012', 'address': '1060 W ADDISON'}
    07/03/2012
         {'date': '07/03/2012', 'address': '2122 N CLARK'}
    07/04/2012
         {'date': '07/04/2012', 'address': '5148 N CLARK'}
         {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}


## Discussion

- The `groupby()` function works by scanning a sequence and finding sequential “runs” of identical values. Since `groupby()` only examines consecutive items, failing to sort first won’t group the records as you want.
- If your goal is to simply group the data together by dates into a large data structure that allows random access, you should use `defaultdict()`.


```python
# Example of building a multidict
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
```

    {'date': '07/01/2012', 'address': '5412 N CLARK'}
    {'date': '07/01/2012', 'address': '4801 N BROADWAY'}

