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

### Training project 

[Caffe-YOLOv2-Windows](https://github.com/eric612/Caffe-YOLOv2-Windows)

The result was not optimization , still trying now .

