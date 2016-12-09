
# Mapping Names to Sequence Elements

## Problem

- You have code that accesses list or tuple elements by position, but this makes the code somewhat difficult to read at times. You’d also like to be less dependent on position in the structure, by accessing the elements by name.

## Solution

- __`collections.namedtuple()`__ provides these benefits, while adding minimal overhead over using a normal tuple object.


```python
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub
```




    Subscriber(addr='jonesy@example.com', joined='2012-10-19')




```python
print(sub.addr)
print(sub.joined)
```

    jonesy@example.com
    2012-10-19


- `namedtuple` is interchangeable with a tuple and supports all of the usual tuple operations such as indexing and unpacking.


```python
print(len(sub))
addr, joined = sub
print(addr)
print(joined)
```

    2
    jonesy@example.com
    2012-10-19


- A major use case for named tuples is decoupling your code from the position of the elements it manipulates. So, if you get back a large list of tuples from a database call, then manipulate them by accessing the positional elements, your code could break if, say, you added a new column to your table. Not so if you first cast the returned tuples to namedtuples.

- Here is the code using ordinary tuples


```python
def compute_cost(records): 
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total
```

- Here is a version that uses a `namedtuple`


```python
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# Some Data
records = [
    ('GOOG', 100, 490.1),
    ('ACME', 100, 123.45),
    ('IBM', 50, 91.15)
]

print(compute_cost(records))
```

    65912.5


## Discussion

- Be aware that unlike a dictionary, a `namedtuple` is immutable. If you need to change any of the attributes, it can be done using the `_replace()` method of a `namedtuple` instance


```python
s = Stock('ACME', 100, 123.45)
print(s)
s.shares = 75
```

    Stock(name='ACME', shares=100, price=123.45)



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-8-08525960b121> in <module>()
          1 s = Stock('ACME', 100, 123.45)
          2 print(s)
    ----> 3 s.shares = 75
    

    AttributeError: can't set attribute



```python
s = s._replace(shares=75)
s
```




    Stock(name='ACME', shares=75, price=123.45)



- We can also use `_replace()` method to populate named tuples that have optional or missing fields.


```python
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)
```




    Stock(name='ACME', shares=100, price=123.45, date=None, time=None)




```python
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
dict_to_stock(b)
```




    Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)


