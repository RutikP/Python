def print_file(filename):
    infile = open(filename)  # Here infile is to handle that file

    for line in infile:
        print(line, end="")


print(print_file("Biodata.txt"))


