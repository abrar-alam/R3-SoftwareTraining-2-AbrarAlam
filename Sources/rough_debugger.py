from random import seed
from random import choice

seed()
myList = [0]
sequence = [i for i in range(20)]
x = choice(myList)

seed(1)
y = choice(sequence)
print(x,y)
