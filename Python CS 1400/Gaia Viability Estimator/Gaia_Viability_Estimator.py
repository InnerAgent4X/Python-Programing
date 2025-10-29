#import the command line prompts and prepares a variable and a list
import sys

current_iteration = 0
potential_populations = []

#uses the variables for the equation, and writes to the list

def equation(initial_population, growth_rate, iterations):
    potential_populations.append(f"{current_iteration}   {initial_population}")
    print(potential_populations[0])

    population = potential_populations[current_iteration]
    for num in range(iterations):
        population = growth_rate * population









#converts the command line arguments to variables, and calls the equation function
def main():
    if len(sys.argv) != 5:
        print("Command Line Error (too many or too few arguments)")
        return

    initial_population = float(sys.argv[1])
    growth_rate = float(sys.argv[2])
    iterations = int(sys.argv[3])
    output = sys.argv[4]

    equation(initial_population, growth_rate, iterations)




#initiates the program
if __name__ == "__main__":
    main()