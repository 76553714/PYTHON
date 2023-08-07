set1 = {'SET1','SET2'}
print('This is a set Set collection:',set1)

#Set集合去除重复,不像字典里提到老key代表更新
liebiao = ['machinegun','shotgun','pistpol','machinegun']
print('Origin list:',liebiao)
set2=set(liebiao)
print('After turned to Set2',set2)

collection1 = {'shanghai','hongkong','beijing'}
collection2 = {'shanghai','tianjin','taiwan'}


#集合的交运算
print('交集:',collection1&collection2)

#集合的并运算
print('并集:',collection1|collection2)

#集合的差运算
print('差集:',collection1-collection2)


#set循环（没顺序的）
for i in collection1:
    print(i)