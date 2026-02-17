def squares_up_to_n(N):
    for i in range(N + 1):
        yield i ** 2

# Example usage:
# for sq in squares_up_to_n(5):
#     print(sq) # Outputs 0, 1, 4, 9, 16, 25
