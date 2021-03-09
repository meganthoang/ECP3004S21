#!/usr/bin/python
"""
##################################################
# 
# ECP 3004: Python for Business Analytics
# 
# Solving Equations with Scipy
# 
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
# 
# March 9, 2021
# 
# This program provides introductory examples of 
# numerical methods for finding roots of single equations
# and solving systems of equations.
# 
##################################################
"""


##################################################
# Import Modules.
##################################################


import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import optimize
# from scipy.optimize import minimize
# from scipy.optimize import Bounds
# from scipy.optimize import LinearConstraint

##################################################
# Solving for Roots of Equations
##################################################

#--------------------------------------------------
### The problem
#--------------------------------------------------

# When finding the *root of a non-linear function*, 
# the goal is to find a parameter input that returns 
# a value of zero from that function. 
# It is common notation to refer to the parameter as ```x``` 
# and the function as ```f(x)``` or to solve for ```x``` 
# such that ```f(x) = 0```. 
# The parameter ```x``` can be a vector 
# and there can be multiple solutions, depending on the function. 
# The quadratic formula is the closed-form solution
# to the problem of finding a root of ```f(x, a, b, c) = a*x**2 + b*x + c == 0```.
# Solving a system of linear equations 
# is also a root-finding problem: 
# it solves for the root ```x``` of ```f(x) = A.dot(x) - b == 0```. 
# There is one more element of complexity when the function is nonlinear. 

#--------------------------------------------------
### The solution
#--------------------------------------------------

# There are several algorithms for finding the root of a function 
# and the following selection illustrates the nature of the solution and the type of situation in which it applies. 

#--------------------------------------------------
#### Grid Search
#--------------------------------------------------

# While not favored in terms of computational expense, 
# one approach is to calculate a vector of values. 


# Define function.
def quad_fn(x, a, b, c):
    # Note that this calculation also operates on vectors. 
    f = a*x**2 + b*x + c
    return(f)

a = 1/4
b = 1 
c = -1

# Calculate function values across a grid of values of x.
x_grid = np.arange(-10, 5, 0.01)
f_grid = quad_fn(x_grid, a, b, c)


# It is often very helpful to plot the function to get an idea of where the root might be located.


plt.figure()
plt.plot(x_grid, f_grid, label='f(x)' )
plt.plot(x_grid, 0*f_grid)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()


# From the plot, we can see that there are two roots, one near -5 and the other near 1 and two. 
# We can select the value of ```x``` such that the absolute value of ```f(x)``` is minimized, using the ```which.min()``` and ```abs()``` functions in ```R```. 



# The closest to zero has the lowest abosolute value.

# The argmin() numpy method finds the index number of the minimal value.
abs_f_grid = abs(f_grid)
x_root_index = abs_f_grid.argmin()
x_root_1 = x_grid[x_root_index]

print(x_root_1)

# Verify that this is actually a root.
print(quad_fn(x_root_1, a, b, c))


# Do it again with a higher resolution.
x_grid = np.arange(0, 1, 0.0001)
f_grid = quad_fn(x_grid, a, b, c)

# All in one line:
x_root_2 = x_grid[abs(f_grid).argmin()]

print(x_root_2)
print(quad_fn(x_root_2, a, b, c))


    

# This approach is fairly foolproof but it is limited in scope because it is 
# computationally expensive to evaluate the function at all candidate values
# and the accuracy is limited by the step size between grid points. 
# Other approaches are designed to take fewer steps to approach roots using information from more than one point at a time. 






################################################################################
# Solving Nonlinear equations with Python Modules
################################################################################

#--------------------------------------------------
# Single variable equations
#--------------------------------------------------

# Goal: Find the root of this function.
def f(x):
    out_value = math.log(x) - math.exp(-x)
    print("(x, f(x)) = (%f, %f)" % (x, out_value))
    return out_value
# That is, find the x at which this function is zero.

# Note that this function unnecessarily prints
# the value of x and f(x) to demonstrate the progress. 

# Plot this function to show an approximate root.
x_grid = np.arange(0.1, 2, 0.01)
f_grid = x_grid*0
for i in range(0, len(x_grid)):
    f_grid[i] = f(x_grid[i])


