import numpy as np
import pandas as pd
import ase.io
from ase.io import extxyz

import os


posList = []
energies = []

# 读取system.txt,由于读取缺少第一行而加了一行标签：id,energy
df = pd.read_csv("./data/system.txt",delimiter=',')
initialEnergy = df.iloc[:,1]
#print(initialEnergy)
# 读取已由uncompress.py解压过的文件
dataDir = './data/H'
files = os.listdir(dataDir)
count = 0





dataPath = os.path.join(dataDir,'random207.extxyz')
traj = ase.io.read(dataPath, index = ":")
initial = traj[0]
stable = traj[-1]
# 获取每种晶体的特征
#print(initial.get_positions())
matrix = initial.get_positions().flatten()
posList.append(np.concatenate((matrix[-3:], matrix[:-3])))
# 获得每种晶体的吸附能
relaxed_energy = stable.get_potential_energy()
energies.append(relaxed_energy - initialEnergy[0])
#print(count)




dataPath = os.path.join(dataDir,'random416.extxyz')
traj = ase.io.read(dataPath, index = ":")
initial = traj[0]
stable = traj[-1]
# 获取每种晶体的特征
#print(initial.get_positions())
matrix = initial.get_positions().flatten()
posList.append(np.concatenate((matrix[-3:], matrix[:-3])))
# 获得每种晶体的吸附能
relaxed_energy = stable.get_potential_energy()
energies.append(relaxed_energy - initialEnergy[1])




dataPath = os.path.join(dataDir,'random624.extxyz')
traj = ase.io.read(dataPath, index = ":")
initial = traj[0]
stable = traj[-1]
# 获取每种晶体的特征
#print(initial.get_positions())
matrix = initial.get_positions().flatten()
posList.append(np.concatenate((matrix[-3:], matrix[:-3])))
# 获得每种晶体的吸附能
relaxed_energy = stable.get_potential_energy()
energies.append(relaxed_energy - initialEnergy[2])


maxLen = max(len(array) for array in posList)


X = np.array([np.pad(subarr, (0, maxLen - len(subarr)), constant_values=0) for subarr in posList])


#X = np.vstack(posList)
Y = np.vstack(energies)

print(X)
print(Y)