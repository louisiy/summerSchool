import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

# 加载处理好的数据
data = np.load('./data/data.npz')
X = data['X']
Y = data['Y'].ravel()

# 标准化
std = StandardScaler()
X_std = std.fit_transform(X)

# 拆分训练集
X_train, X_test, Y_train, Y_test = train_test_split(X_std,Y,test_size=0.3)

# 建模
svm_regression = SVR(kernel='rbf', C=100.0, gamma='auto')
#svm_regression.fit(X_train,Y_train)

# 模型效果
#print(svm_regression.score(X_test,Y_test))

param_grid = {
    'C': [0.1, 1, 10,100],
    'kernel': ['linear', 'rbf'],
    'gamma': [0.1, 1, 10]
}
grid_search = GridSearchCV(svm_regression, param_grid, cv=5)
grid_search.fit(X_std, Y)

print("Best parameters: ", grid_search.best_params_)
print("Best score: ", grid_search.best_score_)