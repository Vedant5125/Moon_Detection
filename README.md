Yolo train script: yolo detect train model=yolov8n.pt data=Lunar_Craters/data.yaml epochs=10 imgsz=640 
Yolo predict script: yolo detect predict model=runs/detect/train/weights/best.pt source=tiles
Roboflow pretrained model: Lunar Crater Detection 2

Current trained on epochs=10

tile_position.csv has size of tile. Each tile is broken down into size n from main image .
craters_latlong.csv has actual coordinates of cratersnon main image. Its made with help of runs/detect/predict/labels which contains normalised values of position of crater on tile and the tile_position.csv .

