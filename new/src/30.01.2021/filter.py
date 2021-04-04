from PIL import Image, ImageFilter
image = Image.open("task1.jpg")
image = image.filter(ImageFilter.EMBOSS)
image.show()