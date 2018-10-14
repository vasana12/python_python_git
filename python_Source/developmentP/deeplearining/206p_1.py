import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib

font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
plt.title('테스트')
plt.plot([1,2,3,4],[2,3,4,5])       #첫번째x축 값 두번째y축 값
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.show()