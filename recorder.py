import cv2, numpy as np, pyautogui
import time, os, datetime

# your path
path = f'C:/Users/'#YourUser/Desktop/

def screenshot():
    while 0 < 1:
        hour = int(str(datetime.datetime.now()).split(' ')[1].split('.')[0].replace(':',''))
        
        # Generate and Optimize Image
        image = pyautogui.screenshot()
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # image = cv2.resize(image, (1070, 600))
        image = cv2.resize(image, (800, 480))

        files = os.listdir(path+"/images/")

        # write image
        if f"image{int(hour)}.jpg" not in files:
          # cv2.imwrite(path+f"/images/image{int(hour)}.jpg", image) 
            cv2.imwrite(path+f"/images/image{int(hour)}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 60])

        try:
            if str(hour).endswith("00"):
                print(f'One minute cycle complete')
            else:
                os.remove(path+f"/images/image{int(hour)-3}.jpg")
        except:
            pass

        time.sleep(0.5)

screenshot()
