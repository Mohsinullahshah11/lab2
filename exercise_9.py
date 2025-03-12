#Write a decorator log_decorator that prints "Function called" before executing the function.

def log_decorator(func):
    def wrapper():
        print("\nFunction called")
        func()
    return wrapper

@log_decorator
def myfunction():
    print("Hello! \n")

myfunction()