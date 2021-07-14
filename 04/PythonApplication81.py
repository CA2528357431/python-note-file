# 文件 读取


x=open("first text.txt","r")
# "r"代表读取模式
y=x.read()#默认读取全部
print(y)
y=x.readlines()#读取全部
print(y)
x.close()


print()


x=open("first text.txt","r")
y=x.read(5)
# 3代表前三个字，且指针移动三下。再次读写从第4个开始
# \n等转义字符也占一个位置
print(y)
y=x.read(5)
print(y)
x.close()


print()


x=open("first text.txt","r")
y=x.readline()
#第一行本质是“xxx \n ”,所以会多一行空格
#指针也动一行
print(y)
y=x.readline()
print(y)
x.close()


print()


x=open("first text.txt","r")
y=x.readlines()#读取全部
print(y)
x.close()
#与read()区别在于前者直接返回一整个字符串
#而readlines()是返回一个list每行都是一个元素