def sharp(out,mask_size):
    medium = mask_size // 2
    mask2 = -(mask_size * 2) * (np.ones((mask_size, mask_size)))
    mask2[medium, medium] = (np.sum(mask2) * -1) * 2
    mask2 = mask2 / np.sum(mask2)
    out1 = np.copy(out)
    guard = int((mask_size - 1) / 2)
    for i in range(guard, lenna.shape[0] - guard):
        for j in range(guard, lenna.shape[1] - guard):
            out1[i, j] = np.sum(mask2 * out[i-guard:i + guard+1, j-guard:j + guard+1])
    return out1
 sharp(이미지, filter_size)
