from PIL import Image as im 
from PIL import ImageChops as ic

i1 = im.open("General/XOR/Lemur.png").convert("RGB")
i2 = im.open("General/XOR/Flag.png").convert("RGB")


width, height = i1.size
new_img = im.new("RGB",(width, height))

for x in range(width):
    for y in range(height):
        r1, g1, b1 = i1.getpixel((x, y))
        r2, g2, b2 = i2.getpixel((x,y))
        new_r = r1 ^ r2
        new_g = g1 ^ g2
        new_b = b1 ^ b2
        new_img.putpixel((x, y), (new_r, new_g, new_b))

new_img.save("XORED_Image.png")
