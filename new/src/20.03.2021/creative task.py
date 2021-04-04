import os
from PIL import Image
ROOT_DIR = r'D:\Программирование\Влада программирование\src\20.03.2021\cute_cats'
TARGET_DIR = r'D:\Программирование\Влада программирование\src\20.03.2021\black_and_white_cats'
print(os.listdir(ROOT_DIR))
img = Image.open(ROOT_DIR + '/cat1.jpg')
for i in range(1,6):
    img = Image.open(f'{ROOT_DIR}/cat{i}.jpg')
    img = img.convert('1')
    img.save(f'{TARGET_DIR}/cat{i}.jpg', 'JPEG')
