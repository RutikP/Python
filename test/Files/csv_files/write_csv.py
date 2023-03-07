def write_csv(filename):
    import csv

    list = [['7-1-2020', 'Acharya habba'],
         ['10-2-2020', 'Panchami habba'],
         ['12-3-2020', 'Devali habba'],
         ['15-10-2020', 'Rutik Birthday']]

    f = open(filename, 'w', newline='')
    for item in list:
        print(csv.writer(f).writerow(item))


print(write_csv("holidays.csv"))
