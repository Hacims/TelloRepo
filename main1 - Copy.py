import tello
from tello_control_ui import TelloUI
import cv2
import time
def main():

    drone = tello.Tello('', 8889)
    vplayer = TelloUI(drone,"./img/")

	# start the Tkinter mainloop
    vplayer.root.mainloop()
print ("start")
time.sleep(5)

##cam = cv2.VideoCapture(0)
##ret, img = cam.read()
##while True:
##    ret, img = cam.read()
##    cv2.imshow('drone', img)
##    if cv2.waitKey(1) == 27:
##        break
if __name__ == "__main__":
    main()
