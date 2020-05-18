import random
from scipy.stats import rv_discrete 
import matplotlib.pyplot as plt

def frequencies(data):
    # This function calculates frequencies of elements in dataset

    freq = [data.count(x) for x in set(data)]
    return freq

def probabilities(frequencies):
    # This function calculates probabilities of elements in dataset

    dataCount = sum(frequencies)
    probs = [f/dataCount for f in frequencies]
    return probs

# Generate sleep data
sleepHours = [random.gauss(6,3) for x in range(1000)]

# Generate random variable from sleep data
freqs = frequencies(sleepHours)
probs = probabilities(freqs)
X = rv_discrete(values=(sleepHours, probs))  # Create random variable

# Probabilities of given intervals
probIntervals = [X.cdf(3), X.cdf(6) - X.cdf(3), X.cdf(9) - X.cdf(6), 1-X.cdf(9)]
# Plot probability distribution ( in this case it is pmf because X is discrete)
fig, ax = plt.subplots(1, 1)
ax.bar(range(0,len(probIntervals)),probIntervals)
ax.set(title= "PMF of Random Variable X for Given Intervals", xlabel='Intervals (hours)', ylabel='Probability')
ax.set(xticks = [0,1,2,3], xticklabels = ["< 3", "3 - 6", "6 - 9", "> 9"])
plt.show()

print("Mean of X: " , X.mean())
print("Variance of X: " , X.var())
