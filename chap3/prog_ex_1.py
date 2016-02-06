# write a program to calculate volume and surface area of sphere given radius as input
import math

radius = eval(input("Enter the radius : "))
print(radius)
# vol = 4/3 * PI * cube of radius
volume = 4 / 3 * math.pi * (radius ** 3)
print("Volume =", volume)
# surface area = 4 * PI * square of radius
surface_area = 4 * math.pi * (radius ** 2)
print("Surface area =", surface_area)
