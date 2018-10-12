import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib

font_location = "C:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

labels = '개구리', '돼지', '개', '통나무'
sizes = [15, 30, 40, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode = explode, labels=labels, colors=colors,
        autopct='%2.2f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()