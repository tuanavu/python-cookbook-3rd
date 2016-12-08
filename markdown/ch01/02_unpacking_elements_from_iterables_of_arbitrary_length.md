
# Unpacking Elements from Iterables of Arbitrary Length

## Problem

- You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a “too many values to unpack” exception.

## Solution
- Python “star expressions” can be used to address this problem.

## Example 1
- Suppose you have user records that consist of a name and email address, followed by an arbitrary number of phone numbers. 


```python
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print (name)
print (email)
print (phone_numbers)
```

    Dave
    dave@example.com
    ['773-555-1212', '847-555-1212']


## Example 2


```python
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print (trailing)
print (current)
```

    [10, 8, 7, 1, 9, 5, 10]
    3


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

    foo 1 2
    bar hello
    foo 3 4


## Example 4
- Dealing with certain kinds of string processing operations


```python
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print (uname)
print (homedir)
print (sh)
```

    nobody
    /var/empty
    /usr/bin/false


## Example 5
- Unpack values and throw them away


```python
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

print (name)
print (year)
```

    ACME
    2012

