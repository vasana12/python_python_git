import pandas as pd
from sklearn import model_selection, svm, metrics
from sklearn.model_selection import GridSearchCV

# MNIST 학습 데이터 읽어 들이기
train_csv = pd.read_csv('./mnist/train.csv')
test_csv = pd.read_csv('./mnist/t10k.csv')

# 필요한 열 추가하기
train_label = train_csv.ix[:, 0]
train_data = train_csv.ix[:, 1:785]
test_label = test_csv.ix[:, 0]
test_data = test_csv.ix[:, 1:785]
print('학습 데이터의 수 = ', len(train_label))

# 그리드 서치 매개변수 설정
# C : 얼마나 많은 데이터 샘플이 다른 클래스에 놓이는 것을 허용하는지를 결정
# C값을 낮게 설정하면 이상치들이 있을 가능성을 크게 잡아 일반적인 결정 경계를 찾아내고,
# 높게 설정하면 반대로 이상치의 존재 가능성을 작게 봐서 좀 더 세심하게 결정 경계를 찾아낸다.
# gamma : 하나의 데이터 샘플이 영향력을 행사하는 거리를 결정
# gamma가 클수록 한 데이터 포인터들이 영향력을 행사하는 거리가 짧아지는 반면,
# gamma가 낮을수록 커진다.

params = [{"C":[1,10,100,1000], "kernel":['linear']},
          {"C":[1,10,100,1000], 'kernel':['rbf'], 'gamma':[0.001, 0.0001]}
          ]

# 그리드 서치 수행
clf = GridSearchCV(svm.SVC(), params, n_jobs=1)
clf.fit(train_data, train_label)
print('학습기 = ', clf.best_estimator_)

pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(pre, test_label)
print('정답률 = ', ac_score)