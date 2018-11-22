def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)


# Brackets --> Indents
def fib(n):
    # Indent level 1: function body
    if n <= 1:
        # Indent level 2: if statement body
        return 1
    else:
        # Indent level 2: else statement body
        return fib(n - 1) + fib(n - 2)


# Classes
class Animal(object):
    def __init__(self, species, age):   # Constructor 'a = Animal('bird', 10)'
        self.species = species          # Refer to instance with 'self'
        self.age = age                  # All instance variables are public

    def isPerson(self):                 # Invoked with 'a.isPerson()'
        return self.species == "Homo Sapiens"

    def ageOneYear(self):
        self.age += 1


class Dog(Animal):                      # Inherits Animal's methods
    def ageOneYear(self):               # Override for dog years
        self.age += 7


if __name__ == '__main__':
    print(QuickSort([3, 6, 8, 10, 1, 2, 1]))

    x = 10  # Declaring two integer variables
    y = 3   # Comments start with the hash symbol
    print(x + y)    # Addition
    print(x - y)    # Subtraction
    print(x ** y)   # Exponentiation
    print(x // y)    # Dividing two integers
    print(x / float(y))     # Type casting for float division
    print(str(x) + " + " + str(y))  # Casting and string concatenation

    print(fib(10))

    # List Slicing
    numbers = [0, 1, 2, 3, 4, 5, 6]
    print(numbers[0:3])
    print(numbers[:3])
    print(numbers[5:])
    print(numbers[5:7])
    print(numbers[:])
    print(numbers[-1])  # Negative index wraps around
    print(numbers[-3:])
    print(numbers[3:-2])    # Can mix and match

    # Collections: Tuple
    names = ('Zach', 'Jay')     # Note the parentheses
    names[0] == 'Zach'
    print(len(names) == 2)
    print(names)
    # names[0] = 'Richard'      # Error
    empty = tuple()     # Empty tuple
    single = (10,)      # Single-element tuple. Comma matters!

    # Collections: Dictionary
    phonebook = dict()  # Empty dictionary
    phonebook = {'Zach': '12 - 37'}  # Dictionary with one item
    phonebook['Jay'] = '34 - 23'  # Add another item
    print('Zach' in phonebook)
    print('Kevin' in phonebook)
    print(phonebook['Jay'])
    del phonebook['Zach']  # Delete an item
    print(phonebook)
    for name, number in phonebook.items():
        print(name, number)

    # Loops
    for name in ['Zack', 'Jay', 'Richard']:
        print('Hi ' + name + '!')

    while True:
        print('We\'re stuck in a loop...')
        break   # Break out of the while loop

    # Loops (cont'd)
    for i in range(10):     # Want an index also?
        print('Line ' + str(i))     # Look at enumerate()!

    for idx, ele in enumerate([3, 4, 5]):
        print(str(idx) + ':' + str(ele))

    # Looping over a list, unpacking tuples:
    for x, y in [(1, 10), (2, 20), (3, 30)]:
        print(x, y)

    # Classes
    a = Animal('bird', 10)
    print(a.isPerson())
    print(a.age)
    a.ageOneYear()
    print(a.age)
    d = Dog('ben', 10)
    print(d.isPerson())
    print(d.age)
    d.ageOneYear()
    print(d.age)

    # Importing Modules
    # Import 'os' and 'time' modules
    import os, time

    # Import under an alias
    import numpy as np
    print(np.dot(x, y))    # Access components with pkg.fn

    # Import specific submodules/functions
    from numpy import linalg as la, dot as matrix_multiply

    # Not really recommended b/c namespace collisions...

    # Iterables (cont'd)
    names = set(['Zack', 'Jay'])
    # print(names[0])     # TypeError: 'set' object does not support indexing
    print(len(names) == 2)
    print(names)
    names.add('Jay')
    print(names)    # Ignored duplicate

    empty = set()   # Empty set
