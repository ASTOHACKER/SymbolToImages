from PIL import Image, ImageDraw, ImageFont

image = Image.open('E:/fornew/girl2.jpg')

width, height = image.size
aspect_ratio = height / width
new_width = 1440
new_height = int(aspect_ratio * new_width * 0.55) 
image = image.resize((new_width, new_height))

# Convert the image to grayscale
image = image.convert('L')

ascii_chars = '"@%#*+=-:. /'

draw_image = Image.new('RGB', (new_width * 6, new_height * 12), color='white')
draw = ImageDraw.Draw(draw_image)
font = ImageFont.load_default()

x = 0
y = 0
for pixel_value in image.getdata():
    char = ascii_chars[pixel_value // 25]
    draw.text((x, y), char, fill='black', font=font)
    x += 6  
    if x >= new_width * 6:
        x = 0
        y += 12  

draw_image.save('ascii_art_fixed_width.png')
draw_image.show()

print("Success")
