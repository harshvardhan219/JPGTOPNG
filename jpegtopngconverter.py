import sys
import os
from PIL import Image

#Taking the path input

image_folder = sys.argv[1]
output_folder = sys.argv[2]

#Creating a folder
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

#Loop through the images
for filename in os.listdir(image_folder):
	img=Image.open(f'{image_folder}{filename}')
	#taking only the first name not the .jpg
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png','png')