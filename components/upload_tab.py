import os
from tkinter import ttk, filedialog, messagebox
from core.class_def import Cloth
from core.json_func import upload_json


types = ["topwear", "bottomwear", "footwear", "accessories"]
topwear = ['T-shirt', 'Long-sleeve shirt', 'Sweater', 'Jacket', 'Heavy jacket', 'Heavy winter coat']
bottomwear = ['Shorts', 'Pants']
footwear = ['Sandals', 'Sneakers', 'Boots']
accessories = ['Gloves', 'Scarf', 'Hat']

pre_files, pre_clothes = None, None

def check_upload(file_name, combo1, combo2):
    global pre_files, pre_clothes
    clothes = []
    if combo1 != "type" and combo2 != "subtype":
        clothes.append(Cloth(file_name, combo2, combo1))
        upload_json(clothes, pre_files, pre_clothes)
    

def update_combo2(event, combo1, combo2):
    global topwear, bottomwear, footwear, accessories

    if combo1.get() == "topwear":
        combo2['values'] = topwear
    elif combo1.get() == "bottomwear":
        combo2['values'] = bottomwear
    elif combo1.get() == "footwear":
        combo2['values'] = footwear
    elif combo1.get() == "accessories":
        combo2['values'] = accessories
    

def upload_combo(frame):
    global types
    ttk.Label(frame, text="Please select the type and subtype of the cloth you are uploading.").pack(pady=10)
    cloth_type = ttk.Combobox(frame, values=types)
    cloth_type.pack(side='left', padx=5)
    cloth_type.set("type")
    cloth_subtype = ttk.Combobox(frame, values=types)
    cloth_subtype.pack(side='right', padx=5)
    cloth_subtype.set("subtype")
    cloth_type.bind("<<ComboboxSelected>>", lambda event: update_combo2(event, cloth_type, cloth_subtype))
    
    return cloth_type, cloth_subtype

def upload_command(combo1, combo2):
    global pre_files, pre_clothes
    file_path = filedialog.askopenfilename(title="Upload the image here.", filetypes=[("Image Files", "*.png")])
    if file_path:
        file_name = os.path.basename(file_path)
        if file_name not in pre_files:
            save_path = os.path.join("pictures", file_name)
            with open(file_path, "rb") as f_in, open(save_path, "wb") as f_out:
                f_out.write(f_in.read())
            messagebox.showinfo("Upload Success", f"{file_name} has successfully uploaded.")
            check_upload(file_name, combo1.get(), combo2.get())
        else:
            messagebox.showerror("File Exists","this filename already exists, please name it something else.")

def upload_image(frame, combo1, combo2):
    upload_frame = ttk.Frame(frame)
    upload_frame.pack(pady=65)
    ttk.Button(upload_frame, text="Select Image", command= lambda: upload_command(combo1, combo2)).pack(pady=10)

def upload(frame, filenames, clothes):
    global pre_files, pre_clothes
    pre_files, pre_clothes = filenames, clothes
    comboframe = ttk.Frame(frame)
    comboframe.pack(pady=30)
    imageframe = ttk.Frame(frame)
    imageframe.pack(pady=50)
    combo1, combo2 = upload_combo(comboframe)
    upload_image(imageframe, combo1, combo2)