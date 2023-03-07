# import sys
#
# lis = []
# num = 0
#
#
# def cal(x):
#     j = 0
#     res = 0
#     res = float(res)
#     for i in x:
#         j += i
#     y = len(x)
#     res = float(j/y)
#     print("Avg: ", res)
#
#
# def avg():
#     global num
#     global lis
#     x = "end"
#     num = input("Enter number: ")
#     if num != x:
#         if num.isdigit():
#             num = int(num)
#             lis.append(num)
#             avg()
#         else:
#             print("Enter num to add in list or enter \"end\" to get avg")
#             avg()
#
#     elif num == "end":
#         if len(lis) != 0:
#             cal(lis)
#             sys.exit()
#         else:
#             sys.exit()
#
#
#
# avg()

















#
import re
# s = 'abc123 xyz666 lmn-11 def77'
# print(re.sub(r'\b([a-z]+)(\d+)',r'\2\   ',s))

# n = re.sub(r'\w+','Hello','Cats and dogs')
# print(n)

# w = re.compile('[A-Za-z]+')
# print(w.findall('It will rain today'))

# print(re.split(r'\s+','Chrome is better than explorer', maxsplit=3))

# temp = 'indiparker@ind.com'
# temp1=''
# if(re.search(r'@ind\.',temp)):
#     temp1 = re.sub(r'i\w+(\.com)',r'edu\1',temp)
# print(temp1)


# str = "Encountered Error : error code E101"
# if(re.search(r"E...r",str) != None):
#     str2 = re.sub(r"E(\d{3})",r"#\1",str)
#     print(str2)


# Nameage = '''
# Janice is 22 and Theon is 33
# Gabriel is 44 and Joey is 21
# '''
# ages = re.findall(r'\d{1,3}', Nameage)
# names = re.findall(r'[A-Z][a-z]*',Nameage)
# ageDict = {}
# x = 0
# for eachname in names:
#     ageDict[eachname] = ages[x]
#     x +=1
# print(ageDict)

# def text_match(text):
#     patterns = '^[a-z]+_[a-z]+$'
#     if not re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not Matched!')
# print(text_match("aab_cbbbc"))
# print(text_match("aab_Abbbc"))
# print(text_match("Aaab_abbbc"))


