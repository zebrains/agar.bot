import win32gui, time

def GetPosition():
    while 1:
        print win32gui.GetCursorPos()
        time.sleep(1)

GetPosition()
