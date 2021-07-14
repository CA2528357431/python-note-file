# 文件安全打开

with open("better","w",encoding="utf8") as x:
    x.write("hello world")
    x.close()
with open("better","r",encoding="utf8") as x:
    print(x.read())
    x.close()

#分别是 文件名 打开方式 编码方式
#有效防止无法读取 非utf8 的文本
#用于爬虫，自己写没必要用
#或者自己写时用  with open("better","w") as x: