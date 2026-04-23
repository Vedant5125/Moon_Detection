import cv2
import os

img = cv2.imread("moon_images/landing_area.png")
h, w, _ = img.shape

tile_size = 640
os.makedirs("tiles", exist_ok=True)

count = 0
for y in range(0, h, tile_size):
    for x in range(0, w, tile_size):
        tile = img[y:y+tile_size, x:x+tile_size]
        if tile.shape[0] == tile_size and tile.shape[1] == tile_size:
            cv2.imwrite(f"tiles/tile_{count}.jpg", tile)
            count += 1

print("Tiling done. Total tiles:", count)
