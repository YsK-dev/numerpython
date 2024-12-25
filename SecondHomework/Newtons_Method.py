import math

def newton_method(x0, epsilon=1e-3):
    xn = x0
    n = 0
    
    print("Iteration sequence:")
    print(f"x{n} = {xn:.6f}")
    
    while True:
        # Calculate f(x) and f'(x)
        fx = math.exp(xn) + xn**2 - 2.33
        fpx = math.exp(xn) + 2*xn
        
        # Newton's iteration
        xn_next = xn - fx/fpx
        
        n += 1
        print(f"x{n} = {xn_next:.6f}")
        
        # Check convergence
        if abs(xn_next - xn) < epsilon:
            break
            
        xn = xn_next
    
    return n, xn_next

# Run the method with x0 = 0.5
iterations, solution = newton_method(0.5)
print(f"\nConverged after {iterations} iterations")
print(f"Final solution: {solution:.6f}")
