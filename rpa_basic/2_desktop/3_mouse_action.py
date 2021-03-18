import pyautogui

pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(215, 169, duration=1)

# pyautogui.click()  #현재 마우스 위치에서 클릭
# # pyautogui.click()은 아래 두개를 실행한 것과 동일
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.click(clicks=2)  # 더블클릭 효과

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()

# pyautogui.rightClick()
# pyautogui.middleClick()  # 마우스 휠

# print(pyautogui.position())
# pyautogui.moveTo(113, 110)
# pyautogui.drag(100, 0, duration=0.25) # 현재 위치 기준으로 x 100, y 0 만큼 드래그
# pyautogui.dragTo(100, 200, duration=0.25)  # 절대 좌표 기준

pyautogui.scroll(300) # 양수이면 위방향으로, 음수이면 아래로 ...