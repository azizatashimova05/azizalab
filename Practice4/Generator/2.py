def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)

n = int(input("Enter a value for n: "))
print(",".join(even_numbers(n)))
