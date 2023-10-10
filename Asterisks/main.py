import numpy as np
from scipy.ndimage import binary_erosion
from skimage.measure import label
import matplotlib.pyplot as plt


plus_mask = np.array([[0,0,1,0,0],
                      [0,0,1,0,0],
                      [1,1,1,1,1],
                      [0,0,1,0,0],
                      [0,0,1,0,0]])

cross_mask = np.array([[1,0,0,0,1],
                       [0,1,0,1,0],
                       [0,0,1,0,0],
                       [0,1,0,1,0],
                       [1,0,0,0,1]])

f = np.load('stars.npy')


def get_count_object(file, mask):
    return label(binary_erosion(file, mask)).max()


def show_image(file):
    plt.imshow(file)
    plt.show()
    


plus = get_count_object(f, plus_mask)
cross = get_count_object(f, cross_mask)

print("Count pluses: " + str(plus))
print("Count crosses: " + str(cross))
