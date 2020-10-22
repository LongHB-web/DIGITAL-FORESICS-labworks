import cv2

def GetMousePosition(event, x, y, flags, param):
   if event == cv2.EVENT_LBUTTONDBLCLK:
       print(str(x) + " " + str(y))
       
img = cv2.imread(r"C:\Users\MY PC\Downloads\opencv\sources\samples\data\football.jpeg")
cv2.namedWindow("Football")
cv2.setMouseCallback("Football", GetMousePosition)
cv2.imshow("Football", img)

# ball = img[198:225, 208:239]
# player1 = img[73:239, 108:193]
# player2 = img[87:237, 253:345]
#
# cv2.imwrite("ball.jpeg", ball)
# cv2.imwrite("i1.jpeg", player1)
# cv2.imwrite("i2.jpeg", player2)

cv2.waitKey(0)