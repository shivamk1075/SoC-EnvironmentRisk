import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import rasterio

source_root = 'data'
destination_root = 'task1'
target_width = 520
target_height = 561
footer_height = 20
legend_height = 30

try:
    font = ImageFont.truetype("arial.ttf", 14)
except:
    font = ImageFont.load_default()

legends = {
    "NDVI": [("brown", "Low"), ("yellow", "Medium"), ("green", "High")],
    "NDVI_Change": [("red", "Loss"), ("white", "No change"), ("green", "Gain")],
    "Urban": [("white", "Non-Urban"), ("red", "Urban")],
    "Urban_Growth": [("white", "No Change"), ("red", "Growth")],
    "Landuse": [
        ("#419bdf", "Water"), ("#397d49", "Trees"), ("#88b053", "Grass"),
        ("#7a87c6", "Flooded"), ("#e49635", "Crop"), ("#dfc35a", "Shrub"),
        ("#c4281b", "Built"), ("#a59b8f", "Bare"), ("#ffffff", "Snow")
    ],
    "Landuse_Change": [("red", "Loss"), ("white", "No change"), ("blue", "Gain")]
}

skip_keywords = ["Satellite"]

def get_legend_type(filename):
    for key in legends.keys():
        if key in filename and all(skip not in filename for skip in skip_keywords):
            return key
    return None

def draw_legend(draw, legend_items, top_y, spacing=5):
    x = 10
    for color, label in legend_items:
        draw.rectangle([x, top_y, x + 15, top_y + 15], fill=color)
        draw.text((x + 20, top_y), label, font=font, fill='black')
        x += 20 + draw.textlength(label, font=font) + spacing

for mine_folder in os.listdir(source_root):
    mine_path = os.path.join(source_root, mine_folder)
    if not os.path.isdir(mine_path):
        continue

    dest_mine_path = os.path.join(destination_root, mine_folder)
    os.makedirs(dest_mine_path, exist_ok=True)

    for file in os.listdir(mine_path):
        if not file.endswith('.tif'):
            continue

        tif_path = os.path.join(mine_path, file)
        png_path = os.path.join(dest_mine_path, file.replace('.tif', '.png'))

        with rasterio.open(tif_path) as src:
            arr = src.read()
            if arr.shape[0] == 3:
                arr = np.transpose(arr, (1, 2, 0))
            else:
                arr = arr[0]
                arr = np.stack([arr]*3, axis=-1)

            if arr.dtype != np.uint8:
                arr = ((arr - arr.min()) / (arr.max() - arr.min()) * 255).astype(np.uint8)

        image = Image.fromarray(arr)
        image_resized = image.resize((target_width, target_height))

        legend_key = get_legend_type(file)
        final_height = target_height + footer_height + (legend_height if legend_key else 0)

        final_img = Image.new("RGB", (target_width, final_height), (255, 255, 255))
        final_img.paste(image_resized, (0, 0))

        draw = ImageDraw.Draw(final_img)

        if legend_key:
            draw_legend(draw, legends[legend_key], target_height + 5)

        footer_y = final_height - footer_height
        text = os.path.splitext(file)[0].replace("_", " ")
        text_width = draw.textlength(text, font=font)
        draw.text(((target_width - text_width) // 2, footer_y), text, font=font, fill=(0, 0, 0))

        final_img.save(png_path)
        print(f"✅ Saved with legend/footer: {png_path}")

print("🎯 All images processed with legends (if applicable).")
