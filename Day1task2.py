"""
Task 2 - printing type of given value

Your task is to print two objects with separator for the same primitive types as in task 1.
The first object is a value of given type, the second object is a type of value.
The separator is a string " is type of ".
Your result could look like this:


123 is type of <class 'int'>
43.23 is type of <class 'float'>
(4-1j) is type of <class 'complex'>
How are you? is type of<class 'str'>
True is type of <class 'bool'>
"""

a = 123
b = 43.23
c = (4-1j)
d = "How are you?"
e = True

print(f"{a} is a type of {type(a)}")
print(f"{b} is a type of {type(b)}")
print(f"{c} is a type of {type(c)}")
print(f"{d} is a type of {type(d)}")
print(f"{e} is a type of {type(e)}")