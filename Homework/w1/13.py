num = []    # 数字栈
optr = ['+', '-', '*', '/'] # 识别符号

# 用于获取运算符并计算
def calculate(o:str):
    # +
    if o == optr[0]:
        num[-2] += num[-1]
        del num[-1]
    # -
    elif o == optr[1]:
        num[-2] -= num[-1]
        del num[-1]
    # *
    elif o == optr[2]:
        num[-2] *= num[-1]
        del num[-1]
    # /
    elif o == optr[3]:
        num[-2] /= num[-1]
        del num[-1]

# 检查表达式
def check(s:str):
    count = 0
    # 读取运算符个数
    for i in s:
        if i in optr:
            count += 1
    # 比较
    if count * 2 + 1 != len(s):
        print("输入的逆波兰表达式有误！")
        return 1    #如输入错误即返回错误码1
    else:
        return 0    #如输入正确即返回0

def calcRPN(s : str) ->int:
    # 获取数字，以num栈形式存储
    for i in s:
        if i not in optr:
            num.append(int(i))
    # 运算
        else:
            calculate(i)
    return num.pop()

f = input("请输入逆波兰表达式：").split(" ") # 获取输入并去除空格

if check(f) == 0:
    an = calcRPN(f)
    print(an)   # 打印结果