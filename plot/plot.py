import numpy as np
import matplotlib.pyplot as plt

def read_settings(file_name):
    with open(file_name, 'r') as set_f:
        return [float(i) for i in set_f.read().split('\n')]
    
freq, disc = read_settings("settings.txt")

data = np.loadtxt("data.txt", dtype = float)
data *= disc 
times = np.arange(len(data)) * freq

fig, ax = plt.subplots(figsize = (16,10), dpi = 200)

ax.set_xlim(0, 1.1 * max(times))
ax.set_ylim(0, 1.1 * max(data))

ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")
plt.title("Процесс заряда-разряда", wrap = True)

ax.minorticks_on()
ax.grid(True)
ax.grid(True, 'minor', ls=':')

plt.text(0.8 * max(times), 0.7 * max(data), 
         f"Время заряда: {data.argmax() * freq :.2f} с \n\nВремя разряда: {max(times) - data.argmax() * freq :.2f} с", 
         size = 'xx-large', wrap = True)

stp = 256
ax.plot(times, data, color = 'm', alpha = 0.5, label = "V(t)")
ax.plot(times[::stp], data[::stp], 'bo')
plt.legend(fontsize = 'x-large')

fig.savefig("test.png")
fig.savefig("test.svg")

