# Q6. Write a Python function to calculate the cumulative distribution function of a Poisson distribution
# with given mean at a given point.

import math 

def poisson_cdf(x,mean):
    cdf_value = 0.0
    for k in range(x+1):
        cdf_value += (math.exp(-mean) * (mean ** k)) / math.factorial(k)
    
    return cdf_value

x = 4
mean = 3.0

print(poisson_cdf(x,mean))