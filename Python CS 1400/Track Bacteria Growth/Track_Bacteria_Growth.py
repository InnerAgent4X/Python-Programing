
#asks the user for the pupulation size, Growth rate, and the Hours to simulate.

while True:
    try:
        bacteria = float(input("Enter sarting population: "))
        break
    except ValueError:
        print("Invalid Input. Please enter the population in number form")

while True:
    try:
        growth = float(input("Enter hourly growth rate: "))
        break
    except ValueError:
        print("Invalid Input. Please enter the hourly growth rate as a number")

while True:
    try:
        hours = int(input("Enter number of hours to simulate: "))
        break
    except ValueError:
        print("Invalid Input. Please enter the number of hours as an integer")


#defines a variable used to track iterations and creates list and adds the starting population
current_hour = 0

list_data = [f"Hour 0: {bacteria}"]

#multiplies the population by the growth rate and records the number to the list. 
#repeats until the hours are up
while True:
    if current_hour < hours:
        current_hour += 1
        bacteria = bacteria * growth
        list_data.append(f"Hour {current_hour}: {bacteria:.2f}")
    else:
        break

print(list_data)