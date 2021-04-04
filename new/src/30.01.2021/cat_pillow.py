from PIL import Image
image = Image.open("cat2.jpg")
region = image.crop((100, 10, 200, 215))
region = region.transpose(Image.ROTATE_90)
region = region.rotate(270, expand=True, fillcolor="white")
image.paste(region, (15, 10))
image.show()