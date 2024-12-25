import math

import math

def bisection_method(a, b, epsilon=1e-2, max_iterations=100):
    """
    Implements the bisection method to find roots of f(x) = x³ - (x + 3)^(1/3) - 3
    with improved error handling and analysis capabilities.
    
    Args:
        a, b: Interval endpoints
        epsilon: Tolerance for convergence
        max_iterations: Maximum number of iterations allowed
    
    Returns:
        tuple: (iterations, solution, error_estimate, all_points)
    """
    def f(x):
        return x**3 - (math.pow(x + 3, 1/3)) - 3
    
    if f(a) * f(b) >= 0:
        raise ValueError("Function must have opposite signs at interval endpoints")
        
    n = 0  # Iteration counter
    all_points = [(a, f(a)), (b, f(b))]  # Store all points for analysis
    
    while n < max_iterations:
        c = (a + b) / 2  # Midpoint
        fc = f(c)
        n += 1
        
        all_points.append((c, fc))
        
        if abs(b - a) < epsilon:  # Convergence criterion
            error_estimate = abs(b - a) / 2
            return n, c, error_estimate, all_points
            
        if fc * f(a) < 0:
            b = c
        else:
            a = c
    
    raise RuntimeError(f"Method failed to converge within {max_iterations} iterations")

# Example usage with analysis
try:
    iterations, solution, error, points = bisection_method(1, 2, epsilon=1e-2)
    
    print(f"Solution Analysis:")
    print(f"{'='*50}")
    print(f"Converged to x = {solution:.6f}")
    print(f"Number of iterations: {iterations}")
    print(f"Estimated error: {error:.6e}")
    print(f"Function value at solution: {points[-1][1]:.6e}")
    
    # Convergence rate analysis
    print(f"\nConvergence Analysis:")
    print(f"{'='*50}")
    print(f"{'Iteration':^10}{'x_n':^15}{'f(x_n)':^15}{'|x_n - x_{n-1}|':^15}")
    print(f"{'-'*55}")
    
    for i in range(len(points)):
        x_n, fx_n = points[i]
        if i > 0:
            diff = abs(x_n - points[i-1][0])
            print(f"{i:^10}{x_n:^15.6f}{fx_n:^15.6e}{diff:^15.6e}")
        else:
            print(f"{i:^10}{x_n:^15.6f}{fx_n:^15.6e}{'N/A':^15}")

except (ValueError, RuntimeError) as e:
    print(f"Error: {e}")