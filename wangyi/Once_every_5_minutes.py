from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from PIL import Image
import numpy as np
import time
from io import BytesIO
# 创建一个空的图像对象

left = 0  # 左上角横坐标
top = 80  # 左上角纵坐标
right = 2561  # 右下角横坐标
bottom = 1193  # 右下角纵坐标


chrome_options = Options()
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.binary_location = "./chrome-win64/chrome.exe"
# 创建一个WebDriver实例，这里使用Chrome浏览器
driver = webdriver.Chrome(executable_path = "./chromedriver.exe",options=chrome_options)
driver.maximize_window()
# 打开目标网页

driver.get("https://www.163.com/")
sleep(1)
window_height = driver.get_window_size()['height'] - 170 # 窗口高度

page_height = driver.execute_script('return document.documentElement.scrollHeight')  # 页面高度
driver.save_screenshot('./images/part/163.png')

if page_height > window_height:
    n = page_height // window_height  # 需要滚动的次数
    base_mat = np.atleast_2d(Image.open('./images/part/163.png'))  # 打开截图并转为二维矩阵

    for i in range(n):
        driver.execute_script(f'document.documentElement.scrollTop={window_height*(i+1)};')
        sleep(1)
        driver.save_screenshot(f'./images/part/163_{i}.png')  # 保存截图
        image = Image.open(f'./images/part/163_{i}.png')
        cropped_image = image.crop((left, top, right, bottom))
        cropped_image.save(f'./images/part/163_{i}.png')
        image = Image.open(f'./images/part/163_{i}.png')
        mat = np.atleast_2d(image)  # 打开截图并转为二维矩阵
        base_mat = np.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
    Image.fromarray(base_mat).save(f'./images/complete/163_{int(time.time())}.png')

driver.quit()


