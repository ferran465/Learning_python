import pyautogui

def pulsar_esc():
    while True:
        try:
            pulsación = pyautogui.press("esc")
            if pulsación == None:
                pyautogui.FAILSAFE == False
                pyautogui.moveTo(800, 800) 
                print("se ha pulsado la tecla")
            else:
                print("no se ha podido pulsar")
        except:
            pass
pulsar_esc()


