# name = input("输入你名字")
# age  = input("输入你年龄")
# hobby= input("输入你爱好")

# wholemsg = """
# ---info of %s--- 
# Name :%s
# age  :%s
# hobby:%s
# ---end---
# """%(name,name,age,hobby)
# print(wholemsg)
#  #老格式输出 %s(string)占位字符串 %d占位整数(digit) %f占位小数（float）
#print("My name is %s and I am %d,my salary is %.2f "%("jack",18,28.22)) 

#新版本输出 f-string python3.5以上
addr = "黄河路"
time = "2023年7月29"

print(f"我在{addr},现在时间是{time}") #最好办法 其他基本不用

print("我在{},现在时间是{}".format(addr,time))

print("我在{1},现在时间是{0}".format(time,addr))
print("我在{1},{1}这里真不错".format(time,addr))

print("我在{dizhi},现在时间是{shijian}".format(shijian=time,dizhi=addr))