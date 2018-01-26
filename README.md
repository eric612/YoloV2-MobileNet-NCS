# YOLOv2 for Intel/Movidius Neural Compute Stick (NCS)

## Reference

> https://github.com/duangenquan/YoloV2NCS

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
