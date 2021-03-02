"""
A program to convert a number to hours, minutes, 
and seconds in a 24-hour clock format.

"""

#index will add s if plural
def singlePlural(num):
    if num == 1:
        return 0
    else:
        return 1
 
suffix = ["", "s"]

#prompt the user to enter a number
time = int(input("Enter a number from 1 to 86400: "))

#conversion to hours, minutes, seconds
hours = time // 3600
output_hours = "hour{}".format(suffix[singlePlural(hours)])
    
minutes = (time % 3600) // 60
output_minutes = "minute{}".format(suffix[singlePlural(minutes)])

seconds = (time % 3600) % 60
output_seconds = "second{}".format(suffix[ singlePlural(seconds)])

#print conversion in hours, minutes, seconds
print("{} {}, {} {}, and {} {}".format(hours, output_hours, minutes, output_minutes, seconds, output_seconds))
