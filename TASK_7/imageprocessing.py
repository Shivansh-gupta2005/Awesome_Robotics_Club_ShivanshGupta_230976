import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.filters import gaussian

image_path = r"C:\\Users\\shiva\\OneDrive\\Pictures\\navigationtask.jpg"
image = io.imread(image_path)
gray_image = color.rgb2gray(image)
filtered_image = gaussian(gray_image, sigma=1)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(gray_image, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(filtered_image, cmap='gray')
ax[1].set_title('Filtered Image (Gaussian)')
plt.show()

