#元组 tuple 俗称不可变列表,用小括号包起来 可便利 可看可读 可切片 可循环 就是不能改
t = ('你好','谢谢','再见')
print(type(t),t)
print(t[2])
print(t[1:2])

for i in t :
    print("遍历",i)
# t[1] = 'a' #不能改 否则报错

#如果想写元组里只有一个元素 必须后面跟逗号 否则会认为是数学运算优先级
k = (4,)
print(type(k))

#元组的不可变指的仅仅是元组本身,例:
yuanzu = ('0Bye','1OK',[],'BK')#元组本身还是没变,[2]指向了一个新列表,列表可以变
yuanzu[2].append('偷偷在元组中的数组中加一个也没事')
print(yuanzu)