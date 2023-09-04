import os
import lzma

# 定义文件路径，采用相对路径
input_path = './data/1'
output_path = './data/H'

# 获得文件列表
files = os.listdir(input_path)

# 为了解压缩过程更有体验，定义计数器
count = 0

for file_name in files:
    # 定义每个完整文件名
    file_path = os.path.join(input_path, file_name)
    output_file = os.path.join(output_path,file_name[:-3])

    # 解压缩
    with lzma.open(file_path, 'rb') as compressed_file:
        with open(output_file, 'wb') as output:
            output.write(compressed_file.read())
    # 计数器工作
    count += 1
    print(count)
