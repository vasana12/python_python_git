#https://matplotlib.org/index.html
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x = range(0,100)
y = [v*v for v in x]

ax1.plot(x,y,'ro')
ax2.bar(x,y) #막대그래프

plt.show()