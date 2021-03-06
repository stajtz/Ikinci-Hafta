import cv2
import numpy as np

# Nesne tanıması için cascade mizi okuyoruz
carsCascade = cv2.CascadeClassifier("cars.xml")

#kendi yaptığım cascade
carsCascade2=cv2.CascadeClassifier("cascade.xml")


# Yaya için cascade
#bodyCascade=cv2.CascadeClassifier("body.xml")

# Yaya Tespiti için farklı bir algoritma
#hog=cv2.HOGDescriptor()
#hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def empty(a): pass


# Kameradan gelen görüntüyü almak için değişkenimize atıyoruz
capture = cv2.VideoCapture("MOT17-13.mp4")

# Trackbarları koyabilmek için bir pencere oluşturup trackbarları koyuyoruz
cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc", 1280, 720)
cv2.createTrackbar("Scale", "Sonuc", 400, 1000, empty)
cv2.createTrackbar("Neighb/Box", "Sonuc", 4, 50, empty)
key = None



opencvTrackers={"boosting":cv2.legacy.TrackerBoosting_create(),
                "mil":cv2.legacy.TrackerMIL_create(),
                "kcf":cv2.legacy.TrackerKCF_create(),
                "tld":cv2.legacy.TrackerTLD_create(),
                "medianflow":cv2.legacy.TrackerMedianFlow_create(),
                "mosse":cv2.legacy.TrackerMOSSE_create(),
                "csrt":cv2.legacy.TrackerCSRT_create()}


#tracker oluşturur
#tracker = cv2.legacy.TrackerMOSSE_create()
#tracker = cv2.TrackerKCF_create()
trackerName="kcf"
tracker = opencvTrackers[trackerName]

x  = 0
y  = 0

#obje seçildikten sonra box çıkar
def drawBox(img,bbox):
    global x
    global y
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w), (y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(61,145,64), 2)
    
#Takip işlemi başladığı zaman Nesne tespitini durdurmak için    
track=False

while True:
    # kameradan görüntü bilgisini değişkenlere atıyoruz
    success, frame = capture.read()
    key = cv2.waitKey(8)
    # trackbarlardaki bilgiyi alıyoruz
    scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Sonuc") / 1000)
    neighbor = cv2.getTrackbarPos("Neighb/Box", "Sonuc")

    # eğer kameradan görüntü geliyorsa işlemlerimizi yapıyoruz
    if success:

        # Daha kolay işlem yapmak için gelen görüntünün boyutunu küçültüyoruz
        frame = cv2.resize(frame, dsize=(1280, 720))

        # a tusuna basilinca obje seçmeyi sağlar
        if key == ord("a"):
            track=True
            bbox = cv2.selectROI("Sonuc", frame, False)
            tracker.init(frame, bbox)
            
        # seçilen obje için trackeri sürekli update eder
        ret, bbox = tracker.update(frame)

        if ret:
            #nesne seçilmesi başarılı olarak update edilirse hem çevrevesi çizilir hem de koordinatları yazılıyor
            drawBox(frame, bbox)
            koord = "x: {} y: {}".format(np.round(x), np.round(y))
            cv2.putText(frame, koord, (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (61, 145, 64), 2)
        #ret false olursa ya da henüz nesne seçilmemişse Lost yazılır
        else:
            cv2.putText(frame, "Lost", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


        #Eger takip işlemi başlamışsa nesne tespiti işlemini durduruyor
        if not track:
            
            # Gelen görüntüyü nesneyi yaklaması için cascade veriyoruz
            Rect = carsCascade.detectMultiScale(frame, scaleVal, neighbor)
    
            # Yaya yakalaması için
            #Rect=bodyCascade.detectMultiScale(frame,scaleVal,neighbor)
    
            # Yaya yakalaması için obür algoritma
            #pedestrianRect,weight=hog.detectMultiScale(frame,padding=(neighbor,neighbor),scale=scaleVal)
    
            # cascade den gelen Nesne etrafına bir dikdörtgen çizdiriyoruz
    
            for (x, y, w, h) in Rect:
                cv2.putText(frame, "Araba", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 255, 0))
                #cv2.putText(frame, "Yaya", (x,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,255,0))
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
                
            Rect = carsCascade2.detectMultiScale(frame, scaleVal, neighbor)
            for (x,y,w,h) in Rect:
                cv2.putText(frame, "Araba", (x, y+w +20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255))
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #for (x,y,w,h) in pedestrianRect:
            #    cv2.putText(frame, "Yaya", (x+w-40,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,0,255))
            #    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    
        

        cv2.imshow("Sonuc", frame)

    # klavyeden bir tuşa basılırsa değişkene atıyoruz ve q harfine basılırsa kameradan görüntü almayı durdurup oluşturduğumuz ekranları kapıyoruz
   
    if key == ord("q"): break

capture.release()
cv2.destroyAllWindows()