# Q8. Generate a random sample of size 1000 from a Poisson distribution with mean 5 and calculate the
# sample mean and variance.


# Answer - 
import numpy as np

random_sample = np.random.poisson(5,size=1000)
print(random_sample)

mean = np.mean(random_sample)
print(mean)

variance = np.var(random_sample)
print(variance)