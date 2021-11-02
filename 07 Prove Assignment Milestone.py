# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("beach.jpg")
image_background = Image.open("cactus.jpg")
new_image = Image.new('RGB', image_original.size)


(width, height) = image_original.size
print(width, height)

pixels_original = image_original.load()
pixels_background = image_background.load()
pixels_new = new_image.load()


for y in range(400, 600):
    for x in range(200, 800):
        pixels_original[x, y] = (0, 255, 0)


image_original.show()
new_image = image_original
new_image.save('the_new_image.jpg')