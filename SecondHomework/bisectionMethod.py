import math

def bisection_method(a, b, epsilon=1e-2):
    n = 0
    
    print("Iteration sequence:")
    print(f"x{n} = {a:.6f}")
    
    while True:
        c = (a + b)/2
        n += 1
        print(f"x{n} = {c:.6f}")
        
        # Calculate function values
        fc = c**3 - math.sqrt(3)*c - 0
        fa = a**3 - math.sqrt(3)*a - 0
        
        if abs(b - a) < epsilon:
            break
            
        if fc*fa < 0:
            b = c
        else:
            a = c
    
    return n, c

# Run the method with interval [1,2]
iterations, solution = bisection_method(1, 2)
print(f"\nConverged after {iterations} iterations")
print(f"Final solution: {solution:.6f}")