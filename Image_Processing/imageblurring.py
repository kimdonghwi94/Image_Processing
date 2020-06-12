import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
# lenna1 = img.imread('/home/kim/PycharmProjects/tensorflow2.0-gpu/donghwikim/imageclass/lenna1.png')
# lenna = lenna1[:, :, 0]
# print(lenna1)
# def blurring(lenna,mask_size):
#     mask1 = np.ones((mask_size, mask_size)) / mask_size ** 2
#     guard = int((mask_size - 1) / 2)
#     out = np.copy(lenna)
#     for i in range(guard, lenna.shape[0] - guard):
#         for j in range(guard, lenna.shape[1] - guard):
#             out[i, j] = np.sum(mask1 * lenna[i-guard:i + guard+1, j-guard:j + guard+1])
#     return out
# def sharp(out,mask_size):
#     medium = mask_size // 2
#     mask2 = -(mask_size * 2) * (np.ones((mask_size, mask_size)))
#     mask2[medium, medium] = (np.sum(mask2) * -1) * 2
#     mask2 = mask2 / np.sum(mask2)
#     out1 = np.copy(out)
#     guard = int((mask_size - 1) / 2)
#     for i in range(guard, lenna.shape[0] - guard):
#         for j in range(guard, lenna.shape[1] - guard):
#             out1[i, j] = np.sum(mask2 * out[i-guard:i + guard+1, j-guard:j + guard+1])
#     return out1
# out=blurring(lenna,5)
# out1=sharp(out,5)
# out2=sharp(lenna,5)
#
# plt.imshow(lenna1, cmap='gray')  # 원본
# plt.show()
# plt.imshow(out, cmap='gray')  # 흐릿하게한것
# plt.show()
# plt.imshow(out1, cmap='gray')  # 흐릿하게 한거에서 선명하게
# plt.show()
# plt.imshow(out2,cmap='gray') #원본에서 선명하게
# plt.show()

lenna1 = img.imread('/home/kim/PycharmProjects/tensorflow2.0-gpu/donghwikim/imageclass/sepo.png')
lenna = lenna1[:, :, 0]
def erosion(lenna,mask_size): #침식
    mask1 = np.ones((mask_size, mask_size),np.float32)
    guard = int((mask_size - 1) / 2)
    out = np.copy(lenna)

    for i in range(guard, lenna.shape[0] - guard):
        for j in range(guard, lenna.shape[1] - guard):
            out[i, j] = np.max(lenna[i - guard:i + guard + 1, j - guard:j + guard + 1] * mask1)
        lenna=out
    return lenna
erosion(lenna,2)
plt.imshow(lenna, cmap='gray')  # 원본
plt.show()

def erosion(img, mask_size, interations): #침식
    rows, cols = img.shape
    erosion_mask = np.ones((mask_size, mask_size), np.float32)
    guard = int((mask_size - 1) / 2)

    for i in range(interations):
        erosion_img = np.copy(img)
        for x in range(guard, rows - guard):
            for y in range(guard, cols - guard):
                erosion_img[x, y] = np.max(img[x - guard:x - guard + mask_size, y - guard:y - guard + mask_size] * erosion_mask)
        img = erosion_img
    return img

def dilation(img, mask_size, interations): #팽창
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

