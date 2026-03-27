import math

def value_printer(r, sections):
    a = r
    b = 360 / sections
    
    for i in range(sections):
        angle = math.radians(i * b)  
        
        x = round(a * math.sin(angle), 1)
        y = round(a * math.cos(angle), 1)
        
        print("x =", x, "y =", y)

    return


print("Enter radius ")
r = int(input())

print("Enter sections")
sections = int(input())

value_printer(r, sections)
