import display

import numpy as np
import matplotlib.pyplot as plt
import os

CWD = os.getcwd()



def main():
    print("main function")

def read_data(filename: str):
    with open(f"{CWD}//mnist//{filename}") as images_data:

        images_list = images_data.readlines()
        for image in images_list:
            image = image.strip()
        
        return images_list
        





if __name__ == "__main__":
    main()
