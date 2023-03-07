# namedtuple() which returns a named value for each element in a tuple
from collections import namedtuple

a = namedtuple('courses', 'name,technology')
b = a('data science', 'python')
print(b)
x = a._make(['data science', 'python'])
print(x)

print()
# deque pronounced as 'deck' is an optimized list to perform insertion and deletion easily
from collections import deque

a = ['r', 'u', 't', 'i', 'k']
d = deque(a)
print(d)


d.append('python')
print(d)
d.pop()
d.appendleft('Java')
print(d)
d.popleft()
print(d)

#  Chainmap is a dictionary like class for creating a single view of multiple mappings
from collections import ChainMap

A = {1: 'Rutik', 2: 'Sahil', 3: 'Sarthak'}
B = {4: 'Pavan', 4: 'Rushi', 6: 'Shanu'}
c = ChainMap(A, B)
print(c)

# Counter is a dictionary subclass for counting hashable objects
from collections import Counter

A = [1, 1, 2, 3, 4, 2, 7, 6, 4, 3, 2, 1, 5, 3, 2, 4, 2, 6, 3, 4, ]
B = Counter(A)
print(B)
print(B.most_common())
sub = {2: 1, 6: 2}
B.subtract(sub)
print(B.most_common())

# OrderedDist
from collections import OrderedDict
d = OrderedDict()
d[1] = 'P'
d[2] = 'A'
d[3] = 'N'
d[4] = 'C'
d[5] = 'H'
d[6] = 'A'
d[7] = 'L'
print(d)
print(d.keys())

d[1] = 'p'
print(d)

# defaultdict: it is a dictionary subclass which calls a factory function to supply missing values
from collections import defaultdict
d = defaultdict(int)
d[1] = 'Python'
d[2] = 'Java'
print(d)
print(d[0])