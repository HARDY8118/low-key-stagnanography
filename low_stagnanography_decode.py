import cv2
import sys

filename=""
try:
    filename=sys.argv[1]
except:
    filename=input("Filename: ")
    # filename="all.png"

filename+="" if filename.endswith(".png") else ".png"

if not len(filename):
    print("Invalid filename")
else:
    img=cv2.imread(filename)
    try:
        if len(img):
            for i in img:
                for j in i:
                    for k in j:
                        print(chr(k),end="")
            print()
    except TypeError:
        if img==None:
            print(f"Unable to open {filename}")