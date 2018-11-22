import numpy as np
x = np.array([1, 2, 3])
y = np.array([[3, 4, 5]])
z = np.array([[6, 7], [8, 9]])
print(x)
print(y)
print(z)
print(x.shape)  # A list of scalars!
print(y.shape)  # A (row) vector!
print(z.shape)  # A matrix!

x = np.array([[1, 2], [3, 4]])
print(np.max(x, axis=1))
print(np.max(x, axis=1, keepdims=True))
print(np.min(x, axis=1, keepdims=True))
print(np.argmax(x, axis=1))
print(np.sum(x, axis=1, keepdims=True))
print(np.mean(x, axis=1, keepdims=True))

print(np.array([1, 2, 3]).T)
# print(np.sum(np.array([1, 2, 3]), axis=1))   # Error
print(np.sum(np.array([1, 2, 3]), axis=0))

# Indexing
x = np.random.random((3, 4))    # Random (3, 4) matrix
print(x)
print(x[:])                     # Selects everything in x
print(x[np.array([0, 2]), :])   # Selects the 0th and 2nd rows
print(x[1, 1:3])                # Selects 1st row as 1-D vector, and 1st through 2nd elements
print(x[x > 0.5])               # Boolean indexing

# Broadcasting
x = np.random.random((3, 4))    # Random (3, 4) matrix
y = np.random.random((3, 1))    # Random (3, 1) matrix
z = np.random.random((1, 4))    # Random (3,) vector
print('x = ' + str(x))
print('y = ' + str(y))
print('z = ' + str(z))
print(x + y)    # Add y to each column of x
print(x * z)    # Multiplies z element-wise with each row of x
print((y + y.T).shape)  # Can give unexpected results!

# Avoid explicit for-loops over indices/axes at all costs.
