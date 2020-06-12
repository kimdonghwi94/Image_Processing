import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.image as img
# def loop(a):
#     b=[]
#     c=[]
#     for i in range(len(a)):
#         r=a[i]
#         start=time.time()
#         sq_y=np.ones((2*r,2*r,3))
#         sq_y[:,:,2]=0
#         certer_x=r
#         center_y=r
#         x=np.arange(2*r)
#         y=np.arange(2*r)
#         for i in x:
#             for j in y:
#                 if (i-certer_x)**2 + (j-center_y)**2 < r**2:
#                     sq_y[i,j,0:2]=0
#                     sq_y[i,j,2]=1
#         end_time=time.time()
#         t=end_time- start
#         b.append(t)
#         print('루프사용, 반지름이 : {} 일때, 시간 : {}sec '.format(r,t))
#
#         start=time.time()
#         sq_y=np.ones((2*r,2*r,3))
#         sq_y[:,:,2]=0
#         certer_x=r
#         center_y=r
#         x=np.arange(2*r).reshape(1,2*r)
#         y=np.arange(2*r).reshape(2*r,1)
#         x_sq=np.repeat(x,2*r,axis=0)
#         y_sq=np.repeat(y,2*r,axis=1)
#         dist=np.sqrt((x_sq-certer_x )**2 + (y_sq-center_y)**2)
#         idx=np.where(dist<=r)
#         x_idx=x_sq[idx]
#         y_idx=y_sq[idx]
#         sq_y[x_idx,y_idx,0:2]=0
#         sq_y[x_idx,y_idx,1]=1
#         end_time=time.time()
#         t=end_time- start
#         c.append(t)
#         print('루프사용 x, 반지름이 : {} 일때, 시간 : {}sec '.format(r,t))
#     plt.plot(a,b,label='with roop',marker='o')
#     plt.plot(a,c,label='Non roop',marker='x')
#     plt.xlabel('Radius[Pixel]')
#     plt.ylabel('Time[sec]')
#     plt.title('check')
#     plt.legend()
#     plt.show()
# a=list(map(int, input('숫자를 입력하세요').split()))
# loop(a)


# r = 200
# #With Loop
# start_time = time.time()
# sq_y = np.ones((2*r, 2*r, 3))
# sq_y[:,:,2] = 0
# center_x = r
# center_y = r
# x = np.arange(2*r)
# y = np.arange(2*r)
#
# for i in x:
#     for j in y:
#         if (i-center_x)**2 + (j-center_y)**2 < r**2:
#             sq_y[i,j,0:2] = 0
#             sq_y[i,j,2] = 1
# end_time = time.time()
# t = end_time - start_time
# print(f"Time W/ Loop:{t}")
#
# #Without Loop
# start_time = time.time()
# sq_y = np.ones((2*r, 2*r, 3))
# sq_y[:,:,2] = 0
# center_x = r
# center_y = r
# x = np.arange(2*r).reshape(1, 2*r)
# y = np.arange(2*r).reshape(2*r, 1)
# x_sq = np.repeat(x,2*r, axis = 0)
# y_sq = np.repeat(y, 2*r, axis = 1)
# dist = np.sqrt((x_sq - center_x)**2 + (y_sq - center_y)**2)
# idx = np.where(dist <= r)
# x_idx = x_sq[idx]
# y_idx = y_sq[idx]
# sq_y[x_idx, y_idx, 0:2] = 0
# sq_y[x_idx, y_idx, 1] = 1
# end_time = time.time()
# t = end_time - start_time
# print(f"Time W/O Loop:{t}")

#
#
#
# r = 200
# #With Loop
# start_time = time.time()
# sq_y = np.ones((2*r, 2*r, 3))
# sq_y[:,:,2] = 0
# center_x = r
# center_y = r
# x = np.arange(2*r)
# y = np.arange(2*r)
#
# for i in x:
#     for j in y:
#         if (i-center_x)**2 + (j-center_y)**2 < r**2:
#             sq_y[i,j,0:2] = 0
#             sq_y[i,j,2] = 1
# end_time = time.time()
# t = end_time - start_time
# print(f"Time W/ Loop:{t}")
#
# #Without Loop
# start_time = time.time()
# sq_y = np.ones((2*r, 2*r, 3))
# sq_y[:,:,2] = 0
# center_x = r
# center_y = r
# x = np.arange(2*r).reshape(1, 2*r)
# y = np.arange(2*r).reshape(2*r, 1)
# x_sq = np.repeat(x,2*r, axis = 0)
# y_sq = np.repeat(y, 2*r, axis = 1)
# dist = np.sqrt((x_sq - center_x)**2 + (y_sq - center_y)**2)
# idx = np.where(dist <= r)
# x_idx = x_sq[idx]
# y_idx = y_sq[idx]
# sq_y[x_idx, y_idx, 0:2] = 0
# sq_y[x_idx, y_idx, 1] = 1
# end_time = time.time()
# t = end_time - start_time
apple=img.imread('/home/kim/PycharmProjects/tensorflow2.0-gpu/1.png')
print(apple)

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