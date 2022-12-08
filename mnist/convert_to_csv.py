import os

cwd = os.getcwd() + "\\mnist\\"


def convert():
    labels = open(cwd + "t10k-labels.idx1-ubyte", "rb")
    images = open(cwd + "t10k-images.idx3-ubyte", "rb")
    csv = open(f"{cwd}test-data.csv", "w")
    images.read(16)
    labels.read(8)
    
    outputs = []

    for i in range(10000):
        image = [ord(labels.read(1))]
        for j in range(28*28):
            image.append(ord(images.read(1)))
        outputs.append(image)

    for image in outputs:
        csv.write(",".join(str(pix) for pix in image)+"\n")
    
    labels.close()
    images.close()
    csv.close()
    


