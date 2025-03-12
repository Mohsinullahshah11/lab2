# Create a function that modifies a global variable inside a function using the global keyword.

def myfunc():
   global number 
   number = 2

myfunc()

print(number)
