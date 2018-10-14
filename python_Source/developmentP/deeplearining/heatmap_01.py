import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

uniform_data = np.random.rand(10,12)
print(uniform_data)
sns.heatmap(uniform_data, cbar=True, vmin=0, vmax=1)
plt.show()


flights = sns.load_dataset("flights")
print(flights.head())
#pivot() = > index : month, column : year, value : passengers
flights = flights.pivot("month", "year", "passengers")
print(flights.head(5))

plt.figure(figsize=(10,8))
#flights : 데이터, annpt=True : 값 출략, fmt="d" :값을 정수형으로 출력
#linewidths =.5 : 줄간격, cbar= True : 색상바 출력(기본), cbar_kws : cbar 위치
sns.heatmap(flights, annot=True, fmt="d", vmin=0, vmax=650, linewidths=.5,\
            cbar=True, cbar_kws={"orientation": "horizontal"}, cmap="Reds")
plt.show()
