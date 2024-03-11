import cv2

def locate(source, target, acc=0.9):
    screen = cv2.imread(fr'{source}')
    wanted = cv2.imread(fr'{target}')
    
    result = cv2.matchTemplate(screen, wanted, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if(max_val>=acc):
        return max_loc
    else:
        return None
    
