from PIL import Image

cuts = 10
Image.MAX_IMAGE_PIXELS = 1000000000
img = Image.open('biggest_map.bmp')
w,h = img.size
for i in range(cuts):
    for j in range(cuts):
        img.crop((w/cuts*i, h/cuts*j, (w/cuts)*(i+1),(h/cuts)*(j+1))).save('./sections/section'+str(i)+str(j)+'.png')

