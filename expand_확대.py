
dir = '/home/kim/PycharmProjects/tensorflow2.0-gpu/lenna1.png'
a = img.imread(dir)
def expand(image,n):
    c = np.zeros((int(image.shape[0] * n), (image.shape[1] * n)))
    for i in range(image.shape[0] ):
        for j in range(image.shape[1]):
            c[i*n:i*n+n,j*n:j*n+n]=image[i,j,0]
    plt.imshow(image)
    plt.title('original')
    plt.show()
    plt.imshow(c,cmap='gray')
    plt.title('expand')
    plt.show()
expand(이미지, 확대시킬사이즈)
