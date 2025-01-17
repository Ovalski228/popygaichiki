#Импортируем нампай и opencv
import numpy as np
import cv2

# Тута создается черный фон
height, width = 500, 500
image = np.zeros((height, width, 3), dtype=np.uint8)

# Тута рисуются стены дома
cv2.rectangle(image, (150, 250), (350, 450), (255, 255, 255), -1)

# Тута делается крыша
pts_roof = np.array([[150, 250], [250, 100], [350, 250]], dtype=np.int32)
cv2.fillPoly(image, [pts_roof], (255, 255, 255))

# Тута делается шедевральная дверца
cv2.rectangle(image, (230, 350), (270, 450), (100, 100, 100), -1)

# Окошечки
cv2.rectangle(image, (170, 300), (210, 330), (0, 0, 0), -1)
cv2.rectangle(image, (290, 300), (330, 330), (0, 0, 0), -1)

# Выводим изо на наши экранчики
cv2.imshow('Домик', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
