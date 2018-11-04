import cv2


a = 0
b = 0
k = 1
a1 = 340
b1 = 220
c = []
d = []


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    img = cv2.resize(img, (340, 220))
    img2 = cv2.resize(img, (340, 220))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #height, width = img.shape[:2]

    a = 0
    b = 0
    k = 1
    i = 0
    j = 0
    for i in range(220):
        for j in range(340):
            try:
                if img[i, j][2] > 220 and img[i, j][1] > 220 and img[i, j][0] > 220 and img[i, j][2] < 255 and img[i, j][1] < 255 and img[i, j][0] < 255:
                    img[i, j] = (255, 255, 255)
                    a = a + j
                    b = b + i
                    k = k + 1
                    c.append(i)
                    d.append(j)

                else:
                    img[i, j] = (0, 0, 0)
            except IndexError:
                continue
            j += 1
        i += 1
    try:
        c1 = min(c)
        c2 = max(c)
        d1 = min(d)
        d2 = max(d)
    except ValueError:
        c1, c2, d1, d2 = 0, 2, 0, 2
    a = int(a / k)
    b = int(b / k)
    #print(c1, d1, c2, d2)
    cv2.rectangle(img2, (d1, c1), (d2, c2), (255, 255, 255), 2)
    #cv2.circle(img2, (a, b), 30, (0, 100, 255), 4)
    cv2.imshow('output', img)
    cv2.imshow('output2', img2)
    c = [item for item in c if item < -1]
    d = [item for item in d if item < -1]
    print(c)
    key = cv2.waitKey(10)




''' 


c = []
d = []
a = 0
b = 0
k = 1

#get_image("/home/dmitriy/PycharmProjects/untitled/venv/0004.jpg")
img = Image.open("6.jpg")
img = img.resize((100, 100), Image.ANTIALIAS)
pix = img.load()
#img.show()
for i in range(640):
    for j in range(480):
        if pix[i, j][0] > 200 and pix[i, j][1] < 100 and pix[i, j][2] < 100:
            pix[i, j] = (255, 255, 255)
            a = a + i
            b = b + j
            k = k +1
            c.append(i)
            d.append(j)
        else:
            pix[i, j] = (0, 0, 0)
        j += 1
    i += 1

#img.show()
for i in range(100):
    for j in range(100):
        try:
            if pix[i, j] == (0, 0, 0) and pix[i - 1, j] == (255, 255, 255) and pix[i, j - 1] == (255, 255, 255):
                pix[i, j] = (255, 255, 255)
            if pix[i, j] == (255, 255, 255) and pix[i + 1, j] == (0, 0, 0) and pix[i, j + 1] == (0, 0, 0) and pix[i - 1, j] == (0, 0, 0):
                pix[i, j] = (0, 0, 0)
        except IndexError:
            continue
        j += 1
    i += 1

x1 = min(c)
x2 = max(c)
y1 = min(d)
y2 = max(d)
a = a / k
b = b / k
print(a, b)
draw = ImageDraw.Draw(img)
draw.rectangle(((x1,y1),(x2, y2)), fill=None, outline=None)
img.show()
#cv2.imwrite("my.png",img)
#cv2.rectangle(img, (x1, y1), (x2, y2), (255,255,255), 2)
#cv2.imshow("lalala", img)
'''