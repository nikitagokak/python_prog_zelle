__author__ = 'santosh'
import math

diameter = eval(input("Enter pizza diameter value :"))
price = eval(input("Enter pizza price :"))
radius = diameter / 2
area = 4 * math.pi * (radius ** 2)
cost = area / price
print("Cost per square inch of pizza :", cost)
