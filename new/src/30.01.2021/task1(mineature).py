from PIL import Image
image = Image.open("task1.jpg")
image.thumbnail((1024, 768))
image.show()
image.save("pic-1024-768.jpg")
image.thumbnail((600, 400))
image.show()
image.save("pic-600-400.jpg")
image.thumbnail((100, 100))
image.show()
image.save("pic-100-100.jpg")
