# write a function is_even that return True if a given number is even and return False if the number is odd

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False


isEven = is_even(11)
if(isEven):
    print("Number is Even")
else:
    print("Number is odd")