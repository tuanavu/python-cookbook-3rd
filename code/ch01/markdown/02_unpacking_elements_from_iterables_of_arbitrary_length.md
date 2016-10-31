
# Unpacking a Sequence into Separate Variables

## Problem
- You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

## Solution
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. The only requirement is that the number of variables and structure match the sequence.

## Example 1
>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212') >>> name, email, *phone_numbers = user_record
>>> name
'Dave'
>>> email
'dave@example.com'
>>> phone_numbers ['773-555-1212', '847-555-1212']
## Example 2
>>> *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
>>> trailing
[10, 8, 7, 1, 9, 5, 10]
>>> current
3