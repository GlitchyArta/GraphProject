# Input:   Provide the user with a bunch of options
#          getting input from user to write a function for the program to be able to create points
# Process: The program will create the points using the information about the function
# Output: Arrange and display all points based on x and y from low to high

# Library Files
from points import Equation
from collections import namedtuple
from fractions import *


def prompting():
    op = int(input("""What would you like to do? 
             1. Give the graph function(Enter 1)
             2. Print slope(Enter 2)
             3. Print x-intercept(Enter 3)
             4. Print y-intercept(Enter 4)
             5. Quit(Enter 5)
    """))

    return op

# Declaring an array variable and a namedTuple variable


dot = namedtuple("point", 'x,y')
points = []
xs = []
ys = []
p1 = Equation(None, None, None, None, None, None, None)
frc = None
frc2 = None

# initiating the program
g = int(input("1. is the equation linear(Enter 1) or 2. something else(Enter 2)\n"))

# Decision-making
if g == 1:
   print("Welcome to Graph app ... ")

   p = prompting()
   while p != 5:
        prompting()
        match p:
            case 1:
                #Add points
                prompt = int(input("1.Add point\nenough\n"))

                while prompt != 2:
                    if 3 > prompt > 0:

                        # Getting input from user for x and y
                        determine = int(input("Please enter the x and y of the point:\nx: "))
                        xs.append(determine)
                        determine2 = int(input("\ny: "))
                        ys.append(determine2)
                        p1.X = determine
                        p1.Y = determine2

                        points.append(dot(p1.X, p1.Y))
                        print(len(points))
                        print(list(points))
                        prompt = int(input("""1.Add point\nenough\n"""))
                    else:
                        print("Error ... no such option. Please retry.")
                        prompt = int(input("1.Add point\nenough\n"))

                p = prompting()
            case 2:
                # Assigning frc to difference of x and frc2 to difference of y
                print("Let's evaluate the slope")
                print(len(points))
                if len(points) > 1:
                    frc = xs[1] - xs[0]
                    frc2 = ys[1] - ys[0]
                else:
                    print("Error ... more than one point is required")
                    p = prompting()

                # Figure out the slope
                p1.slope = Fraction(frc/frc2)
                print(p1.slope)

                p = prompting()
            case 3:
                # Figure out the y-intercept
                p1.yintercept = p1.getyintercept(p1.slope, xs[0], ys[0])
                print(p1.yintercept)
                prompt = int(input("""1.Add point\nenough\n"""))
            case 4:
                # Figure out the x-intercept
                if p1.yintercept == None or p1.slope == None:
                    print("Error ... missing information(s)")
                    p = prompting()
                else:
                    p1.getxintercept(p1.yintercept, p1.slope)
                prompt = int(input("""1.Add point\nenough\n"""))
        continue
   if p == 5:
      # Quit
      print("Bye bye ...")
elif g == 2:
    print("I can't really help with that.")
elif 2 < g or g < 1:
    print("Invalid option. Please retry.")
