import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("123232")
# pyautogui.write("nadocoding", interval=0.25)

# pyautogui.write(["t","e","s","t", "left", "right","a","enter"], interval=0.25)

#특수문자
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간단한 조합키
# pyautogui.hotkey("ctrl", "a")

#한글 처리 pip install pyperclip
import pyperclip
# pyperclip.copy("나도코딩")  # 클립보드 저장
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
  pyperclip.copy(text)  # 클립보드 저장
  pyautogui.hotkey("ctrl", "v")

my_write("너는 코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + Shift + option + q