# Create a function that modifies a global variable inside a function using the global keyword.

# number = 1
# def myfunc():
#    global number 
#    number = 2
# #    return number

# # value = myfunc()

# print(number)


def spam():
    global eggs
    eggs = 'spam'


#eggs = 'global'
spam()
print(eggs)