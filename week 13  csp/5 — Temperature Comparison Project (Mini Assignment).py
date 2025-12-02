# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
temp = int(input("What is today's temperaure"))

if temp < -10 or temp > 110:
    print("extreme temp warning")
    
elif temp < -9:
        print("it is cold")
elif temp < 60:
            print("it is warm")
elif temp > 60:
                print("it is hot")


