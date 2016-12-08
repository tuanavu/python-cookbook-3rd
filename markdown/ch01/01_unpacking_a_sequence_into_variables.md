
# Unpacking a Sequence into Separate Variables

## Problem
- You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

## Solution
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. The only requirement is that the number of variables and structure match the sequence.

## Example 1


```python
# Example 1
p = (4, 5)
x, y = p
print x
print y
```

    4
    5


## Example 2


```python
# Example 2
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print name
print date

name, shares, price, (year, mon, day) = data
print name
print year
print mon
print day
```

    ACME
    (2012, 12, 21)
    ACME
    2012
    12
    21


# Example 3
- If there is a mismatch in the number of elements, you’ll get an error


```python
# Example 3
# error with mismatch in number of elements
p = (4, 5)
x, y, z = p
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-3-b612f455712e> in <module>()
          2 # error with mismatch in number of elements
          3 p = (4, 5)
    ----> 4 x, y, z = p
    

    ValueError: need more than 2 values to unpack


## Example 4
- Unpacking actually works with any object that happens to be iterable, not just tuples or lists. This includes strings, files, iterators, and generators.


```python
# Example 4: string
s = 'Hello'
a, b, c, d, e = s
print a
print b
print e
```

    H
    e
    o


## Example 5
- Discard certain values


```python
# Example 5
# discard certain values
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print shares
print price
```

    50
    91.1

