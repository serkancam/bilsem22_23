import cv2
from keras import models
import numpy as np

model_adresi="/home/serkan/Belgeler/yillar/2022-2023/bilsem22_23/2022-oyg2-a1/yapay_zeka/mnist_ann_model.h5"
resim_adres="/home/serkan/Belgeler/yillar/2022-2023/bilsem22_23/2022-oyg2-a1/yapay_zeka/rakam8_2.png"

ysa=models.load_model(model_adresi)
resim=cv2.imread(resim_adres)

resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)#opencv bgr olarak renkleri tutuyor
# print(resim)
resim_gri=cv2.bitwise_not(resim_gri)
rakam = resim_gri.astype("float32")/255
rakam=rakam.reshape((-1,28*28))
tahmin=ysa.predict(rakam)

i=0
for t in tahmin[0,:]:
    print(str(i),"için tahmin",t)
    i=i+1

# print(np.argmax(tahmin))
# cv2.imshow("resim_gri",resim_gri)

# cv2.waitKey(0)
# cv2.destroyAllWindows()