import numpy as np
import matplotlib.pyplot as plt

def read_settings(file_name):
    with open(file_name, 'r') as set_f:
        return [float(i) for i in set_f.read().split('\n')]
    
freq, disc = read_settings("settings.txt")

data = np.loadtxt("data.txt", dtype = float)
data *= disc 
times = np.arange(len(data)) * freq

fig, ax = plt.subplots(figsize = (16,10), dpi = 300)

ax.set_xlim(0, 1.1 * max(times))
ax.set_ylim(0, 1.1 * max(data))

stp = 256
ax.plot(times, data)
ax.plot(times[::stp], data[::stp], 'bo')
fig.savefig("test.png")

