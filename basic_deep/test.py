import random
import numpy as np
import matplotlib.pyplot as plt
from comm_func import mean_squared_error, cross_entory_error 


t = [0, 0, 1, 0, 0]
n = 1
mss = []
cee = []
my_range = np.arange(0.01, 0.9, 0.001)
for i in my_range:
    n = n + 1
    if n < 300:
        n_range = 0.8
    elif n < 400:
        n_range = 0.7
    elif n < 500:
        n_range = 0.6
    elif n < 600:
        n_range = 0.5
    elif n < 700:
        n_range = 0.4
    elif n < 800:
        n_range = 0.3
    
    y = [ random.uniform(0.1, n_range), random.uniform(0.1, n_range), i, random.uniform(0.1, n_range), random.uniform(0.1, n_range)]
    mss.append(mean_squared_error(np.array(y), np.array(t)))
    cee.append(cross_entory_error(np.array(y), np.array(t)))

#print(mss)
#print(cee) 

plt.figure()
plt.plot(my_range, mss)
plt.plot(my_range, cee)
plt.show()