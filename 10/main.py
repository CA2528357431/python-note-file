#图片复制

with open('ori.jfif','rb') as x:
    with open('cpy.jfif','wb') as y:

        a=x.readlines()
        for r in a:
            y.write(r)


