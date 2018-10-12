#https://matplotlib.org/index.html
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(221)  #2행 1열의 1위치
plt.plot([1,2,3,4],[1,2,3,4])
plt.subplot(222)  #2행 1열의 2위치
plt.plot([5,6,7,8],[5,6,7,8])
plt.subplot(223)  #2행 1열의 2위치
plt.plot([9,10,11,12],[9,10,11,12])
plt.subplot(224)  #2행 1열의 2위치
plt.plot([13,14,15,16],[13,14,15,16])
plt.show()
