import cv2
path = r'C:\Users\vyomy\Downloads\Dhamaal Funny Scene _ Mr. Iyer Drops Javed Jaffrey & Arshad Warsi _ Netflix India (1).mp4'
video = cv2.VideoCapture(path)

while True:
    status, img = video.read()
    if not status:
        break
    cv2.imshow('video', img)
    if cv2.waitKey(1) == 27:
        break
video.release()
cv2.destroyAllWindows()