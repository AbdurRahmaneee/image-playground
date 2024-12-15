from PIL import Image, ImageFilter

# img = Image.open('./astro.jpg')
# # filter_img = img.convert('L')
# # crooked = filter_img.resize(300, 300)
# # box = (100, 100, 400, 400)
# # region = filter_img.crop(box)
# # # crooked.save('grey.png', 'png')
# # # filter_img.show()
# # region.save('cropped.png', 'png')
# img.thumbnail((400, 200))
# img.save('thumbnail.jpg')
# print(img.size)

import sys
import os
# grab first and second argument
# check if new/ exists, if not create it
# loop through Pokedex,
# convert images to png
# save to the new folder
image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('yshsahhaha')

print(image_folder, output_folder)
