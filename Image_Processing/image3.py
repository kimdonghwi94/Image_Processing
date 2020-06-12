# import matplotlib.pyplot as plt
# import matplotlib.image as img
# import numpy as np
# apple=img.imread('C:/Users/우쓰/PycharmProjects/untitled/data/batch1/test_mini/CNV/CNV-172472-224.jpeg')
# print(apple.shape)
# rgb=apple[:,:]
# num_bins=1000
# hist,x= np.histogram(rgb,bins=num_bins)
# sum_hist=[np.sum(hist[:i]) for i in range(len(hist))]
# plt.plot(sum_hist)
# plt.show()
# rgb_eq=np.copy(rgb)
# for i in range(1,num_bins):
#     idx= np.where( (rgb>x[i-1]) & (rgb < x[i]))
#     rgb_eq[idx] = sum_hist[i] / rgb.size
# hist_eq , x_eq= np.histogram(rgb_eq , bins=num_bins)
# plt.plot(x[1:], hist, 'r', label='original histo')
# plt.plot(x_eq[1:], hist_eq, '-b', label='eq histo')
# plt.show()
# plt.imshow(rgb)
# plt.show()
# plt.imshow(np.repeat(rgb_eq[:,:,np.newaxis]),3,axis=2)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


def erosion(img, mask_size, interations): #침식
    rows, cols = img.shape
    erosion_mask = np.ones((mask_size, mask_size), np.float32)
    guard = int((mask_size - 1) / 2)

    for i in range(interations):
        erosion_img = np.copy(img)
        for x in range(guard, rows - guard):
            for y in range(guard, cols - guard):
                erosion_img[x, y] = np.max(
                    img[x - guard:x - guard + mask_size, y - guard:y - guard + mask_size] * erosion_mask)
        img = erosion_img
    return img


def dilation(img, mask_size, interations):
    rows, cols = img.shape
    erosion_mask = np.ones((mask_size, mask_size), np.float32)
    guard = int((mask_size - 1) / 2)

    for i in range(interations):
        erosion_img = np.copy(img)
        for x in range(guard, rows - guard):
            for y in range(guard, cols - guard):
                erosion_img[x, y] = np.min(
                    img[x - guard:x - guard + mask_size, y - guard:y - guard + mask_size] * erosion_mask)
        img = erosion_img
    return img


# 검정배경
def image_binary(img, th):
    gray_img = np.where(img <= th, 0.0, 1.0)
    return gray_img