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

# 读取已由uncompress.py解压过的文件
dataDir = './data/H'
files = os.listdir(dataDir)
count = 0

for file in files:
    dataPath = os.path.join(dataDir,file)
    traj = ase.io.read(dataPath, index = ":")
    initial = traj[0]
    stable = traj[-1]

    # 获取每种晶体的特征
    # posList.append(initial.get_positions())
    ## 获得所有的坐标，并合成一行
    matrix = initial.get_positions().flatten()
    ## 把H的位置移到前三
    posList.append(np.concatenate((matrix[-3:], matrix[:-3])))


    # 获得每种晶体的吸附能
    relaxed_energy = stable.get_potential_energy()
    energies.append(relaxed_energy - initialEnergy[count])

    # 显示进度
    print("\rprocessing:{:.2f}%".format(count/12828 * 100), end='')
    count += 1

maxLen = max(len(array) for array in posList)
X = np.array([np.pad(subarr, (0, maxLen - len(subarr)), constant_values=0) for subarr in posList])
Y = np.vstack(energies)

np.savez('./data/data.npz',X=X,Y=Y)