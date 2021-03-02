"""
A program that estimates how much paint is needed
to paint a rectangular room. 

"""

#liters of paint per square meter
liters = 10 / 2.5

#prompt the user to enter room dimensions in centimeters
height = int(input("What is the height of the room in centimeters? ")) / 100
width = int(input("What is the width of the room in centimeters? ")) / 100
length = int(input("What is the length of the room in centimeters? ")) / 100

#calculate the total area of a rectangular room, excluding the floor
area = (2 * (length * height)) + (2 * (width * height)) + (length * width)

#print the total liters of paint needed
print("Total liters of paint required: " + str(round(area / liters, 2)))
