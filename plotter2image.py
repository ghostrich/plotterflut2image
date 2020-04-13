import json
import requests
from PIL import Image

#getting data from plotterflut
r = requests.get(url='https://team-tfm.com/plotterflut/data')
data = r.json()


width = 0
height = 0

#find out the size of the picture
for entry in data:
    col = int(233-(255 * (int(entry['i'])/9)))
    if int(entry['x']) > width:
        width = int(entry['x'])+1
    if int(entry['y']) > height:
        height = int(entry['y'])+1

    
#create image pixel by pixel
img = Image.new( 'L', (width,height), "white")
pixels = img.load()
for entry in data:
    col = int(233-(255 * (int(entry['i'])/9)))
    pixels[int(entry['x']),int(entry['y'])] = (col)

img.show()

