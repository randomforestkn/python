from PIL import Image

import glob

# "*.png" = give the list of files that have an extension of png
print(glob.glob("*.png"))

# convert png to jpg
# image to greyscale (mode “L”)
for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("png","jpg"), quality=95)
