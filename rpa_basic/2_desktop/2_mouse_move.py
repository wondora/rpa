import pyautogui

# pyautogui.moveTo(200, 100)  # 지정한 위치로 마우스를 이동
# pyautogui.moveTo(200, 100, duration=5)  # 5초 동안 지정한 위치로 마우스를 이동

# pyautogui.moveTo(100, 100, duration=0.25)
# print(pyautogui.position()) # point(x, y)
# # 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로 부터 이동)
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position()) # point(x, y)
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position()) # point(x, y)

p = pyautogui.position()
print(p[0], p[1]) # x, y  == print(p.x, p.y)