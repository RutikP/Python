import csv

print()


def read_csv_file(filename):
    f = open(filename)
    for row in csv.reader(f):
        print(row)

    print()

    k = open(filename)
    for row in csv.reader(k):
        print(row[0], "->", row[1], "\n")


print(read_csv_file("phones.csv"))


print()

import csv


def read_csv_file(filename):
    f = open(filename)
    for row in csv.reader(f):
        print(row)

    print()

    k = open(filename)
    for row in csv.reader(k):
        for row_item in row:
            print(row_item, end=",")
        print()



print(read_csv_file("menu.csv"))


import csv


def open_csv_file(filename):
    data = []
    m = open(filename)
    for row in csv.reader(m):
        data.append(row)
    print(data)


print(open_csv_file("phones.csv"))

print()


import csv


def read_csv_file(filename):
    f = open(filename)
    for row in csv.reader(f):
        print(row)


print(read_csv_file("holidays.csv"))  #  This "holidays.csv" file is not imported it is written in program "write_csv.py"