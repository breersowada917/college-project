import numpy as np
def random_matrix(n):
    """
    Generate an n x n random matrix filled with 0s.
    
    Parameters:
    - n: An integer representing the size of the matrix
    
    Returns:
    A 2D Numpy array of shape (n, n) containing random numbers between 0 and 1.
    """
    return np.random.rand(n, n)

# Example usage
print(random_matrix(5))
