# Type Casting
# 1. Explicit = Manual changing
name = 'abc'
age = 21
gpa = 3.56
student = True

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

# 2. Implicit = Automatic changing
x = 2
y = 2.0

x = x/y
print(x)