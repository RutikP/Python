# 4th Program
# count = 0
# total = 0
# num = " "
# avg = 0
#
# while num != "done":
#     num = input("Enter number")
#     if num == "done":
#         print("Count:", count)
#         print("Total:", total)
#         avg = total / count
#         print("Avg:", avg)
#     elif num.isdigit():
#         num = int(num)
#         if (num % 2) == 0:
#             count += 1
#             total += int(num)
#         else:
#             print("Enter only even numbers")
#     else:
#         if (num != "done"):
#             print("Enter only even numbers")

# =============================================================================================
"""6th Program"""

import sys
dict = {}
option = ""
while option != exit:
    def add():
        global dict
        wordname = input("Enter word")
        wordmeaning = input("Enter its meaning")
        dict.update({wordname:wordmeaning})


    def search():
        global dict
        findmeaningof = input("Enter the word")
        if findmeaningof in dict.keys():
            print(dict[findmeaningof])
        else:
            print("Not found in dictionary")

    def showitems():
        global dict
        for i in sorted(dict.keys()):
            print(i+" : "+dict[i],end=", ")
        print()



    def main():
        global dict
        global option
        option = input("1)If you want to search in dict enter 'search' \n"
                       "2)If you want to Add to dictionary enter 'add'\n"
                       "3)enter exit to exit \n"
                       "4)Enter show to show dict values\n")
        if option == "search":
            search()
        if option == "add":
            add()
        if option == "exit":
            sys.exit()
        if option == "show":
            showitems()


    main()


