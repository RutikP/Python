fname = "Rutik"
lname = "Panchal"
message = f'my name is {fname} {lname}'
print(message)
print(message.index("t"))
print(message.find("Ru"))
print(message.upper())
print(message.replace("Rutik", "Ashok"))

# Returns a right trim version of the stringReturns a right trim version of the string
sentens = "my name is Rutik"
print(sentens.rsplit())


# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# The split() method splits the string into substrings if it finds instances
# of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# Check if the phrase "ain" is NOT present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

# String Concatenation:
a = "Hello"
b = "World"
c = a + b
print(c)


# String Format:
age = 36
txt = "My name is John, I am "+str(age)
print(txt)


# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))

"""The escape character allows you to use double quotes when
 you normally would not be allowed:"""
txt = "We are the so-called \"Vikings\" from the north."

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
# Here whatever number used here are in octal numbers, which are converted to
# ascii letters makes one word
"""Example:
110: 1(8^2)+1(8^1)+0(8^0) => 64+8+0 = 72 = h(becoz->In ascii letters start from
65 that is 'a', and upto 90 that is 'z') """


# print(r'that\'s a really beautiful place') # Here "r" is row, backslash is also
# printed in output


s1 = "times of india"
s2 = "bangalore"
mid = int(len(s1)//2)
print(s1[:mid]+s2+s1[mid:])

"""The isX String Methods"""

print('wish'.isalpha())  # prints true
print('MANAGE'.isalpha())  # prints true
print('abcDEF'.isalpha())  # prints true
print('101abe'.isalpha())  # prints false
print('102abe'.isalnum())  # prints true
print('102ABC'.isalnum())  # prints true
print('102ABC#$'.isalnum())  # prints false
print('102'.isalnum())  # prints true
print('102.2'.isalnum())  # prints false
print('102.2'.isdecimal())  # prints false becoz it's float
print(' '.isspace())  # prints True becoz it should consist only spaces,tabs and newlines
print('\n\t\n\t'.isspace())  # prints true
print('My name is Rutik'.isspace())  # prints false
# istitle means a every word in a string should start with Caps then only it returns true
print('Hi buddy'.istitle())  # prints false
print('Hi Buddy'.istitle())  # Returns True

# while True:
#     age = input("Enter your valid age: ")
#     if age.isdecimal():
#         print("OK, This is valid")
#         break
#     else:
#         continue


print('Hello world'.startswith('Hello'))  # Prints True
print('Hello world'.endswith('world'))  # Prints True

import pprint

msg = 'Hello and welcome to Birthday Party'
print(msg)
"""Output: Hello and welcome to Birthday Party"""
pprint.pprint(msg)
"""Output: 'Hello and welcome to Birthday Party' """

count = {}
for c in msg:
    count.setdefault(c, 0)
    count[c] = count[c] +1
pprint.pprint(count)

# Find method returns the index of the first occurence of
# s in the string or -1 if s doesn't occcur in the string

# find(sunstr)

hstr = "lacosta"
# print(hstr.find('co'))
# print(hstr.find('oc'))

# find(substr, beg) # search substr in string from beg
# position

print(hstr.find('o', 2)) #  So here find fun will start searching from index 2
print(hstr.find('o', -1)) #  Gives -1
print(hstr.find('a', -1))  # Gives me 6

# find(sustr, beg, end) Search substr in string within beg index
# and end index
print('lacosta'.find('c', 3, 5))

pivalue = 3.1415
print("pi value rounded to {0} decimal places is {1:.2f}".format(2, pivalue))
print("pi value rounded to {0} decimal places is {1:.3f}".format(2, pivalue))
# split(saperator, maxsplit)
sen = 'Hello and welcome to Birthday Party. Web based projects are interesting and ' \
      'fun. Python frameworks like Django and Flask are more popular.Hello and welcome to Birthday Party '
cou = len((sen.split()))
print(sen.split('.'))
print(cou)
print(sen.split('are', 1))

# join() methods joins the all string present in the list
print(' '.join(['my', 'name', 'is', 'Rutik']))
# The above list prints "my name is Rutik"
print(','.join(['Cat', 'Dog', 'Rat', 'Lion']))
str1 = "abc"
print(str1.join(['All', 'is', 'well']))
