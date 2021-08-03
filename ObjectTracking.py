import cv2

cap = cv2.VideoCapture("MOT17-13.mp4")
#tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.legacy.TrackerCSRT_create()

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w), (y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    imgresized = cv2.resize(img, (1280, 720), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)

    if cv2.waitKey(33) == ord("a"):
        bbox = cv2.selectROI("Tracking", imgresized, False)
        tracker.init(imgresized, bbox)

    ret, bbox = tracker.update(imgresized)

    if ret:
        drawBox(imgresized, bbox)
    else:
        cv2.putText(imgresized, "Lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Tracking", imgresized)

    if cv2.waitKey(1) & 0xff ==ord("q"):
        bbox = ()