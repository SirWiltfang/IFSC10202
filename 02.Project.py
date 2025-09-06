import math
from math import pi

r=input("Enter the radius of sphere:")
x1=input("Enter First Latitude:")
y1=input("Enter First Longitude:")
x2=input("Enter Second Latitude:")
y2=input("Enter Second Longitude:")

R=float(r)
x=float(x1)
y=float(y1)
X=float(x2)
Y=float(y2)

r=(R*math.pi)/180
x1=(x*math.pi)/180
y1=(y*math.pi)/180
x2=(X*math.pi)/180
y2=(Y*math.pi)/180

d= R*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
H= round(d,2)

D = str(H)
P = "The Great Circle Distance is "
W = P + D
print(W)