'''
Created on Feb 20, 2021
Objective: In this project I will convert different things like miles to yards
by using stings.

@author: Alex AC
'''

'''

#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.

miles = input("How many miles would you like to convert?")


#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
#
#Store the value in a variable called yards and print it out with a 
#simple statement.

yards = miles * 1760
print(str(miles) + "converts to" + str(yards) + "yards.")

#Convert miles to feet, using the following:
# 1 miles = 5280 feet.
#
#Store the value in a variable called feet and print it out with a 
#simple statement.

feet = miles * 5280
print(str(miles) + "converts to" + str(feet) + "feet.")

#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
#
#Store the value in a variable called inches and print it out with a 
#simple statement.

inches = miles * 63,360
print(str(miles) + "converts to" + str(inches) + "inches.")