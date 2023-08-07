# w2 = "HolyShit"
# t2 = "abc_efu_哈csd哈ok ay" #句段头大写，也就是A E C O A大写
# print(w2[2])
# print(w2[0:3:1], w2[3:1:-1])#1切到3 步长为正1;此时d是0位 m是1 n是2 同样骨头不顾尾
# print(w2.upper(), w2.lower()) # 大写 # 小写
# print(w2.swapcase(), w2.capitalize()) # 颠倒大小;首字母大写
# print(t2.title())
# while True:
#     s2 = input("pls input words to say(Exit to end)")
#     if s2.upper() == "EXIT": break # ignore whether upper or lower
#     print(s2)               #总结 其他都不用记 只记住Upper最重要


s = "joyDreamerJoy真不错joy"
t = " \n  HAHAHOKOK\n \t\t"
o = "wdnmd_OK_wdnmd"
print(s.center(30)) #强行拉长到20个长度 并且居中
print(s.center(30,"*")) #强行拉长到20个长度 *来填充

print(t.strip()) #去掉两边\n \t 以及空格 scrip意思是脱
print(o.strip("wdnmd")); #去掉两边wdnmd
print(o.strip("wd")); print(o.strip("nmd"))

print(s.replace("joy","Kali")) # joy替换为Kali

liebiao = o.split("_") #用_位标志分割 返回值需要一个数组去接
print(liebiao)
pinjie = "和".join(liebiao)
print(pinjie) #使用 和 将列表里的字符连起来

# startswith endswith #
n1 = "张上三" ; n2 = "李四" ;
if n1.startswith("张"):
    print("这人姓张")
else : print("这人不姓张，姓"+n2[0])
if n2.startswith("张"):
    print("这人姓张")
else : print("这人不姓张，姓"+n2[0])

if n1.endswith("三"):
    print("结尾是三")

# find count index #
m = "AK47 M4A1 M249 USP FAMAS"
print(m.find("M4A1")); print(m.find("PPS"))#如果找到则返回首字位置 没找到则-1
print(m.count("M")) #统计数量
print(m.index("A1")) #A1这个字符串的开头索引,但如果不存在会报错,所以尽量用find

print(len(m));print(len("你好")) #m这个字符的字符长度,汉字也是1