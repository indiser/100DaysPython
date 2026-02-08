from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

script_path=os.path.dirname(os.path.abspath(__file__))
filepath=os.path.join(script_path,"Gemini_Generated_Image_7omm3k7omm3k7omm.png")

def invert_color(filepath,savename:str):
    img=Image.open(filepath).convert("RGB")
    image_array=np.array(img,dtype=np.uint8)
    inverted_image=255-image_array
    inverted_image=Image.fromarray(inverted_image)
    inverted_image.save(os.path.join(script_path,savename))

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def get_palette(image_path, num_colors=10):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((150, 150))
    img_array = np.array(img)
    pixels = img_array.reshape(-1, 3)
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
    sorted_indices = np.argsort(counts)[::-1]
    top_colors = unique_colors[sorted_indices][:num_colors].tolist()
    tuple_of_colors=[tuple(color) for color in top_colors]
    return tuple_of_colors

def plot_colors(palette,hex_list):
    indices = range(len(palette))
    normalized_colors = [(r/255, g/255, b/255) for r, g, b in palette]

    fig, ax = plt.subplots(figsize=(12, 2)) # Wide and short
    ax.set_xlim(0, len(palette))
    ax.set_ylim(0, 1)
    ax.axis('off') # Turn off the ugly x/y axis numbers

    for i, color in enumerate(normalized_colors):
        rect = patches.Rectangle((i, 0), 1, 1, facecolor=color)
        ax.add_patch(rect)
        
        avg_brightness = sum(color) / 3
        text_color = 'black' if avg_brightness > 0.5 else 'white'
        
        ax.text(i + 0.5, 0.5, hex_list[i], 
                color=text_color, 
                fontsize=12, 
                ha='center', va='center', weight='bold')

    plt.title("Dominant Color Palette", fontsize=16)
    plt.show()


palette = get_palette(filepath)
hex_list=list(map(rgb_to_hex,palette))
invert_color(filepath,"Inverted.png")

print(f"RGB:{palette}")
print(f"HEX LIST:{hex_list}")

plot_colors(palette,hex_list)
