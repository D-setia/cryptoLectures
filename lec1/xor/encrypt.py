from PIL import Image
import numpy
import random

originalImg = Image.open("image.png")
(width, height) = originalImg.size

originalImgArray = list(originalImg.getdata())

randImgArray = [[[ random.randrange(256) for i in range(3)]  for j in range(width)] for k in range(height)]

orImgArray = [[[0 for i in range(3)]  for j in range(width)] for k in range(height)]
andImgArray = [[[0 for i in range(3)]  for j in range(width)] for k in range(height)]
xorImgArray = [[[0 for i in range(3)]  for j in range(width)] for k in range(height)]


for i in range(height):
    for j in range(width):
        for k in range(3):
            orImgArray[i][j][k] = originalImgArray[i*width+j][k] | randImgArray[i][j][k]
            andImgArray[i][j][k] = originalImgArray[i*width+j][k] & randImgArray[i][j][k]
            xorImgArray[i][j][k] = originalImgArray[i*width+j][k] ^ randImgArray[i][j][k]



randImgArray = numpy.array(randImgArray, dtype = numpy.uint8)
randImage = Image.fromarray(randImgArray)
randImage.save("rand.png")

orImgArray = numpy.array(orImgArray, dtype = numpy.uint8)
orImage = Image.fromarray(orImgArray)
orImage.save("orEnc.png")

andImgArray = numpy.array(andImgArray, dtype = numpy.uint8)
andImage = Image.fromarray(andImgArray)
andImage.save("andEnc.png")

xorImgArray = numpy.array(xorImgArray, dtype = numpy.uint8)
xorImage = Image.fromarray(xorImgArray)
xorImage.save("xorEnc.png")
