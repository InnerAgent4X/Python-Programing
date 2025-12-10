import csv
from datetime import date
from dateutil.relativedelta import relativedelta


def job_data(pres_data):
    print("job_data")
    # opens and reads the csv file into a dictionary
    with open('BLS_private_mine.csv', newline='') as csvfile:
        values = csv.DictReader(csvfile)
        pres_counter = 0
        month_counter = pres_data[0][1]
        total_counter = 0

        jobs_presidents = {
            'Democrat': 0,
            'Republican': 0
        }
        done = False
        for row in values:
            if done:
                break
            #Converts the strings to integers
            for key,value in row.items():
                row[key] = int(value)

                if key == 'Year':
                    continue
                elif pres_data[pres_counter][2] == 'Democratic':
                    jobs_presidents['Democrat'] += row[key]
                    month_counter -= 1
                elif pres_data[pres_counter][2] == 'Republican':
                    jobs_presidents['Republican'] += row[key]
                    month_counter -= 1
                if month_counter == 0:
                    pres_counter += 1
                    if pres_counter == len(pres_data):
                        done = True
                        break
                    month_counter = pres_data[pres_counter][1]
                total_counter += 1
                print(f"{total_counter} : {jobs_presidents}")









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
                #for debugging
                print('Error, party not found')


        #uses the dates to find the amount of time in between, then converts to months
        for pres in pres_data:
            term = relativedelta(pres[2], pres[1])
            diff_months = term.years * 12 + term.months

            pres[1] = diff_months
            pres.remove(pres[2])


        print(pres_data)
        return pres_data






def main():
    print("main")

    job_data(presidents_parser())









if __name__ == '__main__':
    main()