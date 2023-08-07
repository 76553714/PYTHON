#赋值-仅仅引用地址
liebiao1 = ['你好','我好']
liebiao2 = liebiao1
liebiao1.append('大家好')
print('列表1内容:',liebiao1,'列表2内容：',liebiao2)
print('列表1内存地址:',id(liebiao1),'列表2内存地址：',id(liebiao2))

zidian1 = {'KEY1':'VALUE1','KEY2':'VALUE2'}
zidian2 = zidian1
zidian1['KEY3']='NewValue3'
print('字典1内容:',zidian1,'字典2内容：',zidian2)
print('字典1内存地址:',id(zidian1),'字典2内存地址：',id(zidian2))

#copy：浅拷贝 相当于抄作业,别人说详见附录3,我们也说详见附录3
liebiao3 = ['car','Plane','Ship']
liebiao4 = liebiao3.copy()
print('列表3内容:',liebiao3,'列表4内容：',liebiao4)
print('列表3内存地址:',id(liebiao3),'列表4内存地址：',id(liebiao4))

liebiao5 = ['car','Ship',['Driver','Passenger']]
liebiao6 = liebiao5.copy()
liebiao5[2].append('Farmer')
print('列表5内容:',liebiao5,'列表6内容：',liebiao6)
print('列表5内存地址:',id(liebiao5),'列表6内存地址：',id(liebiao6))
print('列表5中乘员列表地址:',id(liebiao5[2]),'列表6乘员列表地址：',id(liebiao6[2]))

#import copy :: copy.Deepcppy()深度copy需要导包,相当于别人说见附录3,我们说见自己的附录9
import copy
liebiao7 = ['car','Ship',['Driver','Passenger']]
liebiao8 = copy.deepcopy(liebiao7)
liebiao5[2].append('Farmer')
print('列表7内容:',liebiao7,'列表8内容：',liebiao8)
print('列表7内存地址:',id(liebiao7),'列表8内存地址：',id(liebiao8))
print('列表7中乘员列表地址:',id(liebiao7[2]),'列表8乘员列表地址：',id(liebiao8[2]))