import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()

# 89,130 255,0,0 #FF0000
pixel = pyautogui.pixel(89, 130)
# print(pixel)

# 아래 두 결과는 같다.
# print(pyautogui.pixelMatchesColor(89, 130, (255,0,0)))
print(pyautogui.pixelMatchesColor(89, 130, pixel))