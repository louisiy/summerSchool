import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# 读取文件
# 由于编码原因，已将原始提供的文件里的中文转写为英文来方便读取
df = pd.read_csv('car.csv')
# print(df.to_string())

# 提取数据
xs = df.iloc[:,0]
ys = df.iloc[:,1]
#print(xs)
#print(ys)

# 插值
interp_fun = interp1d(xs,ys)
newArr = interp_fun(np.arange(0,1440,1))
#print(newArr)

# 梯形积分计算并在控制台打印
sum = 0
for i in range(1438):
    sum += (newArr[i]+newArr[i+1])/2
sum += (newArr[1439]+3)/2
print(sum)

# 引入图包
import matplotlib.pylab as plt
import pylab as pl

# 绘制
X = np.arange(1440)
Y = newArr
plt.plot(X,Y,linewidth='2.0')
plt.show()
