bool_title = input("本のタイトルを入力してください：")
number_of_pages = input("本のページ数を入力してください：")
get_coordinate = input("座標を取得しますか？(y,N)：")
interval = input("間隔を入力してください？(初期値[0.1])：")

import pyautogui as ag
import os
import time

if get_coordinate == "y":
    print("5秒後に、左上の座標を取得します...")
    time.sleep(5)
    left_x_coordinate, left_y_coordinate  = ag.position()
    print("座標：",left_x_coordinate, left_y_coordinate)
    
    ag.click(x=51, y=461, button='left')

    print("10秒後に、右下の座標の取得します...")
    time.sleep(10)
    right_x_coordinate, right_y_coordinate  = ag.position()
    print("座標：",right_x_coordinate, right_y_coordinate)

    height = right_y_coordinate - left_y_coordinate
    width = right_x_coordinate - left_x_coordinate
else:
    left_x_coordinate, left_y_coordinate, width, height = 130, 40, 1175, 830

if interval == '':
    interval = 0.1
else:
    interval = int(interval)

time.sleep(5)
ag.click(x=51, y=461, button='left')

dir_path = '/Users/ryota/desktop/kindle/' + bool_title + '/'
screen_shot_save_path = dir_path + bool_title +'.png'
os.mkdir(dir_path)

for i in range(-(-int(number_of_pages) // 2)):
    screen_shot_save_path = dir_path + str(i+1) + "_" + bool_title +'.png'
    ag.screenshot(region=(left_x_coordinate, left_y_coordinate, width, height)).save(screen_shot_save_path)
    ag.click(x=1415, y=468, button='left')
    time.sleep(interval)
    
ag.click(x=51, y=461, button='left')
