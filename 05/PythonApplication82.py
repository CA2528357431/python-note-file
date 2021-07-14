# 文件 追加


#与写入不同的是这个是在原文末尾增加
x=open("first text.txt","a")


x.write('''文件
hello,
this is 
the first
text
''')


x.close()