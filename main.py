from PIL import Image
# load the image
image = Image.open('sample.jpg')
# report the size of the image
print(image.size)
print(image.format)
# resize image and ignore original aspect ratio
img_resized = image.resize((200,200))
# report the size of the thumbnail
print(img_resized.size)
img_resized.save('sample2.jpg', format='JPEG')
# load the image again and inspect the format
image2 = Image.open('sample2.jpg')
print(image2.format)
