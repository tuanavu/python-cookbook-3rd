
# Sorting Objects Without Native Comparison Support

## Problem

- You want to sort objects of the same class, but they don’t natively support comparison operations.

## Solution

- The built-in __`sorted()`__ function takes a key argument that can be passed a callable that will return some value in the object that sorted will use to compare the objects. 


```python
from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

# Example
users = [User(23), User(3), User(99)]
print(users)

# Sort by user-id using lambda
print(sorted(users, key=lambda u: u.user_id))

# Sort it by user-id using attrgetter
print(sorted(users, key=attrgetter('user_id')))

```

    [User(23), User(3), User(99)]
    [User(3), User(23), User(99)]
    [User(3), User(23), User(99)]


## Discussion

- `attrgetter()` is often a tad bit faster and also has the added feature of allowing multiple fields to be extracted simultaneously. 
- For example, if User instances also had a first_name and last_name attribute, you could perform a sort like this:
by_name = sorted(users, key=attrgetter('last_name', 'first_name'))