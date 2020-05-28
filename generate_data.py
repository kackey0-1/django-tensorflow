from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

# parameter initialization
classes = ['car', 'motorbike']
num_classes = len(classes)
image_size = 150

# 画像の読み込みとNumpy配列への変換
X = [] 
Y = [] 

for index, classlabel in enumerate(classes):
    photos_dir = "./data/" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    print(photos_dir)
    for i, file in enumerate(files):
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        # トレーニングする上で、スコア向上のためデータの発散を防ぐ必要がある
        
        # Pillowを使って読み込む場合 0~255の濃淡値が各ピクセルに格納されている
        # 3色の場合は、各色ごとに濃淡値が格納されている
        # nuronetworkにこのまま導入すると値が極端にばらついてしまう
        # 255.0で割ることにより、0~1で推移する様にさせる
        data = np.asarray(image) / 255.0
        X.append(data)
        Y.append(index)        

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./imagefiles.npy", xy)
