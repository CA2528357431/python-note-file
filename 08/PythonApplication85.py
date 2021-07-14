# 文件的复制（小）


x=open("ori","r")
y=open("cpy","w")

temp=x.read()
y.write(temp)
