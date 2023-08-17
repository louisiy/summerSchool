def output(s,l):
    if l == 0:
        return
    print(s[l-1])
    output(s,l-1)

list1 = ['Google', 'Meta', 'Taobao', 'Baidu']
#list1.reverse()
#print ("列表反转后: ", list1)
output(list1,4)