import os
import imagehash
from PIL import Image

images = 'images'
hashes = {}
for filename in os.listdir(images):
    filepath = os.path.join(images, filename)
    #print(filepath)

    with Image.open(filepath) as image:
        img_hash = imagehash.average_hash(image, hash_size=8)
        #print(img_hash)
        if img_hash in hashes:
           print('Duplicate image found', filename)
           print('Original hash:', hashes[img_hash])
           os.remove(filepath)
           print(f"Removed duplicate: {filename}")
        else:
            hashes[img_hash] = filename


