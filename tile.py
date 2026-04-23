import cv2
import os
import csv

img = cv2.imread("moon_images/landing_area.png")
h, w, _ = img.shape

tile_size = 640
os.makedirs("tiles", exist_ok=True)

# Save tile positions
with open("tile_positions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["tile_name", "x_offset", "y_offset"])

    count = 0
    for y in range(0, h, tile_size):
        for x in range(0, w, tile_size):
            tile = img[y:y+tile_size, x:x+tile_size]

            if tile.shape[0] == tile_size and tile.shape[1] == tile_size:
                tile_name = f"tile_{count}.jpg"
                cv2.imwrite(f"tiles/{tile_name}", tile)

                # SAVE OFFSET (IMPORTANT 🔥)
                writer.writerow([tile_name, x, y])

                count += 1

print("Tiling done. Total tiles:", count)