from PIL import Image
filename = r'ico.png'
img = Image.open(filename)
ico_sizes = [(64,64), (74, 74), (64, 64), (82,82)]
img.save('img.ico', sizes=ico_sizes)


# pip install Pillow
