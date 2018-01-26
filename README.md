# YOLOv2 for Intel/Movidius Neural Compute Stick (NCS)

## Reference

> https://github.com/duangenquan/YoloV2NCS

*This project shows how to run tiny yolov2 (20 classes) with movidius stick:*
+ A python convertor from yolo to caffe
+ A c/c++ implementation and python wrapper for region layer of yolov2
+ A sample for running yolov2 with movidius stick in images or videos

---

# Updates
+ Refine output bboxes according to letterbox_image in YOLOV2, 01/03/2018, 01/12/2018 (Thanks nathiyaa!)
+ Support multiple sticks, 12/29/2017 (Thanks ichigoi7e!)
+ Process video in the sample, 12/15/2017 (Thanks ichigoi7e!)
+ Fix confident offset issues in nms, 12/12/2017

# How To Use
The following experiments are done on an Intel NUC with ubuntu 16.04.
	
### Step 1. Compile Python Wrapper
```make```

### Step 2. Convert Caffe to NCS
Download pre-trained [caffmodel](https://drive.google.com/open?id=1WXD6Pi47ryGPiTEtGeN4eDQsplgo35qm) , save at location ./models/caffemodels/yolo.caffemodel
```
mvNCCompile ./models/caffemodels/yolo.prototxt -w ./models/caffemodels/yolo.caffemodel -s 12
```
There will be a file *graph* generated as converted models for NCS.

### Step 3. Run tests
```	
python3 ./detectionExample/Main.py --image ./data/dog.jpg
```
This loads *graph* by default and results will be like this: 
![](/test.jpg)

# Run Other YoloV2 models
### Convert Yolo to Caffe 
```
Install caffe and config the python environment path.
sh ./models/convertyo.sh
```
Tips:

Please ignore the error message similar as "Region layer is not supported".

The converted caffe models should end with "prototxt" and "caffemodel".

### Update parameters

Please update parameters (biases, object names, etc) in ./src/CRegionLayer.cpp, and parameters (dim, blockwd, targetBlockwd, classe, etc) in ./detectionExample/ObjectWrapper.py.

Please read ./src/CRegionLayer.cpp and ./detectionExample/ObjectWrapper.py for details.

# References
+ [caffe](https://github.com/BVLC/caffe)
+ [yolo](https://github.com/pjreddie/darknet)
+ [caffe-yolo](https://github.com/xingwangsfu/caffe-yolo)
+ [yoloNCS](https://github.com/gudovskiy/yoloNCS)

---

# License
Research Only

# Author
duangenquan@gmail.com
