# This line imports or includes the library we will need
from PIL import Image

#This is the beach (Background Image)
image_beach = Image.open("beach.jpg")
width, height = image_beach.size
pixels_beach = image_beach.load()

#This is the cactus (Front Image)
image_cactus = Image.open("cactus.jpg")
width, height = image_cactus.size
pixels_cactus = image_cactus.load()

#This is the new Image 
new_image = Image.new('RGB', image_beach.size)
pixels_new = new_image.load()


for y in range(0, height):
     for x in range (0, width):
        (r, g, b) = pixels_beach[x,y]
        pixels_new[x,y] = (r, g, b)

#New image pixels 
for y in range(0, height):
    for x in range (0, width):
        (rc, gc, bc) = pixels_cactus[x,y]
        (r, g, b) = pixels_new[x,y] # This is where I put the beach pixels to the new image 
        
        #This is the part where I take the green pixes out of the image and put it in the cactus pixels 
        if gc >= 125 and bc <= 100 and rc <= 100:
            pixels_cactus[x,y] = (r, g, b)
            
image_cactus.show()
# image_cactus.save('New Picture.jpg')
       



    






















# (width, height) = image_original.size
# print(width, height)
# 
# pixels_original = image_original.load()
# pixels_background = image_background.load()
# pixels_new = new_image.load()
# 
# 
# for y in range(400, 600):
#     for x in range(200, 800):
#         pixels_original[x, y] = (0, 255, 0)
# 
# 
# image_original.show()
# new_image = image_original
# new_image.save('the_new_image.jpg')