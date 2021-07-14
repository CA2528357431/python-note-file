# 文件的复制（大）


x=open("ori","r")
y=open("cpy","w")
while True:
    temp=x.readline()
    if temp=="":
        break
    y.write(temp)

