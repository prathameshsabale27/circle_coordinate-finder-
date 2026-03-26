import math
def value_printer(r,sections):
    a = r
    b = 360/sections
    for i in range(sections):
     x = round(a*math.sin(i*b))
     y = round(a*math.cos(i*b))
     if (x>=0 and y>=0):
         print ("x = ",x,"y = ", y)
     elif (x<0 and y<0):
         print ("x =",x,"y =", y)
     elif (x<0 and y>=0):
         print ("x =",x,"y = ", y)
     else:
          print ("x = ",x,"y =", y)
    
    

    return 


print("Enter radius ")
r= int(input())
print("Enter sections")
sections = int(input())
value_printer(r,sections)
