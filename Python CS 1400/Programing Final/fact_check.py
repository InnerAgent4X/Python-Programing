import csv
from datetime import date
from dateutil.relativedelta import relativedelta


def job_data():
    # opens and reads the csv file into a dictionary
    with open('BLS_private_mine.csv', newline='') as csvfile:
        values = csv.DictReader(csvfile)
        for row in values:
            #Converts the strings to integers
            for key,value in row.items():
                row[key] = int(value)

            print(row)






#opens presidents doc and creates a list
def presidents_parser():
    pres_data = []
    with open('presidents.txt', 'r') as file:
        for line in file:
            #creates a list and strips the spaces and splits on pipes
            pres_data.append([x.strip() for x in line.strip().split('|')])

        for row in pres_data:
            pres_data[1] = date(pres_data[2],pres_data[1],1 )
            pres_data[3] = date(pres_data[4],pres_data[3],1 )

    print(pres_data)







def main():
    print("test")
    presidents_parser()
    #job_data()










if __name__ == '__main__':
    main()