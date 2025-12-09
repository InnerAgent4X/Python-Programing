import csv
from datetime import date
from dateutil.relativedelta import relativedelta


def job_data():
    print("job_data")
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
    print("presidents_parser")
    pres_data = []
    democrats = []
    republicans = []
    with open('presidents.txt', 'r') as file:
        for line in file:
            #creates a list and strips the spaces and splits on pipes
            pres_data.append([x.strip() for x in line.strip().split('|')])

        #converts the string date data into dates
        for item in pres_data:
            item[1] = date(year= int(item[2]), month= int(item[1]), day= 1)
            item[3] = date(year= int(item[4]), month= int(item[3]), day=1)
            item.remove(item[2])
            item.remove(item[3])


        #sorts items into lists
        for row in pres_data:
            if row[-1] == 'Democratic':
                democrats.append(row)
            elif row[-1] == 'Republican':
                republicans.append(row)
            else:
                print('Error')
        print(democrats)
        print(republicans)



        for pres in pres_data:
            term = relativedelta(pres[2], pres[1])
            diff_months = term.years * 12 + term.months

            print(diff_months)






def main():
    print("main")
    presidents_parser()
    #job_data()









if __name__ == '__main__':
    main()