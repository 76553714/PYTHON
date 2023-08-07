a = [1,3]
b = [1,3]
c = {'K1':'V1'}
d = {'K1':'V1'}
#python里用列表 字典这种没缓存，而用字符串 数字 这种有缓存
print(a==b);# ==判断值
print(a is b,'RAM OF a:',id(a),'RAM OF b:',id(b))#is判断内存地址

print(c==d);
print(c is d,'RAM OF c:',id(c),'RAM OF d:',id(d))

#一般用is 来判空 而不是==
c = None
if c is None:
    print('is empty')
else:
    print('not empty')