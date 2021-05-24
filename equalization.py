import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
apple=img.imread('C:/Users/우쓰/PycharmProjects/untitled/apple.png')
print(apple.shape)

rgb=apple[:,:,0:3]
num_bins=1000

hist,x= np.histogram(rgb,bins=num_bins)
sum_hist=[np.sum(hist[:i]) for i in range(len(hist))]

plt.plot(sum_hist)
plt.show()
rgb_eq=np.copy(rgb)
for i in range(1,num_bins):

    idx= np.where( (rgb>x[i-1]) & (rgb < x[i]))
    rgb_eq[idx] = sum_hist[i] / rgb.size

hist_eq , x_eq= np.histogram(rgb_eq , bins=num_bins)

plt.plot(x[1:], hist, 'r', label='original histo')
plt.plot(x_eq[1:], hist_eq, '-b', label='eq histo')
plt.show()

plt.imshow(rgb)
plt.show()

plt.imshow(rgb_eq)
plt.show()
