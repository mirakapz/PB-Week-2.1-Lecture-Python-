#0.7 Area of Figures
from math import pi
FORM = input()

if FORM == "square":
    side = float(input())
    print(f"{side * side:.3f}")

elif FORM == "rectangle":
    side_a = float(input())
    side_b = float(input())
    print(f"{side_a * side_b:.3f}")

elif FORM == "circle":
    radius = float(input())
    print(f"{pi * radius * radius:.3f}")
    
elif FORM == "triangle":
    side_t = float(input())
    height = float(input())
    print(f"{(side_t * height) / 2:.3f}")
