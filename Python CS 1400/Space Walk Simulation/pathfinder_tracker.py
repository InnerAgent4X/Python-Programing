import sys
import matplotlib.pyplot as plt
import random


def lance_walk(astronauts):
    x = 0
    y = 0
    for i in range(1, 11):
        movement = random.choice(["up", "down", "left", "right"])
        if movement == "up":
            y += 1
        elif movement == "down":
            y -= 1
        elif movement == "left":
            x -= 1
        elif movement == "right":
            x += 1

        astronauts["Lance"].append((x, y))










def plot_graph(coordinates, color, marker):

    for item in coordinates:
        plt.scatter(item[0], item[1], marker=marker, color=color)

    #plt.scatter(x_values, y_values, color = color, marker = marker )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Space Walk Simulation")
    plt.grid(True)
    plt.show()


def main():

    astronauts = {
        "Lance": [(0,0)],
        "Sophie": [(0,0)],
        "Finn": [(0,0)]

    }

    lance_walk(astronauts)
    coordinates = [astronauts["Lance"]]
    plot_graph(coordinates, "blue", "o")
    print(astronauts["Lance"])

if __name__ == '__main__':
    main()