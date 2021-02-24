import pyautogui as ag
import time

print("5秒後に、左上の座標を取得します...")
time.sleep(5)
print("座標：",ag.position())

print("10秒後に、右下の座標の取得します...")
time.sleep(10)
print("座標：",ag.position())
