import tkinter as tk
from tkinter import ttk
from components.display_tab import display
from components.rec_tab import rec
from components.upload_tab import upload
from core.json_func import read_json
import ttkbootstrap as ttk

#create app window
root=ttk.Window(themename='cosmo')
filenames, clothes = read_json()

root.title("outfit recommender")
root.geometry("850x600")

greeting_label = ttk.Label(root, text="Welcome to Outfit Recommender!", font=("Arial",16 ,"bold"))  # 修改：使用 ttk.Label
greeting_label.pack(pady=30)
tab_container = ttk.Notebook(root)



#frame 1: clothes display
display_tab = ttk.Frame(tab_container)
tab_container.add(display_tab, text="display")
display(display_tab, filenames)

#frame 2: recommendation
rec_tab = ttk.Frame(tab_container)
tab_container.add(rec_tab, text="recommend")
rec(rec_tab, clothes)

#frame 3: upload clothes
upload_tab = ttk.Frame(tab_container)
tab_container.add(upload_tab, text="upload")
upload(upload_tab, filenames, clothes)



tab_container.pack(expand=True, fill="both")
root.mainloop()