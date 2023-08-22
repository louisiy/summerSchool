y = int(input("year:"))
m = int(input("month:"))
d = int(input("day:"))
i = 1
sum = 0

# 判断闰年
if (y//4 == 0 and y // 100 != 0) or (y // 400 == 0):
    R = 1
else:
    R = 0

Mondict = {1: 31,2: 28,3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}

# 计算月份
while i <= m:
    if i>1:
        sum = sum + int(Mondict[i-1])
    i += 1

# 修正闰年
sum = sum + R + d
print(sum)