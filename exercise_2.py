# write a function calculate_area that takes length and width as an argument and returns the area of a rectangle. the wdth should have a defualt value of 10.


def calculate_area(length,width=10):
    return length*width

area1 = calculate_area(50)
area2 = calculate_area(50,20)

print(f"area with out width is {area1}")
print(f"area with width is {area2}")