def calcRPN(s : str) ->int:
    while len(s)>0:
        temp1 = s.pop(0)
        temp2 = s.pop(0)
        temp3 = s.pop(0)
        if temp3 == '+':

        elif temp3 == '-':

        elif temp3 == '*':

        elif temp3 == '/':
            
        else:
            print("输入的逆波兰表达式有误！")

f = input()
print(calcRPN(f))