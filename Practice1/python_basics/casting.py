# Integers: constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats: constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
a = float(1)     # a will be 1.0
b = float("4.2") # b will be 4.2

# Strings: constructs a string from a wide variety of data types, including strings, integer literals and float literals
c = str("s1") # c will be 's1'
d = str(2)    # d will be '2'

print(x, y, z)
print(a, b)
print(c, d)

# CASTING (Type Conversion) in Python

# ---------- Integers ----------
# Convert different data types to integer

x = int(10)        # integer to integer
y = int(5.9)       # float to integer (decimal part is removed)
z = int("7")       # string to integer

print(x, y, z)

# ---------- Floats ----------
# Convert different data types to float

a = float(3)       # integer to float
b = float("8.4")   # string to float
c = float("6")     # string integer to float

print(a, b, c)

# ---------- Strings ----------
# Convert different data types to string

m = str("hello")   # string to string
n = str(25)        # integer to string
o = str(9.8)       # float to string

print(m, n, o)

# ---------- Type checking ----------
# Check data types after casting

print(type(x))
print(type(a))
print(type(m))
