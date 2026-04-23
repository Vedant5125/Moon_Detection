import os
import pandas as pd

labels_path = "runs/detect/predict2/labels"

rows = []

for file in os.listdir(labels_path):
    if file.endswith(".txt"):
        tile = file.replace(".txt","")

        with open(os.path.join(labels_path,file)) as f:
            for line in f.readlines():
                cls, x, y, w, h = map(float, line.split())

                rows.append({
                    "tile": tile,
                    "x_center": x,
                    "y_center": y,
                    "width": w,
                    "height": h,
                    "type": "crater"
                })

df = pd.DataFrame(rows)
df.to_csv("crater_detections.csv", index=False)

print("CSV created!")