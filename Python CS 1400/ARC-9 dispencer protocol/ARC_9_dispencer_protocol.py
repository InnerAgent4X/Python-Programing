
#asks for the number of citizens
while True:
    try:
        citizens = int(input("Please enter the total number of citizens."))
        print("Thank you")
        break
    except ValueError:
        print("invalid input. Must be an Integer(positive whole number)")

#asks for the amount of supplys, and checks the input is valid
while True:
    try:
        supplys = float(input("Please enter the total number of availible supplies."))
        print("Thank you")
        break
    except ValueError:
        print("Invalid input. Must be a number")

#calulates the amount of supplys used for shore leave.
shore_leave = citizens * 3

#calculates remaining supplys after shore leave
remaining_supplys = supplys - shore_leave
print(f"Supplys required for shore leave: {shore_leave}")
print(f"Remaining Supplys: {remaining_supplys}")

#calculates mira's share(prior to the standard distribution). Then subtracts that from the remaining
mira = (remaining_supplys * .13)
remaining_supplys = remaining_supplys - (remaining_supplys * .13)

#calculates Tov's share(prior to standard distribution). Then subtracts that from the remaining.
tov = (remaining_supplys * .11)
remaining_supplys = remaining_supplys - (remaining_supplys * .11)

#calculates the standard share for each citizen
crew = (remaining_supplys / 20) + 3

#calculates Mira and Tov's final shares
mira = mira + crew
tov = tov + crew

#rounds outputs
final_mira = round(mira, 2)
final_tov = round(tov, 2)
final_crew = round(crew, 2)

#displays all shares
print(f"Captain Mira's share: {final_mira}")
print(f"Tov's share: {final_tov}")
print(f"Crew share: {final_crew}")