plt.figure()
plt.plot(x_grid, f_grid, label='f(x)' )
plt.plot(x_grid, 0*f_grid)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()


# This is a "legacy solution", in that 
# it uses a function definition fslove()
# that is no longer in use.
soln_fs = fsolve(f, 1)
# The root:
print(soln_fs)
# The objective function:
print(f(soln_fs))


# Other legacy functions:

# soln_b1 = broyden1(f, 1)
# soln_b1 = broyden2(f, 1)
# soln_b1 = anderson(f, 1)

# These are named after the mathematicians
# and computer scientists who devised the algorithms. 
# Modern Python functions no longer have these names
# but they may call the algorithms with these names.

#--------------------------------------------------
# Multiple variable equations
#--------------------------------------------------

# Nonlinear equations, 2 equations, 2 parameters.


def my_eqns_22(x):
    F1 = x[0]**2+ x[1]**2 - 1 
    F2 = x[0]**2- x[1]**2 + 0.5
    return [F1, F2]

# Test it for a few inputs (potential starting values).
my_eqns_22([1, 1])

my_eqns_22([1, 2])

# Start at a sensible value (closer to zero already).
x0 = [1, 1]

soln_m_22 = optimize.root(my_eqns_22, x0)



# The root:
print(soln_m_22.x)
# The objective function:
print(soln_m_22.fun)
print(my_eqns_22(soln_m_22.x))


# Nonlinear equations, 3 equations, 2 parameters.


def my_eqns_32(x):
    F1 = x[0] + x[1] + x[2]**2 - 12
    F2 = x[0]**2 - x[1] + x[2] - 2
    F3 = 2 * x[0] - x[1]**2 + x[2] - 1
    return [F1, F2, F3]



# Test it for a few inputs (potential starting values).
my_eqns_32([1, 1, 1])

my_eqns_32([0, 0, 0])

x0 = [1, 1, 1]

soln_m32_1 = optimize.root(my_eqns_32, x0)


# The root:
print(soln_m32_1.x)
# The objective function:
print(soln_m32_1.fun)
print(my_eqns_32(soln_m32_1.x))


# Try the other starting value, just to compare.
x0 = [0, 0, 0]

soln_m32_2 = optimize.root(my_eqns_32, x0)

# The root:
print(soln_m32_2.x)
# The objective function:
print(soln_m32_2.fun)
print(my_eqns_32(soln_m32_2.x))


#--------------------------------------------------
# Passing additional parameters. 
#--------------------------------------------------

# Some systems of equations depend on other fixed parameters. 

def my_eqns_33_p(x, parms):
    F1 = x[0] + x[1] + x[2]**2 - parms[0]
    F2 = x[0]**2 - x[1] + x[2] - parms[1]
    F3 = 2 * x[0] - x[1]**2 + x[2] - parms[2]
    return [F1, F2, F3]

# You can solve for these as above, 
# except that you pass the extra parameters to optimize,root(). 

# Set parameters and choose starting values.
parms = [12, 2, 1]
my_eqns_33_p([1, 1, 1], parms)
x0 = [1, 1, 1]


# Solve
soln_m33_p = optimize.root(my_eqns_33_p, x0, parms)

# The root:
print(soln_m33_p.x)
# The objective function:
print(soln_m33_p.fun)
print(my_eqns_33_p(soln_m33_p.x, parms))


# Try other parameters and starting value.
parms = [24, 4, 2]
x0 = [0, 0, 0]
my_eqns_33_p(x0, parms)

# Solve
soln_m33_p = optimize.root(my_eqns_33_p, x0, parms)

# The root:
print(soln_m33_p.x)
# The objective function:
print(soln_m33_p.fun)
print(my_eqns_33_p(soln_m33_p.x, parms))


# Test these values:
x0 = [-0.6406658, 1.2471383, 4.8366856]
my_eqns_33_p(x0, parms)
# Another solution. 

# Solve to higher degree of precision.
soln_m33_p = optimize.root(my_eqns_33_p, x0, parms)

# The root:
print(soln_m33_p.x)
# The objective function:
print(soln_m33_p.fun)
print(my_eqns_33_p(soln_m33_p.x, parms))


##################################################
# End
##################################################
