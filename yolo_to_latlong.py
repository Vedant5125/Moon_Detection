import os
import csv

# -------- INPUTS --------
labels_folder = "runs/detect/predict/labels"
tile_csv = "tile_positions.csv"

tile_size = 640

# Image size (from your GDAL output)
img_width = 12000
img_height = 65278

# OHRC coordinates (from your XML)
max_lat = -85.313377
min_lat = -84.574934
min_lon = 26.723277
max_lon = 31.180635

# -------- LOAD TILE POSITIONS --------
tile_positions = {}

with open(tile_csv, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tile_positions[row["tile_name"]] = (
            int(row["x_offset"]),
            int(row["y_offset"])
        )

# -------- PROCESS LABELS --------
output = []

for file in os.listdir(labels_folder):
    if file.endswith(".txt"):
        tile_name = file.replace(".txt", ".jpg")

        if tile_name not in tile_positions:
            continue

        x_offset, y_offset = tile_positions[tile_name]

        with open(os.path.join(labels_folder, file), "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 5:
                    continue

                _, x_center, y_center, w, h = map(float, parts[:5])

                # Convert to global pixel
                global_x = x_offset + (x_center * tile_size)
                global_y = y_offset + (y_center * tile_size)

                # Convert to lat/lon
                lat = max_lat - (global_y / img_height) * (max_lat - min_lat)
                lon = min_lon + (global_x / img_width) * (max_lon - min_lon)

                output.append([lat, lon])

# -------- SAVE CSV --------
with open("craters_latlong.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["latitude", "longitude"])
    writer.writerows(output)

print("✅ Conversion done → craters_latlong.csv")