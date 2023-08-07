liebiao = ["字符",True,230,["甚至可以列表套列表",1],"对不对"]
print(liebiao)

lb = ['1UFO','2Jack','3Kali','4Joy']
newlb = ['你好我是新列表','QG2018','WCG2029']
print('原始表1:',lb)
print('原始表2:',lb)

lb.append("〇追加，从尾部加入")
print('追加',lb) #一般用追加而不是插入,因为性能

lb.insert(2,"这是插入项") 
print('插入:',lb) #插入至索引2号位 后面元素自动全体后挪

lb.remove('2Jack') #移除
print('Remove移除了2Jack',lb) 
del lb[1] #删除列表中的第2索引位置
print('del了lb的[1]:',lb)

print('before POP:',lb)
print('POPing:',lb.pop())
print('After POP:',lb) #POP就是从最尾部喷发(返回输出)出一个元素并且把它移出列表

lb.extend(newlb)
print('列表的拓展聚合',lb)

lb[1]='2Jackson';print('修改元素',lb) #列表元素的修改

#切片：跟原来字符串切片操作原理相似
lb = ['1UFO','2Jack','3Kali','4Joy','5Dank1ng']
print(lb[1]) ; print(lb[-2]) ; print(lb[0:6:2]) ; print(lb[0:len(lb):2])
#切片操作不会引发索引越界错误，而会自动调整超出范围的索引为列表的边界索引
#这样是为了更方便地进行切片操作而不必担心超出索引范围导致错误,和print(lb[0:len(lb):2])等价

#列表与增强for和range配合
for count in range(0,6,2):
    print(f"这是索引{count},它是:",lb[count])

for item in lb:  
    print(item)

lb.clear() #清空，删表
print('lb被清空:',lb)

#实战:把所有姓王的名字都变成帅哥
lst = ['王大胖','王佳明','刘某','金三胖','王西只']
for i in range(len(lst)):
    item = lst[i]
    if item.startswith('王'):
        lst[i]='帅哥'
print(lst,'一共有',lst.count('帅哥'),'个帅哥,都姓王哈哈')

#列表的反转-reverse
lst.reverse();print('反转后:',lst)

#列表中值的大小排序 sort
numberlist=[1,5,3,9,0,-4]
chineselist=['从','啊','怕','吧']
numberlist.sort();print(numberlist) #从小到大
numberlist.sort(reverse=True);print(numberlist) #从大到小
chineselist.sort();print(chineselist)

print(dir(list)) #看看列表所有操作

#额外：列表的循环和删除 尽量不要同时发生 例如
names = ['张大冰','张锋','张强','张丽']
for name in names : 
    if name.startswith('张'):
        names.remove(name)
print(names) #输出['张锋', '张丽'] 因为删除后导致剩下元素位置前移

#解决方案1:单独写一个要删除的列表
names = ['张大冰','张锋','张强','张丽']
deletenames = []

for name in names : 
    if name.startswith("张"):
        deletenames.append(name)

for willdelete in deletenames:
    names.remove(willdelete)
print('法一最后：',names)

#解决方案2:切片-浅拷贝
for name in names[:]:
    if name.startswith('张'):
        names.remove(name)
print('法2最后：',names)