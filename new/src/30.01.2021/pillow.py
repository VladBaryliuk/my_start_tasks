from PIL import Image
image = Image.open("cat1.jpg")
image.show()
width = image.width
height = image.height
image.thumbnail((128, 128))
image.show()
image.save("cat-small.jpg")
