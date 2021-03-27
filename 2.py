import cv2


cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
frame = 0

while True:
    success, img = cap.read()
    cv2.imshow('From Camera', img)

    #создание фотографии
    if cv2.waitKey(1) & 0xFF == ord('q'):
        name = 'frame' + str(frame) + '.jpg'
        print('Creating...' + name)   
        cv2.imwrite(name, img)
        frame += 1

    #завершить программу
    k = cv2.waitKey(30) & 0xFF # ecs button
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


