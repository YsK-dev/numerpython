# Numerical Analysis Methods Implementation

This repository contains implementations of various numerical methods for solving mathematical problems, developed as Numerical Analysis course .

## Overview

The repository includes three main components:

1. **Linear Systems Solver (Homework 1)**
   - Jacobi Iterative Method
   - Gauss-Seidel Method
   - Solution for a 5x5 system of linear equations

2. **Root Finding Methods (Homework 2)**
   - Newton's Method
   - Bisection Method
   - Solutions for nonlinear equations

3. **Numerical Integration (Homework 3)**
   - Composite Simpson's Rule
   - Integration of a specific function over [1,3]



## Problem Specifications

### Homework 1: Linear Systems
- System of 5 equations with coefficient `a=3`
- Implementation of both Jacobi and Gauss-Seidel methods
- Convergence analysis and iteration results

### Homework 2: Root Finding
1. Newton's Method for `e^x + x^2 = 2.33`
   - Interval: [0,1]
   - Convergence criterion: |xₙ₊₁ - xₙ| < 10⁻³
   
2. Bisection Method for `x³ - √3x + 3 = 3`
   - Interval: [1,2]
   - Convergence criterion: |xₙ₊₁ - xₙ| < 10⁻²

### Homework 3: Integration
- Integral: ∫[1 to 3] (x/√(x² + 4.33))dx
- Composite Simpson's Rule implementation
- Results for M = 1 to 8 subintervals

## Common Features

All implementations include:
- Mathematical background and theory
- Python implementation
- Detailed documentation
- Example usage
- Error analysis
- Output formatting
- Convergence criteria


## Usage Examples

### Linear Systems Solver
```python
from hw1_linear_systems import jacobi_solver
result = jacobi_solver(A, b, initial_guess=[0,0,0,0,0], iterations=10)
```

### Root Finding
```python
from hw2_root_finding import newton_method
result = newton_method(0.5, epsilon=1e-3)
```

### Numerical Integration
```python
from hw3_integration import composite_simpson
result = composite_simpson(M=4)  # 8 subintervals
```

## Implementation Notes

1. **Error Handling**
   - Input validation
   - Convergence checks
   - Numerical stability considerations

2. **Performance**
   - Vectorized operations where possible
   - Efficient algorithms
   - Memory optimization

3. **Documentation**
   - Detailed mathematical explanations
   - Step-by-step solutions
   - Clear output formatting



## License

This code is provided for educational purposes. Feel free to use and modify as needed.
