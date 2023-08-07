#字典是可以哈希运算的 以key-value的形式存储 根据key来计算一个内存地址 
# 然后将key:value保存在此地址中 这种叫做hash算法
d = {'key1':'VAL1','key1':'VAL2'}
print(d['key1'])
#在 Python 中，字典（Dictionary）的键（Key）是唯一的
#如果在一个字典中出现重复的键，则后面的键值对会覆盖前面的键值对。

#字典的添加数据:
d = {'KEY1':'VAL1','KEY2':'BAT2'}
d['额外K'] = 'ADD-VAL3'

#字典的添加数据:(判断key是否存在,如果不存在才添加这个key和value,存在则啥也不干):
d.setdefault('额外K2','SetDefault-VAL-4')

#字典数据的修改: 跟添加一样,拿出老key直接改
d['额外K']='Modified-VAL'

#字典的删除 字典名.pop(key)
deleted = d.pop('额外K2')
print('已pop删除:',deleted)

#字典的删除法2-Del 跟列表的del一样
del d['KEY2'] 

#字典的遍历：
print(d.items())
#d.items是获取字典d的items属性，但没有调用这个属性
#于没有调用括号()，实际上并未返回字典d中键值对的视图（View），而是返回了一个表示方法对象

print(d.items)#显示了该方法的内存地址而不是实际的键值对视图
#d.items()调用字典d的items()方法,items()会返回一个包含字典d中所有键值对视图,以列表形式展示

#字典的for循环
for k,v in d.items(): 
    print(k,'value：',v)


#字典的查询 法1
print('使用print查询KEY1:',d['KEY1'])
#字典的查询 法2
print('使用get来查询KEY1:',d.get('KEY1','如果不存在则执行这段话'))
#【使用print查询时如果key不存在就会报错，而get不会】
#特殊查询-setDefault setdefault添加后会自动再返回一下他的VALUE
print('Setdefault查询KEY1:',d.setdefault('KEY1'))

#字典的清空 全部删除: 
d.clear() ; print(d)
#注意 循环的时候不能删除 会报错! 把想删除的东西记录到列表中再操作:
info = {'person1':'beijing','person2':'shanghai'}
liebiao = list(info.keys())
for k in liebiao:
    info.pop(k)
print('info=',info)


lst = [11,22,33,44,55,66,77,88,99]
#练习：把上面的数字分成两组-大于50和小于50的 
# 法1：
dayu50 = [] ; xiaoyu50 =[] ; result={}
for num in lst :
    if num < 50 : xiaoyu50.append(num)
    else: dayu50.append(num)

dayu50.sort();xiaoyu50.sort()
result['less50']=xiaoyu50;result['more50']=dayu50
print('Result:',result)


# 法2：
result2={}

for item in lst:
    if item>50:
        if result2.get('bigger') == None:
            result2['bigger']=[item]#如果字典内没这个key则创建，然后数据丢进去
        else : 
            result2['bigger'].append(item)#有的话就直接丢
    else:
        if result2.get('smaller') == None:
            result2['smaller']=[item]
        else : 
            result2['smaller'].append(item)
print('法2Result:',result2)

#法3：
result3={}

for item in lst:
    if item>50:
        result3.setdefault('bigger',[]).append(item)
    else:
        result3.setdefault('smaller',[]).append(item)

print('法3Result:',result3)

#法1：使用两个列表dayu50和xiaoyu50来分别保存大于50和小于50的元素，
# 然后通过sort()方法对这两个列表进行排序，最后将它们存储在result字典中。
# 该算法的时间复杂度是O(nlogn)，其中n是lst列表的元素个数。

# 法2：使用result2字典，通过get()方法来判断是否存在对应的键，
# 然后根据情况创建或追加元素到对应的列表中。这个算法在最坏情况下需要遍历lst列表两次，
# 时间复杂度为O(n)，其中n是lst列表的元素个数。

# 法3：使用result3字典，通过setdefault()方法来判断是否存在对应的键，
# 如果不存在则创建一个空列表，然后直接将元素追加到对应的列表中。这个算法在一次遍历
# lst列表的情况下就可以完成所有操作，时间复杂度为O(n)，其中n是lst列表的元素个数。

# 因此，法3的性能最佳，
# 它只需要一次遍历lst列表就能完成所有操作，
# 并且使用了setdefault()方法可以更快速地操作字典。

#字典的删除