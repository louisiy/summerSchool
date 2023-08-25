import numpy as np
from scipy.optimize import least_squares  as lstsq

# 定义真实函数
def fun(x,para):
    [a,b,c] = para
    return a + b*x + c*x**2
# 定义残差
def residuals(para,ys,xs):
    return ys - fun(xs,para)

# 定义实验数据
xs = np.linspace(0,5,100)+np.random.normal(0,0.2,100)
ys = fun(xs,[1,-2,1])+np.random.normal(0,0.2,100)

# 定义初始参数
para0=[1,1,1]
# 最小二乘获得解
solve = lstsq(residuals, para0, args=(ys, xs))
#print(solve.x)

# 调用图包
import matplotlib.pylab as plt
import pylab as pl
X = xs
Y0 = ys
Y1 = fun(xs,solve.x)
# 绘制
pl.scatter(X,Y0,s=10,c='#029386')
plt.plot(X,Y1,color = '#EF4026',linewidth='2.0')
plt.show()