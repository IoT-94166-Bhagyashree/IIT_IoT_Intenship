from geometry import area_circle, area_rectangle

# Calculate area of a circle
r = float(input("Enter radius of the circle: "))
print("Area of Circle:", area_circle(r))

# Calculate area of a rectangle
l = float(input("Enter length of the rectangle: "))
w = float(input("Enter width of the rectangle: "))
print("Area of Rectangle:", area_rectangle(l, w))
