
# Unpacking a Sequence into Separate Variables

## Problem
- You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

## Solution
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. The only requirement is that the number of variables and structure match the sequence.

## Example 1

```python
>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212') 
>>> name, email, *phone_numbers = user_record
>>> name
'Dave'
>>> email
'dave@example.com'
>>> phone_numbers 
['773-555-1212', '847-555-1212']
```

## Example 2

```python
>>> *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
>>> trailing
[10, 8, 7, 1, 9, 5, 10]
>>> current
3
```

## Example 3


```python
records = [
         ('foo', 1, 2),
         ('bar', 'hello'),
         ('foo', 3, 4),
    ]
def do_foo(x, y): 
    print('foo', x, y)
    
def do_bar(s): 
    print('bar', s)
    
for tag, *args in records: 
    if tag == 'foo':
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(*args)
```

## Example 4

```python
>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false' 
>>> uname, *fields, homedir, sh = line.split(':')
>>> uname
'nobody'
>>> homedir 
'/var/empty'
>>> sh 
'/usr/bin/false'
```

## Example 5

```python
>>> record = ('ACME', 50, 123.45, (12, 18, 2012)) 
>>> name, *_, (*_, year) = record
>>> name
'ACME'
>>> year 
2012
```