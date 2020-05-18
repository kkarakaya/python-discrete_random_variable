import random
import numpy as np
from scipy.stats import rv_discrete 
import matplotlib.pyplot as plt

def frequencies(data, edges):
    # This function calculates frequencies of elements in dataset for given edges

    realEdges = edges + [float("inf")]
    intervalFrequencies  =[]
    for i in range(0,len(realEdges)-1):
        intervalFrequencies.append(sum([1 for k in data if realEdges[i]<= k < realEdges[i+1]]))
    return intervalFrequencies

def probabilities(frequencies):
    # This function calculates probabilities of elements in dataset

    dataCount = sum(frequencies)
    probs = [f/dataCount for f in frequencies]
    return probs

# Generate sleep data
mean = 6
var = 9
sleepHours = [random.gauss(mean,np.sqrt(var)) for x in range(1000)]

# Generate random variable from sleep data
edges = [0,3,6,9]       # X < 3 , 3 <= X < 6 , 6 <= X < 9 , 9 < X
freqs = frequencies(sleepHours, edges)
probs = probabilities(freqs)
X = rv_discrete(values=(range(len(edges)), probs))  # Create random variable

# Plot probability distribution ( in this case it is pmf because X is discrete)
fig, ax = plt.subplots(1, 1)
ax.plot(range(0,len(edges)), X.pmf(range(0,len(edges))), 'ro', ms=12, mec='r')
ax.vlines(range(0,len(edges)), 0, X.pmf(range(0,len(edges))), colors='r', lw=3)
ax.set(title= "PMF of Random Variable X for Given Intervals", xlabel='Intervals (hours)', ylabel='Probability')
ax.set(xticks = [0,1,2,3], xticklabels = ["< 3", "3 - 6", "6 - 9", "> 9"])

plt.show()

print("Mean of X: " , np.mean(sleepHours))
print("Variance of X: " , np.var(sleepHours))
