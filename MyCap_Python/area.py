# -*- coding: utf-8 -*-
"""
@author: Acno-Aamir
"""

r=float(input("Enter the radius of the circle to find area for "))
# pi=3.14159265358979323846
# area=pi*r*r
while(r<=0):
    print("Error, radius is incorrect please try again")
    r=float(input("Enter the radius of the circle to find area for "))

print("The area of circle with radius ",r," is ",(3.14159265358979323846*r*r)," sq units")

#Additional, perimeter of the circle
print("The perimeter of circle with radius ",r," is ",(2*3.14159265358979323846*r)," units")
