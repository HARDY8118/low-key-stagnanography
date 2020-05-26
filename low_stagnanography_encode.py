import cv2
import sys
import numpy

text=""
try:
    text=sys.argv[1]
except:
    text=input("Text: ")
# text="abcdefghijkl"
if len(text)<=0:
    print("Invalid text")
else:
    size=-1
    for _ in range(0,len(text)):
        if (_**2)*3 >= len(text):
            size=_
            break
    text=text.ljust(((size**2)*3))
    print(text[11])
    size=int((len(text)//3)**0.5)
    t=0
    img=[]
    for i in range(size):
        _=[]
        for j in range(size):
            __=[]
            for k in range(3):
                __.append(ord(text[t]))
                t+=1
            _.append(__)
        img.append(_)
    img=numpy.array(img,'uint8')
    # print(img)
    imgname=""
    try:
        imgname=sys.argv[2]
    except:
        imgname=input("Image name: ")
    if not imgname.endswith(".png"):
        imgname+=".png"
    cv2.imwrite(imgname,img)
    
