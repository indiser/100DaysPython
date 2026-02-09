import pyautogui as gui
from PIL import Image, ImageGrab
import time



def iscollide(data):
    # Bird
    for i in range(720,850):                                      
        for j in range(271,273):
            if data[i,j] > 100:
                gui.press("down")
                return

    # Cactus
    for i in range(720,820):
        for j in range(305,308):
            if data[i,j] > 100:            
                gui.press("up")
                return   
    return
         


if __name__=="__main__":
    time.sleep(3)
    gui.press("space")
    while True:
        image=ImageGrab.grab().convert("L")
        data=image.load()
        iscollide(data)
       
    # image=ImageGrab.grab().convert("L")
    # data=image.load()
    # for i in range(720,850):                                      
    #     for j in range(271,273):
    #         data[i,j]=0

    # for i in range(720,820):
    #     for j in range(305,308):
    #         data[i,j] = 0
    # image.show()

