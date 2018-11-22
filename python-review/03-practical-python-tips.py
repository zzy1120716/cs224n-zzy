squares = []
for i in range(10):
    squares.append(i**2)
print(squares)
# following is equivalent
squares = []
squares = [i ** 2 for i in range(10)]
print(squares)
# conditional
odds = [i**2 for i in range(10) if i % 2 == 1]
print(odds)

# Multiple assignment / unpacking iterables
x, y, z = ['Tensorflow', 'PyTorch', 'Chainer']
age, name, pets = 20, 'Joy', ['cat']

# Returning multiple items from a function
def some_func():
    return 10, 1
ten, one = some_func()
print(ten, one)

# Joining list of strings with a delimiter
print(",".join(['1', '2', '3']))

# String literals with both single and double quotes
message = 'I like "single" quotes.'
reply = "I prefer 'double' quotes."
print(message)
print(reply)

class Duck(object):
    def quack(self):
        pass

bird = Duck()
print(type(bird))
print(dir(bird))

# Numpy Debugging
import numpy as np
x = np.array([[0, 0, 0]])
y = np.array([[1, 2, 3]])
# Checking if two float arrays are approximately equal (element-wise)
print(np.allclose(x, y))    # Can also specify tolerance
# Checking if an array is close to zero (e.g. gradient)
print(np.allclose(x, 0))    # Broadcasting
# Selecting all elements less than 0 from an array
z = np.random.random((3, 4))
print(z[z < 0.5])     # Returns 1-dim array
