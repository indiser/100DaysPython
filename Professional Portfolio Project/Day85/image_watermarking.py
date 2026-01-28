from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageDraw,Image,ImageFont,ImageTk
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import random
import sys


def font_style():
    font_list=[]
    font_dir = r"C:/Windows/Fonts"
    fonts = glob.glob(os.path.join(font_dir, "*.ttf"))
    for font in fonts:
        font_list.append(os.path.basename(font))
    
    return random.choice(font_list)

# image_path="C:/Users/ranab/OneDrive/Desktop/100Days Python/Professional Portfolio Project/Day85/puppy.jpg"

# def add_watermark(filename:str,outputfile:str):
#     try:
#         image = Image.open(filename)
#     except FileNotFoundError:
#         print("Error: Could not find 'puppy.jpg'. Check your file path.")
#         exit()

#     print("Please click on the image where you want the watermark...")
#     plt.imshow(image)
#     plt.title("Click exactly where you want the text!")

#     points = plt.ginput(1)
#     plt.close()

#     if points:
#         x, y = points[0]
#         x, y = int(x), int(y) # Convert to integers
#         print(f"You selected coordinates: ({x}, {y})")
#     else:
#         print("No click detected. Using center as default.")
#         w, h = image.size
#         x, y = int(w/2), int(h/2)

#     watermark_img=image.copy()

#     draw=ImageDraw.Draw(watermark_img)

#     font_size=int(min(image.size) / 10)

#     try:
#         font = ImageFont.truetype(font_style(), int(font_size))
#         print(f"The random font has been chosen as: {font_style()}")
#     except OSError:
#         print("Arial not found, using default font (Times New Roman Bold).")
#         font = ImageFont.truetype("timesbd.ttf", int(font_size))

#     draw.text((x,y),"Pups",fill=(255,255,255),font=font,anchor="ms")

#     plt.imshow(watermark_img)
#     plt.axis('off')
#     plt.title("Watermarked Image")
#     plt.show()

#     script_dir=os.path.dirname(os.path.abspath(__file__))
#     file_path=os.path.join(script_dir,outputfile)

#     watermark_img.save(file_path) 

# add_watermark(image_path,"watermarked_puppy.jpg")
# print("Done. Check your folder for 'watermarked_puppy.jpg'")

window=None
original_img = None
display_img = None
final_img = None
filepath = None
watermark_text_entry = None

preview_ratio = 1.0
offset_x = 0
offset_y = 0
watermark_coords = (0, 0)
selected_font_path = None

def select_file():
    global filepath, original_img
    filepath = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png")])
    
    if filepath:
        original_img = Image.open(filepath).convert("RGBA")
        editor()

def editor():
    global window, display_img, watermark_text_entry, preview_ratio, offset_x, offset_y
    window.withdraw()

    editor_panel=Toplevel()
    editor_panel.title("Watermark")
    editor_panel.geometry("800x600")
    editor_panel.configure(bg="#f0f2f5")
    editor_panel.protocol("WM_DELETE_WINDOW", lambda: sys.exit())

    toolbar = Frame(editor_panel, bg="white", pady=10)
    toolbar.pack(fill="x")

    Button(toolbar, text="Save Image", command=save_image, bg="#28a745", fg="white").pack(side="right", padx=10)

    watermark_text_entry = Entry(toolbar)
    watermark_text_entry.insert(0, "Default")
    watermark_text_entry.pack(side="right")

    Label(toolbar, text="Text:", bg="white").pack(side="right")

    canvas = Canvas(editor_panel, bg="#f0f2f5")
    canvas.pack(fill="both", expand=True, padx=20, pady=20)

    w, h = original_img.size

    new_w = 600
    preview_ratio = w / new_w

    aspect = w / h
    new_h = int(new_w / aspect)

    canvas_center_x = 400
    canvas_center_y = 300

    offset_x = canvas_center_x - (new_w // 2)
    offset_y = canvas_center_y - (new_h // 2)

    resized = original_img.resize((new_w, new_h))
    display_img = ImageTk.PhotoImage(resized)

    canvas.create_image(canvas_center_x, canvas_center_y, anchor="center", image=display_img)

    canvas.bind("<Button-1>", lambda event: add_watermark(event, canvas, resized))



def add_watermark(event, canvas, resized_preview):
    global display_img, original_img, final_img, selected_font_path, watermark_coords
    
    if watermark_text_entry is None:
        print("Error: Text entry not found")
        return
    
    rel_x = event.x - offset_x
    rel_y = event.y - offset_y

    watermark_coords = (rel_x, rel_y)

    # Get text
    text = watermark_text_entry.get()
    
    temp_img = resized_preview.copy()
    draw = ImageDraw.Draw(temp_img)

    font_size=int(min(temp_img.size)/10)

    if selected_font_path is None:
        selected_font_path = font_style()


    try:
        fonts = ImageFont.truetype(selected_font_path, int(font_size))
        print(f"The random font has been chosen as: {selected_font_path}")
    except OSError:
        print("Arial not found, using default font (Times New Roman Bold).")
        fonts = ImageFont.truetype("timesbd.ttf", int(font_size))
    
    draw.text((rel_x,rel_y), text,font=fonts ,fill="white", anchor="mm")
    
    # Update Display
    display_img = ImageTk.PhotoImage(temp_img)
    canvas.create_image(400, 300, anchor="center", image=display_img)


def save_image():
    global final_img, original_img, watermark_coords, selected_font_path, watermark_text_entry, preview_ratio

    save_path = filedialog.asksaveasfilename(
        initialfile="watermarked_image.png",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
    )

    if not save_path: return
    # if final_img is None:
    #     messagebox.showerror("Error", "You haven't placed a watermark yet!")
    #     return
    
    high_res_img = original_img.copy()
    draw = ImageDraw.Draw(high_res_img)

    real_x = int(watermark_coords[0] * preview_ratio)
    real_y = int(watermark_coords[1] * preview_ratio)

    base_size = int(min(high_res_img.size)/10)

    try:
        fonts = ImageFont.truetype(selected_font_path, int(base_size))
        print(f"The random font has been chosen as: {selected_font_path}")
    except OSError:
        print("Arial not found, using default font (Times New Roman Bold).")
        fonts = ImageFont.truetype("timesbd.ttf", int(base_size))
    
    text=watermark_text_entry.get()
    draw.text((real_x, real_y), text, font=fonts, fill="white", anchor="mm")

    high_res_img.save(save_path)
    messagebox.showinfo("Done", "Saved!")
    sys.exit()


window=Tk()

# 1st user will upload the image
window.title("Upload an image")
window.geometry("600x400")
window.config(bg="white")
frame=Frame(window,bg="white",padx=20,pady=20)
frame.pack(expand=True)
Label(frame, text="☁", font=("Arial", 50), bg="white", fg="#584e9c").pack()
Label(frame, text="Upload Image", font=("Arial", 16, "bold"), bg="white").pack()
btn = Button(frame, text="Select File", command=select_file, 
                    bg="#584e9c", fg="white", font=("Arial", 12), padx=20, pady=5)
btn.pack(pady=20)



window.mainloop()

