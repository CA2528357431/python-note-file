# 文件

'''

f=open('text','w')   
# r 读      w 写       a 在尾部追加
f.write("hello,world \nhello,earth")
# write 写
f.close

'''

f=open("text",'r')
w=f.read(5)
print(w)
# read 读若干个
w=f.read(5)
print(w)
#每次read都挪动了指针
f.close

f=open("text",'r')
w=f.readlines()
#读取全部，每行都是元素
# w本质是数组
i=1
for x in w:
    print(i,":  ",x)
    i=i+1
f.close


print()
print()
print()
print()
print()
print()


f=open("text",'r')
w=f.readline()
print(w)
w=f.readline()
print(w)
w=f.readline()
print(w)
w=f.readline()
print(w)
#只读取一行，指针也移动一行