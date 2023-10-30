Running Procedure
1、测试.pt模型文件
  1.在pycharm里打开下载的yolov5环境，在根目录打开runs文件，找到trains文件中的best_1.pt即为训练最优模型。
  2.在根目录找到detect.py文件，修改代码221行默认路径至模型路径，222行路径更改至所需测试图片路径，点击运行。
2、测试.onnx模型文件
  1.在pycharm里打开下载的yolov5环境，在根目录打开export.py文件，修改默认输出模型类型为onnx，选择best_1.pt输入模型，点击运行。
  2.在根目录找到detect.py文件，修改代码221行默认路径至模型路径，222行路径更改至所需测试图片路径，点击运行。
  
