# Jacobi Iterative Method Solution

This document describes the solution process for a system of linear equations using the Jacobi iterative method. Given that the last digit of my school ID is 3, we set \( a = 3 \) to modify certain coefficients in the equations.

## System of Equations

With \( a = 3 \), the system of equations is defined as follows:
Firstly last digit of myschool id number is 3 so a=3

1. \( 15x_1 - 2x_2 + x_3 + 2x_5 = 3 \)
2. \( 4x_2 - 2x_3 + x_5 = 2 \)
3. \( 6x_1 - x_2 + 6x_3 - 2x_4 - x_5 = -4 \)
4. \( -x_1 - 2x_2 + x_3 - 7x_4 - 2x_5 = 3 \)
5. \( -3x_1 - x_2 + x_3 + 15.3x_5 = 5 \)

### Rearranging the Equations

We can rearrange each equation to isolate each variable on the left side for iterative calculation:

1. \(15x1-2x2+x3​+2x5​=3 \)
2. \(−0⋅3x1+4x2−2x3+x5=2\)
3.  \(6x1−x2+6x3−2x4−x5=−4\)
4.  \(−x1​−2x2​+x3​−7x4​−2x5​=3\)
5.   \(−3x1−x2+x3+15.3x5=5\)


## Iterative Solution

Starting with an initial guess of \( x = [0, 0, 0, 0, 0] \), we perform 10 iterations to approximate the solution. The calculations for each variable in each iteration are shown below:

| Iteration | \( x_1 \)     | \( x_2 \)     | \( x_3 \)     | \( x_4 \)     | \( x_5 \)     |
|-----------|---------------|---------------|---------------|---------------|---------------|
| 0         | 0.2           | 0.5           | -0.6667       | -0.4286       | 0.3268        |
| 1         | 0.17          | 0.41          | -0.01         | 0.43          | 0.07          |
| 2         | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |
| 3         | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |
| 4         | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |
| 5         | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |
| 6         | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |
| 7         | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |
| 8         | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |
| 9         | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |
| 10        | 0.19          | 0.43          | -0.03         | 0.49          | 0.08          |

> Calculations were performed using a calculator.
## code section 
I used both numpy and raw python to compare and better understand
# Gauss-Seidel Method Implementation

This repository contains Python implementations of the Gauss-Seidel method for solving systems of linear equations. Two versions are provided: a pure Python implementation and a version using the NumPy library.

## Description

The Gauss-Seidel method is an iterative technique used to find approximate solutions to linear systems of equations of the form \(Ax = b\), where:

- \(A\) is the coefficient matrix.
- \(b\) is the constants vector.
- \(x\) is the solution vector.

### Pure Python Implementation

- The function `seidel(a, x, b)` performs one iteration of the Gauss-Seidel method using nested loops.
- It updates the solution vector `x` iteratively over a fixed number of iterations (25 by default).



## Conclusion

After 10 iterations, the approximate solution to the system is:

\[
x \approx [0.19, 0.43, -0.03, 0.49, 0.08]
\]

This solution demonstrates convergence of the Jacobi method over successive iterations.
**Example Usage:**
```python
x = [0, 1, 0, 1, 0]  # Initial guess
a = [[15, -2, 1, 0, 2], [-0.3, 4, -2, 0, 1], [6, -1, 6, -2, -1], [-1, -2, 1, -7, -2], [-3, -1, 1, 0, 15.3]]
b = [3, 2, -4, 3, 5]

for i in range(25):
    x = seidel(a, x, b)
    print(f"Iteration {i + 1}: {x}")


