from PIL import Image
image = Image.open("task2.jpg")
width = image.width
height = image.height
print(width, height)
region1 = image.crop((0, 0, 150, 150))
region2 = image.crop((150, 0, 300, 150))
region3 = image.crop((0, 150, 150, 300))
region4 = image.crop((150, 150, 300, 300))
region1 = region1.transpose(Image.ROTATE_90)
region2 = region2.transpose(Image.ROTATE_180)
region3 = region3.transpose(Image.ROTATE_180)
region4 = region4.transpose(Image.ROTATE_270)
image.paste(region1, (0, 0, 150, 150))
image.paste(region2, (150, 0, 300, 150))
image.paste(region3, (0, 150, 150, 300))
image.paste(region4, (150, 150, 300, 300))
image.show()
