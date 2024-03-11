import pygetwindow as gw
import pydirectinput as pdi
import pyautogui as pag
import cv2, time, os, Imgfind
from ahk import AHK

pdi.FAILSAFE=False
ahk=AHK()
target = fr'GBFR_auto\save\scr.png'

while True:
    windows = gw.getAllTitles()
    if 'Granblue Fantasy: Relink' in windows:
        t_window = gw.getWindowsWithTitle('Granblue Fantasy: Relink')[0]
        time.sleep(3)
        break
    else :
        print('GBFR not found')
        time.sleep(5)

while True:
    pag.screenshot(target)
    if Imgfind.locate(target, r'GBFR_auto\save\the_end.png') is not None:
        while True:
            pag.screenshot(target)
            time.sleep(10)
            if Imgfind.locate(target, r'GBFR_auto\save\mvp.png') is not None:
                pdi.press('enter')
                time.sleep(10)
                if Imgfind.locate(target, r'GBFR_auto\save\continue.png') is not None:
                    pdi.press('s')
                    time.sleep(3)
                    pdi.press('enter')
                else:
                    pdi.press('enter')
                
                    pag.screenshot(target)
                    if Imgfind.locate(target, r'GBFR_auto\save\confirm_to_end.png') is not None:
                        pdi.press('enter')
                        break
                    else:
                        pass
            else :
                pass
            
    else:
        for _ in range(40):
            ahk.right_click()
            time.sleep(0.33)
    

