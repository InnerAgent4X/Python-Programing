import matplotlib.pyplot as plt
import random


def lance_walk(astronauts):
    x = 0
    y = 0
    for i in range(1, 501):
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


def sophie_walk(astronauts):
    x = 0
    y = 0
    for i in range(1, 501):
        movement = random.choices(["up", "down", "left", "right"], weights = [50, 16.67, 16.67, 16.67], k=1)[0]
        if movement == "up":
            y += 1
        elif movement == "down":
            y -= 1
        elif movement == "left":
            x -= 1
        elif movement == "right":
            x += 1
        else:
            print("something went wrong")
        astronauts["Sophie"].append((x, y))


def finn_walk(astronauts):
    x = 0
    y = 0
    for i in range(1, 501):
        movement = random.choice(["left", "right"])
        if movement == "left":
            x -= 1
        elif movement == "right":
            x += 1
        else:
            print("something went wrong")
        astronauts["Finn"].append((x, y))


def plot_graph(x_positions, y_positions, astronaut_name, color, marker):
    """
    Visualizes the spacewalk path of an astronaut.

    Parameters:
    - x_positions: list of x coordinates
    - y_positions: list of y coordinates
    - astronaut_name: name of the astronaut (e.g., "Lance", "Sophie", "Finn")
    - color: color for the path (e.g., 'blue', 'red', 'green')
    - marker: marker style (e.g., 'o' for circles, 's' for squares, '^' for triangles)
    """
    plt.figure(figsize=(10, 10))

    # Plot the path with lines connecting the points
    plt.plot(x_positions, y_positions, color=color, alpha=0.3, linewidth=0.5)

    # Plot the individual positions with markers
    plt.scatter(x_positions, y_positions, c=color, marker=marker, s=20, alpha=0.6)

    # Mark the starting position
    plt.scatter(x_positions[0], y_positions[0], c='black', marker='*', s=200,
                label='Start', zorder=5)

    # Mark the ending position
    plt.scatter(x_positions[-1], y_positions[-1], c='gold', marker='*', s=200,
                label='End', zorder=5)

    plt.xlabel('X Position', fontsize=12)
    plt.ylabel('Y Position', fontsize=12)
    plt.title(f"{astronaut_name}'s Spacewalk Path", fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.axis('equal')

    # Save the figure
    filename = f"{astronaut_name}_spacewalk.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved {filename}")



def main():
    #dictionary with lists to store the movement paths
    astronauts = {
        "Lance": [(0,0)],
        "Sophie": [(0,0)],
        "Finn": [(0,0)]

    }
    #First set the x and y positions to empty lists(so we can use them with all new data. then unpacks the tuples into the lists.
    x_positions = []
    y_positions = []
    lance_walk(astronauts)
    for item in astronauts["Lance"]:
        x_positions.append(item[0])
        y_positions.append(item[1])
    plot_graph(x_positions, y_positions, astronaut_name = "Lance" ,color = "blue", marker = "o")
    print(astronauts["Lance"])

    x_positions = []
    y_positions = []
    sophie_walk(astronauts)
    for item in astronauts["Sophie"]:
        x_positions.append(item[0])
        y_positions.append(item[1])
    plot_graph(x_positions, y_positions, astronaut_name = "Sophie" ,color = "red", marker = "s")
    print(astronauts["Sophie"])

    x_positions = []
    y_positions = []
    finn_walk(astronauts)
    for item in astronauts["Finn"]:
        x_positions.append(item[0])
        y_positions.append(item[1])
    plot_graph(x_positions, y_positions, astronaut_name = "Finn" ,color = "green", marker = "^")
    print(astronauts["Finn"])

if __name__ == '__main__':
    main()