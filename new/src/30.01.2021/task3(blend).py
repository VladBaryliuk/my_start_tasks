from PIL import Image
image1 = Image.open("cat2.jpg")
image2 = Image.open("flashback.jpg")
image2 = image2.resize((225, 225))
res = Image.blend(image1, image2, 0.25)
res.show()
