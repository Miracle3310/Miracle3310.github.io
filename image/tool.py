import base64

def img2base(path):
    f=open(path,'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    f.close()
    print(ls_f)

def base2img(bs,path='image.jpg'):
    imgdata = base64.b64decode(bs)
    file = open(path, 'wb')
    file.write(imgdata)
    file.close()

if __name__ == '__main__':
    img2base('kyaru.png')