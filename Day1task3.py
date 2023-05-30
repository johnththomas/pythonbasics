"""
Task 3 
checking type of value (version 2)

Your task is a slightly modification of task 3. Instead printing True or False modify your code to get readable information about the type of your value.
Your result should look like this:

Is 123  an instance of int?:  True
Is 43.23  an instance of bool?: False
Is (4-1j)  an instance of complex?: True
Is True  an instance of bool?: True
Is 'How are you?'  an instance of float?: False

"""

a = 123
#result= isinstance(type(a),)
b = 43.23
c = (4-1j)
d = "How are you?"
e = True

print(f"Is {a} an instance of int?:{type(a)==int}")
print(f"Is {b} an instance of bool?:{type(b)==bool}")
print(f"Is {c} an instance of complex?:{type(c)==complex}")
print(f"Is {e} an instance of bool?:{type(e)==bool}")
print(f"Is {d} an instance of float?:{type(d)==float}")

#Yet another way of doing it is:
print(f"Is {a} an instance of int?: {isinstance(a, int)}")