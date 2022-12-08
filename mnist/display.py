import numpy as np
import matplotlib.pyplot as plt

def display_image(image: str):
    image = image.split(",")
    prediction = image.pop(0)
    image_array = np.asfarray(image[:]).reshape((28,28))
    plt.imshow(image_array, cmap="Greys", interpolation="None")
    plt.show()

    

