Yolo train script: yolo detect train model=yolov8n.pt data=Lunar_Craters/data.yaml epochs=10 imgsz=640 
Yolo predict script: yolo detect predict model=runs/detect/train/weights/best.pt source=tiles
Roboflow pretrained model: Lunar Crater Detection 2

