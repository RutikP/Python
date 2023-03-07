# Finding patterns of Text using RegExp

import re
# SYNTAX => re.compile(pattern, flags)
"""Method-1"""
# PNRE = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
"""now PNRE has the regex object
re.compile returns regex object"""
# mo = PNRE.search("My number is 434-532-6464.")
# SYNTAX => re.search(pattern,string, flags)
# print('Phone number found is : ', mo.group())

'''the search method will return None if the regex pattern is not found in the string
else it returns the match object and match object have a group method that will return the matched text'''

'''Method-2'''
# PNRE1 = re.compile(r'\d\d-\d\d\d-\d\d\d\d')
# if(PNRE1.search("My number is 434-534-6464.") != None):
#     print('Phone number found is : ', PNRE1.search("My number is 434-532-6464.").group())
# else:
#     print("Pattern not found")

'''Method-3'''
# if(re.search(r'\d\d-\d\d-\d\d\d\d', "My code is 22-12-4212") != None):
#     print("Pattern found")
# else:
#     print("Pattern not found")

# PNRE2 = re.compile(r'\d\d\d-\d\d-\d\d\d\d')
# mo = PNRE2.search("My code is 213-21-4121")
# if mo != None:
#     print(mo.group())
# else:
#     print("Pattern not found")

# ts = "My code is 213-41-4121"
# if re.search(r'\d\d\d-\d\d-\d\d\d\d', ts) != None:
#     print("Pattern found")
# else:
#     print("Pattern not found")

'''Grouping with Parentheses'''

# regexobj = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
# mo = regexobj.search("My code is 273-412-4121")
# if mo != None:
'''print(mo.group(1))
    print(mo.group(0))
    print(mo.group())
    print(mo.groups())'''
#     areacode, phno = mo.groups()
#     print("areacode: ", areacode)
#     print("phno: ", phno)
# else:
#     print("No pattern matched")


'''Escaping the ( and ) characters'''
# regexobj = re.compile(r'(\(\d\d\d\) (\d\d\d-\d\d\d))')
# mo = regexobj.search("My code is (273) 412-4121")
# if mo != None:
#     print(mo.group())
# else:
#     print("Pattern not matched")

# --------------------------------------------------------------------

'''Matching Multiple Groups with the pipe'''
'''Ex-1'''
# regexobj = re.compile('Batman|Tiny fey')
# mo = regexobj.search("Tiny fey and Batman are coming today")
# print(mo.group())

'''Ex-2'''
regexobj2 = re.compile(r'Superman_(Rushi|Sahil|Pavan)')
mo = regexobj2.search("Superman_Rushi and Superman_Sahil came to my home yesterday and we missed Pavan")
mo1 = regexobj2.search("Superman_Sahil and Superman_Rushi came to my home yesterday and we missed Pavan")
print(mo.group()) #  Gives output: Superman_Rushi
print(mo.group(1)) # Gives output: Rushi
print(mo1.group()) #  Gives output: Superman_Sahil
print(mo1.group(1)) # Gives output: Sahil

# ---------------------------------------------------------------------------


