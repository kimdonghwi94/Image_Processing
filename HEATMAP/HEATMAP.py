import keras
from keras.preprocessing import image
import numpy as np
import keras.backend as K
import cv2
model = keras.models.load_model('불러올모델경로 /DenseNet121_allfine_5')#DenseNet121_allfine_5
path='입력이미지 경로 '
make_name='./생성할이미지'
def Heatmap(model,path):
    img = image.load_img(path, target_size=(model.input.shape[1],model.input.shape[2]))
    img=np.array(img)
    img_tensor = img.reshape((1,model.input.shape[1],model.input.shape[2], 3))
    img_tensor = img_tensor / 255
    prediction=model.predict(img_tensor)
    y_pred=np.argmax(prediction)    # Get_Image_Predic
    hypothesis=model.output[:,y_pred]
    Last_conv_Layer=model.get_layer('conv5_block16_2_conv')    #Get Last Layer
    Gradients=K.gradients(hypothesis,Last_conv_Layer.output)[0]#Get y_predic gradi from Last_Layer
    pooled_grad=K.mean(Gradients,axis=(0,1,2))# Get gradients Average
    iterate=K.function([model.input],[pooled_grad,Last_conv_Layer.output[0]]) # Get output
    pooled_grad_value,conv_layer_value=iterate([img_tensor]) # input to original image-> get 2 numpy
    for i in range(pooled_grad.shape[0]):
        conv_layer_value[:,:,i]*=pooled_grad_value[i]# important feature square
    heatmap=np.mean(conv_layer_value,axis=-1) #average
    heatmap=np.maximum(heatmap,0)
    heatmap/=np.max(heatmap)
    return heatmap,prediction,y_pred #히트맵 , % , 결과
def get_heat_map(heatmap,path,make_path):
    img = cv2.imread(path)
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    Finist = heatmap * 0.3 + img
    cv2.imwrite('./{}'.format(make_path), Finist)
    return Finist
if __name__=='__main__':
    # 히트맵 , % , 결과       = Heatmap(불러올 모델 , 입력이미지 경로 )
    heatmap,prediction,y_pred=Heatmap(model, path)
    #            ( 히트맵, 입력이미지 경로, 만들이미지 이름  )
    get_heat_map(heatmap,path,make_name)
