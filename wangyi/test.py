from PIL import Image

# 打开要裁剪的图片
image = Image.open("./images/part/163.png")
left = 0  # 左上角横坐标
top = 80  # 左上角纵坐标
right = 2560  # 右下角横坐标
bottom = 1200  # 右下角纵坐标
cropped_image = image.crop((left, top, right, bottom))
cropped_image.save("cropped_image.png")