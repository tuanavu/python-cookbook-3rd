# 1.1. Unpacking a Sequence into Separate Variables

# Problem
# You have an N-element tuple or sequence
# that you would like to unpack into a collection
# of N variables.

# Example 1
p = (4, 5)
x, y = p
print x
print y

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

# Example 3
# error with mismatch in number of elements
p = (4, 5)
x, y, z = p

# Example 4: string
s = 'Hello'
a, b, c, d, e = s
print a
print b
print e

# Example 5
# discard certain values
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print shares
print price
