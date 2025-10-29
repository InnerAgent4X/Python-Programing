#this gets the numbers we will be working with
colonist = input("Please enter the total number of colonists: ")
ration = input("please enter the total number of rations: ")

#converts the input to an integer
a = int(colonist)
b = int(ration)

#calculates the needed rations and Remaining
needed_rations = (a * 4)
remaining_rations = (b - needed_rations)

#prints the original amount of supplys, the amount distributed, and the total remaining
print("Total rations: ", b)
print("rations needed: ", needed_rations)
print("rations remaining: ", remaining_rations)