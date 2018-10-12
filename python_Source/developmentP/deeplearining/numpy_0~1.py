#https://matplotlib.org/index.html
import matplotlib.pyplot as plt
import numpy as np

# 0.0~1.0 사이의 실수의 범위는 numpy 모듈의 arange() 함수 사용
print('np.pi=',np.pi)
x = np.arange(0.0, 2*np.pi, 0.1)
print('x=',x)
sin_y = np.sin(x)
cos_y = np.cos(x)

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(x, sin_y, 'b--')
ax2.plot(x, cos_y, 'r--')

plt.show()
