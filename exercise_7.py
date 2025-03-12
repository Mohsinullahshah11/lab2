# Write a function operate that takes another function as an argument and applies it to two numbers.

def operate (func,num1,num2):
    return func(num1,num2)

def sum(num1,num2):
    return num1+num2

def multiply(num1,num2):
    return num1*num2

first_number = 10
second_number = 11

print(f'sum is {operate(sum,first_number,second_number)}')
print(f'Multiplication is {operate(multiply,first_number,second_number)}')