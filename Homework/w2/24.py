from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

# 设置图像为3D
fig = plt.figure()
ax = Axes3D(fig)
fig.add_axes(ax)

# 定义X、Y坐标
x = np.arange(-6,6,0.1)
y = np.arange(-6,6,0.1)
x,y = np.meshgrid(x,y)

# 定义该二元函数
def eqn(para):
    x,y = para
    return (x**2+y-11)**2+(x+y**2-7)**2

z = eqn([x,y])
#print(z)

# 优化查找极小值，并打印其与坐标
ohMin = minimize(eqn,[0,0],method='Nelder-Mead')
print(eqn(ohMin.x))
print(ohMin.x)

# 绘制
ax.plot_surface(x,y,z,cmap = 'rainbow')
plt.show()