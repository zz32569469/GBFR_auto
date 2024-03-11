import pygetwindow as gw
import pydirectinput as pdi
import pyautogui as pag
import cv2, time, os, Imgfind
from ahk import AHK

pdi.FAILSAFE=False
ahk=AHK()
target = fr'path'
tot=1

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
    pag.screenshot(fr'{target}\scr.png')
    if Imgfind.locate(fr'{target}\scr.png', fr'{target}\the_end.png') is not None:
        tot+=1
        print(f'已完成{tot}次')
        while True:
            pag.screenshot(fr'{target}\scr.png')
            time.sleep(2)
            if Imgfind.locate(fr'{target}\scr.png', fr'{target}\mvp.png') is not None:
                time.sleep(8)
                pdi.press('enter')
                time.sleep(10)
                if tot%10==0:
                    pag.screenshot(fr'{target}\ten.png')
                    time.sleep(5)
                    pdi.press('w')
                    time.sleep(5)
                    pdi.press('enter')
                else:
                    pdi.press('enter')
                
                    pag.screenshot(fr'{target}\scr.png')
                    if Imgfind.locate(fr'{target}\scr.png', fr'{target}\confirm_to_end.png') is not None:
                        pdi.press('enter')
                        break
                    else:
                        pass
            else :
                pass
            
    else:
        for _ in range(30):
            ahk.right_click()
            time.sleep(0.33)
    

