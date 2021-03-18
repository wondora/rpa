import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# # print(file_menu)
# pyautogui.click(file_menu)

# 똑같은 그림일 경우
# for i in pyautogui.locateAllOnScreen("sample.png")
#   pyautogui.click(i, duration=0.25)

# 속도 개선
# 1. GrayScale 정확도 떨어짐
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(x, y, width, height))
# pyautogui.moveTo(trash_icon)
# pyautogui.mouseInfo() # 좌표 알아내기

# 3. 정확도 조정 pip install opencv-python

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", confidence=0.9))
# pyautogui.moveTo(trash_icon)


# 자동화 대상 이미지가 늦게 뜰 경우
# 1. 무작정 기달리기

# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:  
#   pyautogui.click(file_menu_notepad)
# else:
#   print("발견 실패")
# while file_menu_notepad is None:
#   file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#   print("발견 실패")

# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10
# start = time.time() # 시작시간 설정

# file_menu_notepad = None
# while file_menu_notepad is None:
#   file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#   end = time.time() # 종료시간 설정
#   if end - start > timeout:
#     print("시간 종료")
#     sys.ext()

def find_target(img_file, timeout=30):
  start = time.time()
  target = None
  while target is None:
    target = pyautogui.locateOnScreen(img_file)
    end = time.time()
    if end - start > timeout:
      break
  return target
    
def my_click(img_file, timeout=30):
  target = find_target(img_file, timeout)
  if target:
    pyautogui.click(target)
  else:
    print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
    sys.exit()

my_click("file_menu_notepad.png", 10)
# pyautogui.click(file_menu_notepad)


