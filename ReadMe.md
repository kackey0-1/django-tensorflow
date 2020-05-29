# Django x Tensorflow

> 車、バイクの推定を行うAI

0. 必要なライブラリインストール

```bash
pip install -r requrements.txt
```

1.　画像ファイルの収集

```bash
python download.py car
python download.py motorbike
```

2. 学習用データ作成

```bash
python generate_data_244.py
```

3. 学習

```bash
python vgg16_transfer.py
```

4. モデルデータ配置

```bash
mv vgg16_transfer.h5 aiapps/imageai/ml_models/
```

5. Django起動

```bash
# localhost:8000にて起動
cd aiapps ; python manage.py runserver
```




