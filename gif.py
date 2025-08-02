import imageio.v3 as iio
filenames = ['chicklet1.png', 'chicklet2.png' , 'chicklet3.png' , 'chicklet4.png']
images = [ ]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('chicklets.gif',images,loop = 0,duration = 100)

print("🎉 GIF created as chicklets.gif")
