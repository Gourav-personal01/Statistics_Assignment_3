# Q5. Generate a random sample of size 1000 from a binomial distribution with probability of success 0.4
# and plot a histogram of the results using matplotlib.

# Answer - 
import numpy as np
import matplotlib.pyplot as plt

sample_size = 1000
success_pr = 0.4
random_sample = np.random.binomial(1, success_pr, sample_size)
print(random_sample)

print(plt.hist(random_sample))