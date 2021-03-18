import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활서오하된 창
# print(fw.title) # 창의 제목 정보
# print(fw.size)
# print(fw.left, fw.right, fw.top, fw.bottom)
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#   print(w) # 모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle("스티커 메모"):
#   print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

if w.isActive == False:
  w.activate()

if w.isMaximized == False:
  w.maximize()

pyautogui.sleep(1)

w.restore() #원복
w.close()