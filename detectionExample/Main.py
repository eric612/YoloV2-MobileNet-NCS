import sys,os,time,csv,getopt,cv2,argparse
import numpy as np
from datetime import datetime

from ObjectWrapper import *
from Visualize import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--graph', dest='graph', type=str,
                        default='graph', help='MVNC graphs.')
    parser.add_argument('--image', dest='image', type=str,
                        default='./images/dog.jpg', help='An image path.')
    parser.add_argument('--video', dest='video', type=str,
                        default='./videos/car.avi', help='A video path.')
    args = parser.parse_args()

    network_blob=args.graph
    imagefile = args.image
    videofile = args.video

    detector = ObjectWrapper(network_blob)
    stickNum = ObjectWrapper.devNum

    if sys.argv[1] == '--image':
        # image preprocess
        img = cv2.imread(imagefile)
        start = datetime.now()
        size = (416,416) 
        shrink = (cv2.resize(img, size, interpolation=cv2.INTER_AREA)/255.0)
        im = shrink[:,:,(2,1,0)]
        #print(shrink)
        results = detector.Detect(im,img.shape[1],img.shape[0])

        end = datetime.now()
        elapsedTime = end-start

        print ('total time is " milliseconds', elapsedTime.total_seconds()*1000)

        imdraw = Visualize(img, results)
        cv2.imshow('Demo',imdraw)
        cv2.imwrite('test.jpg',imdraw)
        cv2.waitKey(10000)
    elif sys.argv[1] == '--video':
        # video preprocess
        cap = cv2.VideoCapture(videofile)
        fps = 0.0
        while cap.isOpened():
            start = time.time()
            imArr = {}
            results = {}
            for i in range(stickNum):
                ret, img = cap.read()
                if i not in imArr:
                    imArr[i] = img
            if ret == True:
                tmp = detector.Parallel(imArr)
                for i in range(stickNum):
                    if i not in results:
                        results[i] = tmp[i]
                    imdraw = Visualize(imArr[i], results[i])
                    fpsImg = cv2.putText(imdraw, "%.2ffps" % fps, (70, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
                    cv2.imshow('Demo', fpsImg)
                end = time.time()
                seconds = end - start
                fps = stickNum / seconds
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
