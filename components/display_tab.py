import tkinter as tk
from tkinter import ttk
from display import display_images


def display_command(frame, image_filenames):
    image_perrow = 5
    for widget in frame.winfo_children():
        widget.destroy()
    
    if image_filenames:
        images = display_images(image_filenames) ##only supporting png format
    
        for i, elm in enumerate(images):
            row = i // image_perrow
            cln = i % image_perrow
            label = ttk.Label(frame, image=elm)
            label.grid(column=cln, row=row, padx=1, pady=5)
            label.image = elm



def display(frame, filenames):
    ttk.Label(frame, text="Your Closet", font=("Arial", 10)).pack(pady=10)

    #canvas with scrollbar
    canvas = tk.Canvas(frame)
    canvas.pack(side='left', fill='both', expand=True)
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')
    canvas.config(yscrollcommand=scrollbar.set)

    #embed frame inside canvas
    imageframe = ttk.Frame(canvas)
    canvas.create_window((0, 0), anchor='nw', window=imageframe)
    display_command(imageframe, filenames)

    #update canvas area if resized
    def update_scrollarea(event):
        canvas.configure(scrollregion = canvas.bbox("all"))
    canvas.bind("<Configure>", update_scrollarea)