#!/usr/bin/env python3
def pizza_area(diameter):
    from math import pi
    return 2 * pi * (diameter/2) ** 2
if __name__ == '__main__':
    try:
        pizza_size = float(input("What is the size of your pizza"))
        pizza_cost = float(input("What is the cost of your pizza"))
    except Vaulueerror:
        print("error: Please enter number")
    else:
        if pizza_cost < 0:
            print("ERROR: Cannot have a negative price")
        elif pizza_size <= 0:
            print("ERROR: Cannot have a zero or negative sized pizza")
        else:
            pizza_area = pizza_area(pizza_size)
            square_inch_cost = pizza_cost / pizza_area
            print(f"You are getting {pizza_area:.2f} square inches of pizza")
            print(f"That is £{square_inch_cost:.2f} per square inch")
