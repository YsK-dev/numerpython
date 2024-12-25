
# Define the function `seidel` which performs one iteration of the Gauss-Seidel method
# It takes 3 arguments:
#   `a` - the coefficient matrix
#   `x` - the current solution vector (initial guess or updated values)
#   `b` - the constants vector in the equation Ax = b
def seidel(a, x, b):
    # Determine the size of the matrix `a` (in this case, 5x5)
    n = len(a)
    
    # Iterate over each row in `a` to update the corresponding element in `x`
    for j in range(0, n):
        # Initialize `d` with the corresponding element in `b`
        # This will be modified by subtracting values based on the equation
        d = b[j]
        
        # Iterate over each column in the row to calculate the updated value
        # for the `j`-th variable (x[j])
        for i in range(0, n):
            # If we're not on the main diagonal element (i.e., j != i),
            # subtract `a[j][i] * x[i]` from `d` to isolate `x[j]`
            if j != i:
                d -= a[j][i] * x[i]
        
        # Update the value of `x[j]` by dividing `d` by the diagonal element `a[j][j]`
        x[j] = d / a[j][j]
    
    # Return the updated solution vector `x`
    return x 

# Define the number of variables in the system of equations
n = 5

# Initialize coefficient matrix `a`, constants vector `b`, and initial solution `x`
# normally as a sawe on the internet first value is 0 bu you asked for  x
# (0) = [0 1 0 1 0]T			 
x = [0, 1, 0, 1, 0]					 
a = [
    [15, -2, 1, 0, 2],
    [-0.3, 4, -2, 0, 1],
    [6, -1, 6, -2, -1],
    [-1, -2, 1, -7, -2],
    [-3, -1, 1, 0, 15.3]
]

b = [3, 2, -4, 3, 5]

# Display the initial guess for the solution vector
print("Initial solution:", x)

# Perform the iteration for a fixed number of times (25 in this case) I tried until  25 
# This loop can be stopped earlier if convergence criteria are met
for i in range(0, 25):
    # Call the `seidel` function to update `x` based on the previous values
    x = seidel(a, x, b)
    
    # Print the updated solution after each iteration
    print(f"Iteration {i + 1}: {x}")


#nupmy version i did it then I thought raw python is better

'''
import numpy as np

# Define the Gauss-Seidel method
def gauss_seidel(A, b, x0, iterations):
    n = len(b)
    x = np.copy(x0)
    
    for it in range(iterations):
        for i in range(n):
            sum_ = b[i]
            for j in range(n):
                if i != j:
                    sum_ -= A[i][j] * x[j]
            x[i] = sum_ / A[i][i]
    return x

# Coefficients matrix
A = np.array([
    [15, -2, 1, 0, 2],
    [0, 4, -2, 0, 1],
    [6, -1, 6, -2, -1],
    [-1, -2, 1, -7, -2],
    [-3, -1, 1, 0, 6.5]
])

# Constants vector
b = np.array([3, 2, -4, 3, 5])

# Initial guess
x0 = np.array([0, 1, 0, 1, 0])

# Number of iterations
iterations = 10

# Run Gauss-Seidel
result = gauss_seidel(A, b, x0, iterations)
print("Gauss-Seidel Method Result after 10 iterations:", result)

this solution is with numpy firstly it was more easy to do it with numpy but this below solution was better I think


'''


