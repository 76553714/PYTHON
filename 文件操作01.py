#f是文件句柄 负责操纵打开的文件 算是插到文件山的管子
#路径可以是绝对路径和相对路径 切换上一层文件夹：../
fr=open("E:/SRC/PYTHON/文件操作01.txt",mode='r',encoding='utf-8')#r是只读
print(fr.read())

fr.seek(0)#指针重新定位到0
print(fr.read(5))#只读5字符长度

fr.seek(0)
print(fr.readline())#按行读
print(fr.readline())

fr.seek(0)
for line in fr:
    print(line.strip())#strip去掉换行(之前我们提过strip去掉空格回车\n\t)

fr.seek(0)
first = fr.readline()
print(first.strip(),'\n===========')
for line in fr:
    print(line.strip())

#w:write只写模式，重新创建文件，没有则创建，有文件且有内容则清空内容
fw = open("E:/SRC/PYTHON/文件操作02.txt",mode='w',encoding='utf-8')
fw.write('Hi!');fw.write('\nMike')
fw.close()
#a: append 追加写,不会把以前的东西磨出,而是在后面接着写,文件不存在则创建
fa = open("E:/SRC/PYTHON/文件操作03.txt",mode='a',encoding='utf-8')
fa.write('Hi,this is append\n')
fa.close()
# b :Bytes，二进制 一般处理非文本文件，不能指定encoding了
# rb:二进制读取 wb:写入字节 这俩操作可以完成复制
# +: 扩展 极度不推荐
f1 = open("E:/SRC/PYTHON/文件操作01输入.jpg",mode='rb')
f2 = open("E:/SRC/PYTHON/文件操作01输出.jpg",mode='wb')
for neirong in f1:
    f2.write(neirong)

#记得close关闭管道 不然一直占用 会报错
f1.close()
f2.close()

#另一种关闭:会在代码块末端自动加上.close() 包括网络传输也是有这种
with open ("E:/SRC/PYTHON/文件操作01.txt",mode='r',encoding='utf-8') as f1:
    for line in f1 :
        print(line.strip())

#多个也可以 注意反斜杠在python代表两行代码是属于在同一行
with open("E:/SRC/PYTHON/文件操作01.txt",mode='r',encoding='utf-8') as f1,\
    open("E:/SRC/PYTHON/文件操作02.txt",mode='w',encoding='utf-8') as f2:
    for line in f1:
        f2.write(line)