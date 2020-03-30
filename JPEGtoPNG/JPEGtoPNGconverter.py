import sys
import os
from PIL import Image

source_folder = sys.argv[1]
dest_folder = sys.argv[2]

# path = f'./{source_folder}'
# print (path)
# check if folder exist

folder = os.path.exists(f'../{dest_folder}')
# print (folder, f'{dest_folder}')

if (not folder):
    os.mkdir(f'../{dest_folder}')

# loop entire the folder and convert

dir_list = os.listdir(f'../{source_folder}')
print (dir_list)
for image in dir_list:
    img = Image.open(f'../{source_folder}{image}')
    im = os.path.splitext(image)[0]
    #im = image.split('.')[0]
    img.save(f"../{dest_folder}{im}.png", 'png')
    print('all done baccha')

# # save in new folder
