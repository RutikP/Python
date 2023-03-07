import csv


def read_csv_file(filename):
    f = open(filename)
    for row in csv.reader(f):
        print('"', row[0], '"', ',',  row[1], ",", row[2], end="")
        print()


print(read_csv_file("BooksRead.csv"))
