# # duplicate values are not present in Dictionary
# # Dictionary is a collection which is unordered, changeable and indexed.No duplicate members.
# courses = {1: 'CSE', 2: 'ELE', 'third': 'CIVIL'}
# print(courses)
# print(courses['third'])
# print(courses.get(2))
# courses['third'] = 'MECHANICAL'  # updating the values
# print(courses)
# courses[4] = 'AURONATICAL'
# print(courses)
# # Dictionary Methods
# car = {1: 'Alto', 2: 'Swift', 3: 'Audi', 4: 'Nano'}
# print(car)
# c = car.copy()
# print(c)
# car.clear()
# print(car)
#
# # fromkeys
# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x, y)
# print(thisdict)
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.items()
# print(x)
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.keys()
# print(x)
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# car.pop("model")
# print(car)
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# car.popitem()  # popitem() function will delete the last item in the dict
# print(car)
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.setdefault("model", "Bronco")
# print(x)
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(car)
# car.update({"color": "White"})
# print(car)
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.values()  # This will show only the values in the output
# print(x)
#
# print()
#
# mycat = {'color': 'white', 'size': 'medium', 'height': '3feet', 'age': '14days'}
#
# print(mycat)
#
# print(mycat['size'])
#
# print('mycat has ' + mycat['color'] + ' fur')
# print()
#
# spam = {1: 'a', 2: 'b', 3: 'c'}
# bacom = {4: 'd', 5: 'e', 6: 'f'}
# print(spam == bacom)  # it prints false
#
# print()
#
# birthday = {'Nisha': 'SEP 12', 'Chinnu': 'MAY 14'}
#
# while True:
#     print("Enter the name: ")
#     name = input()
#     if name == ' ':
#         print(birthday)
#         break
#     if name in birthday:
#         print(birthday[name], " is the bday date of  " + name)
#     else:
#         print("I don't have birthday information for " + name)
#         print("What is the DOB")
#         birthday[name] = input()
#         print("Birthday database updated")
#
# # Printing KEYS and VALUES from dictionary
# print()
#
# mycat = {'size': 'fat', 'color': 'red', 'age': '15 days'}
# print(mycat)
# print()
# print("mycat values:")
# for v in mycat.values():
#     print(v + ",", end="")
# print()
# print("mycat keys:")
# for k in mycat.keys():
#     print(k + ",", end="")
#
# print()
#
# # Checking whether key or value exists in Dictionary
# mycat = {'size': 'fat', 'color': 'red', 'age': '15 days'}
#
# print('size' in mycat.keys())
# print('height' in mycat.keys())
# print()
#
# print('red' in mycat.values())
# print('15 inch' in mycat.values())
#
# print()
#
# courses = {1: 'CSE', 2: 'ELE', 'third': 'CIVIL', 'third': 'D'}
# print(courses)
#
# print()
#
# # -----------------------------------------------------------------------------------------------------------------------
#
#
# my_details = {'Employee': {'Dave': {'Salary': '2500', 'ID': '001', 'Designation': 'Team Lead'},
#                            'Joe': {'Salary': '40000', 'ID': '002', 'Designation': 'Associate'}}}
# print(my_details)
#
# import pandas as pd
#
# df = pd.DataFrame(my_details['Employee'])
# print(df)

dict = {}
def add():
    wordname = input("Enter word")
    wordmeaning = input("Enter its meaning")
    dict.update({wordname:wordmeaning})


def search():
    findmeaningof = input("Enter the word")
    if findmeaningof in dict.keys():
        print(dict[findmeaningof])
    else:
        print("Not found in dictionary")


def main():
    option = input("If you want to search in dict enter 'search' or you want to Add to dictionary enter 'add'")
    if option == "search":
        search()
    if option == "add":
        add()


main()



