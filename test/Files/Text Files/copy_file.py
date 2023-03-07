def copyfile(infilename, outfilename):
    infile = open(infilename)
    outfile = open(outfilename, 'w')
    for line in infile:
        outfile.write(line)



print(copyfile("HumptyDumpty.txt", "Rutik.txt"))