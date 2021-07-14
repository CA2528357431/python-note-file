# 循环输出

x=open("first text.txt","r")
while True:
    y=x.readline()
    if y=="":  
    # 注意  “”
    # 不存在真正的空行
    # 所见的空行都是上一行的\n  
        break
    print(y)