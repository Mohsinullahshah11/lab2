# Write a function multiply_all that accepts multiple arguments using *args and returns their product.
import math

def multiply_all(*args):
    return math.prod(args)

product = multiply_all(10,10)

print(f'\nProduct is {product}\n')