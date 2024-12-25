# Define the Jacobi method function
# This function takes:
#   A - the coefficient matrix
#   b - the constants vector
#   x0 - the initial guess for the solution
#   iterations - the number of iterations to perform
def jacobi(A, b, x0, iterations):
    # Get the number of equations (length of vector b)
    n = len(b)
    
    # Initialize `x` with the initial guess `x0`
    x = x0[:]
    # Initialize `x_new` as a copy of `x0` to store updated values in each iteration
    x_new = x0[:]
    
    # Perform the specified number of iterations
    for it in range(iterations):
        # Loop over each row in matrix A
        for i in range(n):
            # Initialize `sum_` with the corresponding element in `b`
            # This will be adjusted by subtracting terms from the equation
            sum_ = b[i]
            
            # Iterate over each element in the row to calculate the updated value for x[i]
            for j in range(n):
                # Skip the diagonal element and calculate the sum of other terms
                if i != j:
                    sum_ -= A[i][j] * x[j]
            
            # Update the value of `x_new[i]` based on the Jacobi formula
            x_new[i] = sum_ / A[i][i]
        
        # Update `x` with the values from `x_new` for the next iteration
        x = x_new[:]
    
    # Return the final result after all iterations
    return x

# Coefficients matrix
A = [
    [15, -2, 1, 0, 2],
    [-0.3, 4, -2, 0, 1],
    [6, -1, 6, -2, -1],
    [-1, -2, 1, -7, -2],
    [-3, -1, 1, 0, 15.3]
]

# Constants vector
b = [3, 2, -4, 3, 5]

# Initial guess for the solution
x0 = [0, 1, 0, 1, 0]

# Number of iterations to perform
iterations = 10

# Run the Jacobi method
result_jacobi = jacobi(A, b, x0, iterations)

# Display the final result
print("Jacobi Method Result after 10 iterations:", result_jacobi)
