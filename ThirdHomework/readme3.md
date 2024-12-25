# Composite Simpson's Rule Implementation

This repository contains a Python implementation of the Composite Simpson's rule for numerical integration. The implementation specifically solves the definite integral:

∫[1 to 3] (x/√(x² + 4.33))dx

## Mathematical Background

### Composite Simpson's Rule
The Composite Simpson's rule approximates a definite integral by dividing the interval into 2M subintervals and using quadratic approximations. The formula is:

```
S_2M = (h/3)[f(x₀) + 4Σ(i=1,3,...,2M-1)f(x_i) + 2Σ(i=2,4,...,2M-2)f(x_i) + f(x_{2M})]
```

where:
- h = (b-a)/(2M) is the step size
- x_i = a + ih are the nodes
- f(x) is the integrand function

### Exact Solution
The exact value of the integral is calculated using the substitution method:
- Let u = x² + 4.33
- Then du = 2x dx
- The integral becomes: (1/2)∫[5.33,13.33] du/√u
- Solution: √13.33 - √5.33 ≈ 1.3989

## Implementation

### Function Descriptions

#### `f(x)`
The integrand function.
```python
def f(x):
    return x / math.sqrt(x**2 + 4.33)
```

#### `composite_simpson(M)`
Implements the Composite Simpson's rule.
- Parameters:
  - `M`: Number of pairs of subintervals (total subintervals = 2M)
- Returns:
  - Approximate value of the integral

### Usage

```python
from composite_simpson import composite_simpson

# Calculate approximation with 2M subintervals
result = composite_simpson(4)  # Uses 8 subintervals
```

## Output Format

The program prints results in the format:
```
Composite Simpson's Rule Results:
--------------------------------
M = 1, Sk = [value]
M = 2, Sk = [value]
...
M = 8, Sk = [value]

Exact value = [value]
```


## Implementation Notes

1. The code uses vectorized operations for efficiency
2. Handles both odd and even indices separately according to Simpson's rule
3. Includes the exact value for comparison

## Limitations and Assumptions

1. Assumes the integrand is continuous and well-behaved
2. No error handling for invalid input values
3. Fixed integration limits [1,3]
4. No handling of improper integrals

