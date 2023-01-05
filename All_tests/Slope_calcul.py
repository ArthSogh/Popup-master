import numpy as np
import matplotlib.pyplot as plt
import random

number_elements = 100 #Number of last values to display

values = [(i, i*2.5 + random.uniform(0, 1)) for i in range(5)]

print(values)
print(*values)
print(list(zip(*values)))
# print(values[-number_elements:])
# print([e[0] for e in values[-number_elements:]])
# print([e[1] for e in values[-number_elements:]])

slope, _ = np.polyfit(list(zip(*values))[0], list(zip(*values))[1], 1) # '_' help intercepting non wanted values
#slope, _ = np.polyfit([e[0] for e in values[-number_elements:]], [e[1] for e in values[-number_elements:]], 1) # '_' help intercepting non wanted values

#frame
plt.grid()
plt.plot(list(zip(*values))[0], list(zip(*values))[1], color='green', label=f" Slope : " + str(slope))
#plt.plot(time, weight, color='green', label=f" Slope : {slope:0.3)}")
plt.legend()
plt.show()

