import os
from tkinter import ttk, filedialog, messagebox
from class_def import Cloth

types = ["topwear", "bottomwear", "footwear", "accessories"]
topwear = ['T-shirt', 'Long-sleeve shirt', 'Sweater', 'Jacket', 'Heavy jacket', 'Heavy winter coat']
bottomwear = ['Shorts', 'Pants']
footwear = ['Sandals', 'Sneakers', 'Boots']
accessories = ['Gloves', 'Scarf', 'Hat']
file_name = None
file_namelst = []
clothes = []

def check_upload(combo1, combo2, file_name):
    global clothes
    if combo1 != "type" and combo2 != "subtype":
        clothes.append(Cloth(file_name, combo1, combo2))

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

def upload_command():
    global file_namelst, file_name
    file_path = filedialog.askopenfilename(title="Upload the image here.", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        file_name = os.path.basename(file_path)
        if file_name not in file_namelst:
            file_namelst.append(file_name)
            save_path = os.path.join("pictures", file_name)
            with open(file_path, "rb") as f_in, open(save_path, "wb") as f_out:
                f_out.write(f_in.read())
            messagebox.showinfo(f"{file_name} has successfully uploaded.")
        else:
            messagebox.showerror("this filename already exists, please name it something else.")

def upload_image(frame):
    upload_frame = ttk.Frame(frame)
    upload_frame.pack(pady=65)
    ttk.Button(upload_frame, text="Select Image", command=upload_command).pack(pady=10)

def upload(frame):
    comboframe = ttk.Frame(frame)
    comboframe.pack(pady=30)
    imageframe = ttk.Frame(frame)
    imageframe.pack(pady=50)
    combo1, combo2 = upload_combo(comboframe)
    upload_image(imageframe)
    ttk.Button(frame, text="Upload", command=lambda:check_upload(file_name, combo1.get(), combo2.get())).pack(pady=10)