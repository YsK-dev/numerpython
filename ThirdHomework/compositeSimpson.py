import math

def f(x):
    """The integrand function x/sqrt(x^2 + 4.33)"""
    return x / math.sqrt(x**2 + 4.33)

def composite_simpson(M):
    """
    Compute integral using Composite Simpson's rule with 2M subintervals
    """
    a, b = 1, 3  # integration limits
    h = (b - a) / (2 * M)  # step size
    
    # Initialize sum with endpoint values
    result = f(a) + f(b)
    
    # Add odd-indexed terms (multiplied by 4)
    for i in range(1, 2*M, 2):
        x = a + i*h
        result += 4 * f(x)
    
    # Add even-indexed terms (multiplied by 2)
    for i in range(2, 2*M-1, 2):
        x = a + i*h
        result += 2 * f(x)
    
    return (h/3) * result

# Compute and print results for M = 1 to 8
print("Composite Simpson's Rule Results:")
print("--------------------------------")
for M in range(1, 9):
    Sk = composite_simpson(M)
    print(f"M = {M}, Sk = {Sk:.10f}")

# Print exact value for comparison
exact_value = math.sqrt(13.33) - math.sqrt(5.33)
print("\nExact value =", f"{exact_value:.10f}")