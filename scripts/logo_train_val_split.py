import os
import random


def main():
    datasetDir = '/home/zhangjiazhao/projects/tensorflow-yolov3-master/data/logo_dataset/JPEGImages'
    trainFile = '/home/zhangjiazhao/projects/tensorflow-yolov3-master/data/logo_dataset/ImageSets/Main/train.txt'
    valFile = '/home/zhangjiazhao/projects/tensorflow-yolov3-master/data/logo_dataset/ImageSets/Main/val.txt'
    train = open(trainFile, 'w')
    val = open(valFile, 'w')

    for image in os.listdir(datasetDir):
        imageName = image.split('.')[0]
        if random.uniform(0, 1) < 0.8:
            train.write(imageName + '\n')
        else:
            val.write(imageName + '\n')

    train.close()
    val.close()


if __name__=='__main__':
    main()