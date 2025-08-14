import copy

# 1. Python’s built-in data types:
# int, float, complex, str, list, tuple, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType

# 2. How do you check the type of a variable?
x = 5
print(type(x))  # <class 'int'>

# 3. What’s the difference between a list and a tuple?
# List is mutable, tuple is immutable.

# 4. How do you create a dictionary in Python?
my_dict = {'a': 1, 'b': 2}

# 5. What’s the difference between append() and extend() for lists?
# append() adds a single element; extend() adds elements from an iterable.
lst = [1, 2]
lst.append(3)      # [1, 2, 3]
lst.extend([4, 5]) # [1, 2, 3, 4, 5]

# 6. How do you remove an item from a list?
lst.remove(3)      # Removes first occurrence of 3
del lst[0]         # Removes item at index 0
lst.pop()          # Removes and returns last item

# 7. How do you reverse a list in Python?
lst.reverse()      # In-place reverse
reversed_lst = lst[::-1]  # Returns a reversed copy

# 8. How do you sort a list in ascending order?
lst.sort()         # In-place sort
sorted_lst = sorted(lst)  # Returns a sorted copy

# 9. What is the difference between shallow copy and deep copy?
# Shallow copy copies references; deep copy copies objects recursively.
shallow = copy.copy(lst)
deep = copy.deepcopy(lst)

# 10. How do you convert a string to lowercase?
s = "Hello"
print(s.lower())   # "hello"

# 11. How do you check if a string starts with a particular word?
print(s.startswith("He"))  # True

# 12. What’s the difference between is and ==?
# is checks identity; == checks equality of values.
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False

# 13. How do you merge two dictionaries in Python 3.9+?
d1 = {'x': 1}
d2 = {'y': 2}
merged = d1 | d2  # {'x': 1, 'y': 2}

# 14. How do you find the length of a dictionary?
print(len(my_dict))  # 2

# 15. How do you create a set?
my_set = set([1, 2, 3])
another_set = {4, 5, 6}

# 16. What’s the difference between set() and {} in Python?
# set() creates an empty set; {} creates an empty dictionary.

# 17. How do you find the union of two sets?
union_set = my_set | another_set
# or my_set.union(another_set)

# 18. How do you find the intersection of two sets?
intersection_set = my_set & another_set
# or my_set.intersection(another_set)

# 19. What’s the difference between remove() and discard() in sets?
# remove() raises KeyError if item not found; discard() does not.
my_set.discard(10)  # No error
# my_set.remove(10) # KeyError if 10 not in set

# 20. How do you convert a list into a tuple?
lst2 = [7, 8, 9]
tup = tuple(lst2)