import numpy as np

a=np.array([[4,5],[3,6],[5,7],[4,6]])
b=np.array([[1,2],[3,4],[4,5],[3,7],[5,7]])

def intersect2d(X, Y):
    """
    Function to find intersection of two 2D arrays.
    Returns index of rows in X that are common to Y.
    """
    X = np.tile(X[:,:,None], (1, 1, Y.shape[0]) )
    Y = np.swapaxes(Y[:,:,None], 0, 2)
    Y = np.tile(Y, (X.shape[0], 1, 1))
    eq = np.all(np.equal(X, Y), axis = 1)
    eq = np.any(eq, axis = 1)
    return np.nonzero(eq)[0]

print a[intersect2d(a,b)]
print b[intersect2d(b,a)]


def union2d(X, Y):
    """
    Function to find intersection of two 2D arrays.
    Returns index of rows in X that are common to Y.
    """
    X = np.tile(X[:,:,None], (1, 1, Y.shape[0]) )
    Y = np.swapaxes(Y[:,:,None], 0, 2)
    Y = np.tile(Y, (X.shape[0], 1, 1))
    eq = np.all(np.equal(X, Y), axis = 1)
    eq = np.any(eq, axis = 1)
    return np.nonzero(eq)[0]


    
#set(map(tuple, a)).isdisjoint(map(tuple, b))
