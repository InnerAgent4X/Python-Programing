import csv
from datetime import date
from dateutil.relativedelta import relativedelta


def job_data(pres_data):
    print("job_data")
    print('-' * 20)

    # opens and reads the csv file into a dictionary
    #IMPORTANT!!!
    #To change between provided sheet and the one I downloaded, just change "p7" to "mine"
    with open('BLS_private_p7.csv', newline='') as csvfile:
        values = csv.DictReader(csvfile)

        #creates a more usable list
        all_jobs = []
        for row in values:
            row.pop('Year')
            all_jobs.append(row)

        #removes the year collum, then converts strings to ints.
        all_jobs_lst = []
        for year in all_jobs:
            all_jobs_lst.extend(list(year.values()))
        jobs_numbers = list(map(int, all_jobs_lst))


        #dict and variables for storing and processing the growth factors.
        jobs_presidents = {
            'Democrat': 0,
            'Republican': 0
        }

        #subtracts the end month from the start month from each president to find the total gain/loss per president
        past_pres = 0
        president_number = 0
        for pres in pres_data:
            job_growth = jobs_numbers[pres[1]-1 + past_pres] - jobs_numbers[past_pres]
            # print(jobs_numbers[pres[1]-1])
            # print(jobs_numbers[past_pres])
            # print(job_growth)
            #sorts the results into the seperate parties
            if pres[2] == 'Democratic':
                jobs_presidents['Democrat'] += job_growth
            elif pres[2] == 'Republican':
                jobs_presidents['Republican'] += job_growth
            past_pres = past_pres + pres[1] - 1
            president_number += 1
            print(f"{president_number} : {jobs_presidents}")

        print('-' * 20)
        print(f'Final Results : Democratic Party {jobs_presidents['Democrat']/1000} Million')
        print(f'Final Results : Democratic Party {jobs_presidents['Republican'] / 1000} Million')
        print('=' * 20)


#opens presidents doc and creates a list
def presidents_parser():
    print("presidents_parser")
    print('-' * 20)
    pres_data = []
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

        #uses the dates to find the amount of time in between, then converts to months
        for pres in pres_data:
            term = relativedelta(pres[2], pres[1])
            diff_months = term.years * 12 + term.months

            pres[1] = diff_months
            pres.remove(pres[2])


        print(pres_data)
        print('=' * 20)
        return pres_data






def main():
    print("main")
    print('=' * 20)

    job_data(presidents_parser())






if __name__ == '__main__':
    main()