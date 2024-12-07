import tkinter as tk
from tkinter import ttk
from display import display_images


def display_command(frame, image_filenames):
    for widget in frame.winfo_children():
        widget.destroy()

    image_perrow = 3
    if image_filenames:
        images = display_images(image_filenames) ##only supporting png format
        
        for i, elm in enumerate(images):
            row = i // image_perrow
            cln = i % image_perrow
            label = ttk.Label(frame, image=elm)
            label.grid(column=cln, row=row, padx=1, pady=5)
            label.image = elm

    #dynamically dsiplay images based on window size
    # def update_display(event):
    #     image_width = 200
    #     frame_width = frame.winfo_width()
    #     if frame_width < 200:
    #         image_perrow = 1
    #     else:
    #         image_perrow = frame_width // image_width

    # update_display(None)
    # # frame.bind("<Configure>", update_display)


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
    imageframe.bind("<Configure>", update_scrollarea)
    #why bind with imageframe

    # link touchpad and moushwheel activity with scrollbar
    def on_mousewheel(event):
        delta = event.delta if event.delta else -1 # Normalize for Button-4/5
        canvas.yview_scroll(-1 * (delta // abs(delta)), "units")  # Use sign only, ignore magnitude


    canvas.bind("<MouseWheel>", on_mousewheel)
    canvas.bind("<Button-4>", lambda event: canvas.yview_scroll(-1, 'units'))
    canvas.bind("<Button-5>", lambda event: canvas.yview_scroll(1, 'units'))

