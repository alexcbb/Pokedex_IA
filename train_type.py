# Librairies à importer
import torch
from ultralytics import YOLO

if __name__ == '__main__':
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    model = YOLO('yolov8s-cls.pt')

    model.train(data='./../Type_Dataset', model='yolov8s-cls.pt', epochs=30, batch=256, imgsz=256, cache=True, workers=1, visualize=True)