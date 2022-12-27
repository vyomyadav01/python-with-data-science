import cv2




def camera(src=0):
    cam = cv2.VideoCapture(src)
    while True:
        status, img = cam.read()
        if not status:
            break
        cv2.imshow('video', img)
        if cv2.waitKey(1) == 27:
            break
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow('image', img)
        cv2.imshow('green', grey)
        cv2.imshow('rgb', rgb)
    cam.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    camera()   