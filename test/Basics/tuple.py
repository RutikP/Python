animals = (10, 20, 30, 'tiger', 'lion', 'tiger')
print(animals)
print(animals[2])
print(animals.count('tiger'))
print(animals[::-1])
rutik = list(dict.fromkeys(animals))
print(rutik)
# the difference b/w tuple and list are, Tuples cannot be changed unlike lists.
# Tuples use parentheses, whereas lists use square brackets.

# index
thistuple = (1, 3, 7, 10, 8, 5, 4, 6, 5, 8)
x = thistuple.index(8)
print(x)
# count
y = thistuple.count(8)
print(y)

# Tuple
print(type(('hello',)))
# not a Tuple
print(type(('hello')))
