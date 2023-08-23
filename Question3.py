# Q3. Write a Python function to calculate the probability density function of a normal distribution with
# given mean and standard deviation at a given point.

# Answer - 
import math

def calculate_pdf(x,mean,std):
    coefficient = 1/(std * math.sqrt(2*math.pi))
    exponent = -((x - mean)**2) / (2 * std**2)
    pdf_value = coefficient * math.exp(exponent)
    return pdf_value

x = 2
mean = 2
std = 2

print(calculate_pdf(2,2,2))