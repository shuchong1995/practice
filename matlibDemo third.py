import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,1000)
y = np.sin(x)
plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.legend("sinx")
plt.title("sinx figure")
plt.savefig("sinx.png")
print (plt.savefig)