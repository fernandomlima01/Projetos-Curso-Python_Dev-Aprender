# Reconhecimento Imagem
# OBS: Deixar sempre no formato .png
import pyautogui

# screenshot = pyautogui.screenshot()
# screenshot.save('screenshot_test.png')

#print(pyautogui.locateOnScreen('num_3.png',confidence=0.8))

num3 = pyautogui.locateCenterOnScreen('num_3.png',confidence=0.9)
print(num3)
pyautogui.click(num3[0],num3[1],duration=2)
