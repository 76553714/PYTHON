# s = int(input("你想要多少的阶乘，来个整数"))
# if s < 0:
#     print("非法输入 必须大于0")
# jiecheng = 1
# while s  > 0 :
#     jiecheng = jiecheng * s
#     s = s - 1
# print(jiecheng)

# maxout = int(input("你想要出去几次"))
# cishu = 1
# while cishu <= maxout :
#     if   cishu == 50 : print("第"+ str(cishu) +"次出不去了 因为有警察在外面");
#     elif cishu == 100 :print("这是第100次 但突然太累了 从此永远宅家里");break
#     else:print("第"+ str(cishu) +"次出去成功");
#     cishu = cishu+ 1
# print("Done")

#这里开始增强for循环
names = ["小红", "小明", "小刚", "小芳", "小李"] #名字列表
nameslist=["Mike","Jack","Bro","Dude"]
nihao = "你好啊"
for name in names:
    if name == "小明":
        continue #如果是小明就不跟他打招呼,跳过本次循环
    print("Hello,", name)

for names in nameslist:
    print(names)

for onebyone in nihao:
    print(onebyone)

for i1 in range(10):  #range就是前闭后开
    print("\t",i1)

for i2 in range(5,10): #所以依然是顾头不顾尾
    print(i2)

for i3 in range(1,10,2): #每2个数一次
    print("\t",i3)

#注意 in 如果单用还可以判断某个元素是否在某个组中
print('Mike在namelist中吗:',"Mike" in nameslist)
print('大闸蟹在namelist中吗:',"大闸蟹" in nameslist)