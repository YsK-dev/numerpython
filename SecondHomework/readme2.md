# Numerical Methods Implementation

This repo is for Nümerical analysis homework 2 and explanation of code and mathematic

## Problem Descriptions

### Problem 1: Newton's Method
Solves the nonlinear equation: e^x + x^2 = 2.33

The implementation:
- Shows that a unique solution exists on the interval [0, 1]
- Implements Newton's iteration sequence
- Computes iterations until |xₙ₊₁ - xₙ| < 10⁻³
- Uses initial value x₀ = 0.5

### Problem 2: Bisection Method
Solves the nonlinear equation: x³ - √3x + 3 = 3

The implementation:
- Shows that a unique solution exists on the interval [1, 2]
- Implements the Bisection method
- Computes iterations until |xₙ₊₁ - xₙ| < 10⁻²



## Usage

### Newton's Method
```python
from newton_method import newton_method

# Run with default epsilon = 1e-3
iterations, solution = newton_method(0.5)

# Or specify custom epsilon
iterations, solution = newton_method(0.5, epsilon=1e-4)
```

### Bisection Method
```python
from bisection_method import bisection_method

# Run with default epsilon = 1e-2
iterations, solution = bisection_method(1, 2)

# Or specify custom epsilon
iterations, solution = bisection_method(1, 2, epsilon=1e-3)
```

## Function Parameters

### Newton's Method
- `x0`: Initial guess (float)
- `epsilon`: Convergence criterion (float, default=1e-3)

Returns:
- `iterations`: Number of iterations needed (int)
- `solution`: Final solution (float)

### Bisection Method
- `a`: Left endpoint of interval (float)
- `b`: Right endpoint of interval (float)
- `epsilon`: Convergence criterion (float, default=1e-2)

Returns:
- `iterations`: Number of iterations needed (int)
- `solution`: Final solution (float)



## Mathematical Background

### Newton's Method
Newton's method uses the iterative formula:
xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)

Where for Problem 1:
- f(x) = e^x + x² - 2.33
- f'(x) = e^x + 2x

### Bisection Method
The Bisection method repeatedly divides an interval containing the solution, selecting the subinterval where the function changes sign.

For Problem 2:
- f(x) = x³ - √3x - 0
- Initial interval: [1, 2]
