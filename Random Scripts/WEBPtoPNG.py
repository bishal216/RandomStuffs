import os
from PIL import Image

def convert_all_webp_to_png(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.webp'):
            webp_path = os.path.join(folder_path, filename)
            png_path = os.path.join(folder_path, filename[:-5] + '.png')
            with Image.open(webp_path) as im:
                im.save(png_path, 'png')
            os.remove(webp_path)    
convert_all_webp_to_png('IandI\\images')