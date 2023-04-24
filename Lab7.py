#this allows the use of increasing the size of the background or border but not the image. 

from PIL import Image
import numpy as np
my_src = Image.open('wave.jpeg')
pic1 = Image.open('TonyHawk.jpeg')
pic2 = Image.open('shoe.jpeg')
new_w, new_h = my_src.width + 700, my_src.height + 700
my_trgt = Image.new('RGB', (new_w, new_h), 'salmon')


#I add the three images in
target_x = 0
for source_x in range(my_src.width):
   target_y = 0
   for source_y in range(my_src.height):
       pixel = my_src.getpixel((source_x, source_y))
       my_trgt.putpixel((target_x, target_y), pixel)
       target_y += 1
   target_x += 1


target_x = 1600
for source_x in range(pic1.width):
   target_y = 0
   for source_y in range(pic1.height):
       pixel = pic1.getpixel((source_x, source_y))
       my_trgt.putpixel((target_x, target_y), pixel)
       target_y += 1
   target_x += 1


target_x = 1300
for source_x in range(pic2.width):
   target_y = 2000
   for source_y in range(pic2.height):
       pixel = pic2.getpixel((source_x, source_y))
       my_trgt.putpixel((target_x, target_y), pixel)
       target_y += 1
   target_x += 1

