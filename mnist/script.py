import gzip
import numpy as np
import matplotlib.pyplot as plt

with open(f"{__file__}\..\\t10k-labels-idx1-ubyte.gz", "rb") as labels, open(f"{__file__}\..\\t10k-images-idx3-ubyte.gz", "rb") as images:
    imgs, lbls = images.read(), labels.read()
    imgs = gzip.decompress(imgs)
    lbls = gzip.decompress(lbls)



print(lbls[0:40].decode())