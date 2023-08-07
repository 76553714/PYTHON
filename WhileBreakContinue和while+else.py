# s = int(input("你想要多少的阶乘，来个整数"))
# if s < 0:
#     print("非法输入 必须大于0")
# jiecheng = 1
# while s  > 0 :
#     jiecheng = jiecheng * s
#     s = s - 1
# print(jiecheng)
maxout = int(input("你想要出去几次"))
cishu = 1
while cishu <= maxout :
    if   cishu == 50 : print("第"+ str(cishu) +"次出不去了 因为有警察在外面");
    elif cishu == 100 :print("这是第100次 但突然太累了 从此永远宅家里");break
    else:print("第"+ str(cishu) +"次出去成功");
    cishu = cishu+ 1
print("Done")


#走break就不走else
i = 0
while i < 10:
    i+=1;print(i)
    if i == 7:
        print('Hi here is 7 will be continue')
        continue#pass#break
else:print('OK of else')
    
#输入一个数字 判断是不是质数
n = int(input('Pls input a number，Must more than 1')) 

while 2 < n :
    if n % i ==0:
        print('Not a prime,exited')   
        break;
    i+=1
else:
    print('It is a prime')