import win32api, win32con, win32com.client, time

Name = (2729, 281)
Server = (2732, 326)
USWest = (2736, 365)
Settings = (3015, 385)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def move(x,y):
    win32api.SetCursorPos((x,y))

#Move to Name location and click
click(Name[0], Name[1])

#Send Name
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("Agarbot")

#Move and click to Region
click(Server[0], Server[1])
time.sleep(.25)

#Select West
click(USWest[0], USWest[1])
time.sleep(.25)

#Click Play
click(USWest[0], USWest[1])
