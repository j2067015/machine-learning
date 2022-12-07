import gzip
import numpy as np
import matplotlib.pyplot as plt
import os

cwd = os.getcwd() + "\\mnist\\"


def convert():
    labels = open(cwd + "t10k-labels.idx1-ubyte", "rb")
    images = open(cwd + "t10k-images.idx3-ubyte", "rb")
    csv = open("test-data.csv", "w")
    images.read(16)
    labels.read(8)
    
    outputs = []

    for i in range(10000):
        label = ord(labels.read(1))
        image = []
        for j in range(28*28):
            image.append(ord(images.read(1)))
        outputs += (label, image)
    
    for output in outputs:
        csv.write(",".join(str(p) for p in output)+ "\n")
    
    labels.close()
    images.close()
    csv.close()
    


convert()
