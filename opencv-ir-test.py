## ermittle Farbwerte eines Tennisballs
 
import cv2
 
# initialisiere Webcam
cam = cv2.VideoCapture(0)
 
# definiere Region of Interest
x, y, w, h = 400, 400, 100, 100
 
# zeige Stream von WebCam an
while cam.isOpened():
    # lese frame von WebCam
    ret, frame = cam.read()
 
    # konvertiere Frame in HSV-Farbraum, um besser nach Farb-Ranges filtern zu können
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # waehle ein Region auf Interest an Punkt: (y, x) mit Dimension 50x50 Pixel
    region_of_interest = image[y:h, x:w]
 
    # zeichne Rechteck in Bild
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), thickness=1)
 
    b, g, r = cv2.mean(region_of_interest)
 
    # zeige Frame an
    cv2.imshow("frame", frame)
 
    # warte auf Tastendruck (sonst sieht man das Fenster nicht)
    key = cv2.waitKey(1) & 0xff
 
    # wenn ESC gedrückt, beende Programm
    if key == 27:
        break
        print("test")






