import tkinter as tk
from tkinter import ttk
from class_def import Cloth
from components.rec_tab import rec
from components.upload_tab import upload
print("This is a test print statement.")



root = tk.Tk()
root.title("outfit recommender")
root.geometry("700x600")

greeting_label = tk.Label(root, text = "Welcome to outfit recommender!").pack(pady=30)
tab_container = ttk.Notebook(root)

#frame 3: upload clothes
upload_tab = ttk.Frame(tab_container)
tab_container.add(upload_tab, text="upload")
upload(upload_tab)


#frame 1: clothes display
display_tab = ttk.Frame(tab_container)
tab_container.add(display_tab, text="display")


#frame 2: recommendation
rec_tab = ttk.Frame(tab_container)
tab_container.add(rec_tab, text="recommend")
rec(rec_tab)







tab_container.pack(expand=True, fill="both")
root.mainloop()