def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Testing the generator
print("Testing squares in range [2, 5]:")
for val in squares(2, 5):
    print(val)
