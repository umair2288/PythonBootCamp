
def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2 
    return area
    

def area_of_rectangle(lenght , width):
    area = lenght * width
    return area


my_total_area = area_of_circle(r=2) + area_of_rectangle(4,10) + area_of_circle(r=1.5)
print(my_total_area)

