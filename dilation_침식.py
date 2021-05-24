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
