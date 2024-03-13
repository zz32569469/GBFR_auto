import pygetwindow as gw
import pydirectinput as pdi
import pyautogui as pag
import cv2, time, os, Imgfind
from ahk import AHK

pdi.FAILSAFE=False
ahk=AHK()
target = fr'.\save'
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
    pag.screenshot(fr'{target}\scr.png', (869, 121, 869+171, 121+31))
    matchOk=Imgfind.locate(fr'{target}\scr.png', fr'{target}\the_end.png')
    if  matchOk is not None:
        #print('the_end:', matchOk)
        tot+=1
        print(f'已完成{tot}次')
        while True:
            pag.screenshot(fr'{target}\scr.png', (0, 545, 1920, 545+35))
            matchOk=Imgfind.locate(fr'{target}\scr.png', fr'{target}\mvp.png')
            time.sleep(2)
            if  matchOk is not None:
                #print('mvp:', matchOk)
                time.sleep(8)
                pdi.press('enter')
                time.sleep(10)
                if tot==0:
                    pass
                elif tot%10==0:
                    time.sleep(5)
                    pdi.press('w')
                    time.sleep(5)
                    pdi.press('enter')
                    break
                else:
                    pdi.press('enter')
                
                    pag.screenshot(fr'{target}\scr.png', (812, 489, 812+288, 489+35))
                    matchOk=Imgfind.locate(fr'{target}\scr.png', fr'{target}\confirm_to_end.png')
                    if  matchOk is not None:
                        #print('next_game:', matchOk)
                        pdi.press('enter')
                        break
                    else:
                        pass
            else :
                pass
            
    else:
        for _ in range(25):
            ahk.right_click()
            time.sleep(0.45)
    

