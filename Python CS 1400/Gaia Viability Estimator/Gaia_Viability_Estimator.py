#import the command line prompts and prepares a list
import sys

potential_populations = []


#prints the command line arguments so we can check them
print(sys.argv)

#uses the variables for the equation, and writes to the list
def equation(initial_population, growth_rate, iterations):

    #Adds the first value to the list so that it can work
    potential_populations.append(initial_population)


    #uses the reverse indexing to always have the most recent iteration
    population = potential_populations[-1]
    for num in range(iterations):
        population = growth_rate * population * (1- population)
        potential_populations.append(population)




#converts the command line inputs to variables, and calls the equation function
def main():
    #checks to make sure the command line has the proper amount of inputs
    if len(sys.argv) > 5:
        print("Command Line Error (too many arguments)")
        return
    elif len(sys.argv) < 5:
        print("Command Line Error (too few arguments)")
        return
    else:
        pass

    initial_population = float(sys.argv[1])
    growth_rate = float(sys.argv[2])
    iterations = int(sys.argv[3])
    output = sys.argv[4]

    #Validates command line inputs
    if initial_population < 0 or initial_population > 1:
        print("Initial Population must be between 0 and 1")
        return
    elif growth_rate < 0 or growth_rate > 4:
        print("Growth rate must be between 0 and 4")
        return
    elif iterations < 0:
        print("Iterations must be positive")
        return
    else:
        pass



    equation(initial_population, growth_rate, iterations)
    #checks that a file exicts. creates it if it doesn't and writes to it if it does
    current_iteration = 0
    try:
        with open(sys.argv[4], "x") as file:
            print("File not found, creating new file")
            for word in potential_populations:
                file.write(f"{current_iteration}   {word:.3f}\n")
                current_iteration += 1
    except FileExistsError:
        print("File Found!")
        with open(sys.argv[4], "w") as file:
            for word in potential_populations:
                file.write(f"{current_iteration}   {word:.3f}\n")
                current_iteration += 1




#initiates the program
if __name__ == "__main__":
    main()