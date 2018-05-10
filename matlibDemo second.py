
import matplotlib.pyplot as plt
x = [0, 1]
y = [0, 1]
plt.figure()
plt.plot(x, y)
plt.xlabel("time(s)")
plt.ylabel("value(m)")
plt.title("a simple plot")
plt.savefig("easyplot2.png")
print (plt.savefig)


