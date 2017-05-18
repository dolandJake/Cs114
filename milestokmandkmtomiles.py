"""convert miles to km"""
"""convert km to miles"""
# 1. setup
Kilometers_per_mile = 1.60934
miles_per_kilometer = 0.621371
# 2. input
print( "miles or kilometers?")
miles02 = input("miles")
kilometers02 = str(input("kilometers"))
print("how many"  "?")
miles = float(input())

# 3 transform
kilometers = Kilometers_per_mile * miles

#4 output
print (str(miles) + " miles is " + str(kilometers) + " kilometers")
