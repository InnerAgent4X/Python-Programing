import sys

#Itemizes the objects in the dictionary and prints them all.
def analyze_scores(scorebook):
    for student in scorebook.items():
        key = student[0]
        score = student[1]
        print(f"{key}: {score}")

    #Performs all the changes and prints the average after the changes.
    scorebook['Dana'] = 85
    print(f"Updated Dana's score to {scorebook['Dana']}.")

    scorebook.pop('Bob')
    print('Removed Bob from the scorebook.')

    print(scorebook.get('Eve', 'Eve not found in scorebook.'))

    print(f"Average score: {sum(scorebook.values())/len(scorebook):.2f}")


#Creates empty dictionary, then manually adds the values.
def main():

    scorebook = {}

    scorebook['Alice'] = 88
    scorebook['Bob'] = 75
    scorebook['Charlie'] = 93
    scorebook['Dana'] = 80


    analyze_scores(scorebook)

#Initalizes program
if __name__ == '__main__':
    main()