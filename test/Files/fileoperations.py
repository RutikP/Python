# "r" - Read-Default value. Opens a file for reading.error if the file does not exixt.
# "a" - Append-Opens a file for appending, creates the file if it does not exxixt
# "w" - Write-Opens a file for writing.creates the file if it does not exixt
# "x" - create - creates the specified file, returns an error if the file exixts


import os

"""File Read-Methods"""
# file = open("C:/Users/admin/Desktop/testfile1.txt", 'r')
# print(file.read())
# file.close()

# file = open("C:/Users/admin/Desktop/testfile1.txt", 'r')
# print(file.read(5))
# file.close()

# file = open("C:/Users/admin/Desktop/testfile1.txt", 'w')
# file.close()

# file = open("C:/Users/admin/Desktop/testfile1.txt", 'r')
# print(file.readline())  # Reads only first line
# print(file.readline(2))  # Reads first two chars of firstline
# print(file.readlines())  # Reads all line from the file
# print(file.readlines(2))  # Reads 2nd line from the file
# file.close()


# file = open("C:/Users/admin/Desktop/testfile2.txt", 'r')
# for line in file:
#     print(file.readlines())
# file.close()


# File Write-Methods
"""File Handling - Writing"""
import os
# file = open('C:/Users/admin/Desktop/testfile3.txt', 'w')
# file.write('This is a test')
# file.write('\nTo add more line')
# file.close()
# File Handling - Overwritten
import os
# file = open('C:/Users/admin/Desktop/testfile3.txt', 'w')
# file.write('Oops overwritten')
# file.close()

"""File Handling - Creation"""
import os
# file = open('C:/Users/admin/Desktop/newcreatedfile.txt', 'x')
# file.write('New File')
# file.close()

"""File Handling - Removing file"""
# import os
# os.remove("C:/Users/admin/Desktop/testfile1.txt")

"""File Handling - Removing file"""
# Check if the file exists
# import os
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
# else:
#     print("The file does not exists")

"""File Handling - Removing folder/directory"""
# import os
# os.rmdir("myfolder")
