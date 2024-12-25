import math

def bisection_method(a, b, epsilon=1e-2):
    n = 0  # Iteration counter
    
    print("Iteration sequence:")
    print(f"x{n} = {a:.6f}")
    
    while True:
        c = (a + b) / 2  # Midpoint
        n += 1
        print(f"x{n} = {c:.6f}")
        
        # Calculate function values
        fc = c**3 - (math.pow(c + 3, 1/3)) - 3
        fa = a**3 - (math.pow(a + 3, 1/3)) - 3
        
        if abs(b - a) < epsilon:  # Convergence criterion
            break
            
        # Check the sign of the product to determine the next interval
        if fc * fa < 0:
            b = c
        else:
            a = c
    
    return n, c

# Run the method with interval [1,2]
iterations, solution = bisection_method(1, 2)
print(f"\nConverged after {iterations} iterations")
print(f"Final solution: {solution:.6f}")
