import tkinter as tk
from tkinter import ttk
from core.display import display_images

imageframe = None

def display_command(frame, image_filenames):

    # dynamically dsiplay images based on window size
    def update_display(event=None):
        for widget in frame.winfo_children():
            widget.destroy()

        canvas = frame.master
        canvas_width = canvas.winfo_width()
        image_width = 200
        padding = 20
        actual_width = canvas_width - padding

        if actual_width < 200:
            image_perrow = 1
        else:
            image_perrow = actual_width // image_width


        cln, row = 0, 0
        if image_filenames:
            if not hasattr(frame, "images_cache"):
                frame.images_cache = display_images(image_filenames) ##only supporting png format

            for elm in frame.images_cache:
                label = ttk.Label(frame, image=elm)
                label.grid(column=cln, row=row, padx=1, pady=5)
                label.image = elm

                cln += 1
                if cln >= image_perrow:
                    cln = 0
                    row += 1


    frame.bind("<Configure>", update_display)
    frame.master.bind("<Configure>", update_display)
    frame.update_idletasks()  # Ensure frame dimensions are available
    update_display()



# refresh display used in upload tab after uploaded
def refresh_display(filename):
    global imageframe

    imageframe.images_cache.extend(display_images(filename))  # add new images to the cache
    # Update the display with the new cache
    display_command(imageframe, filename)



# display_tab created
def display(frame, filenames):
    ttk.Label(frame, text="Your Closet", font=("Arial", 20)).pack(pady=10)

    #canvas with scrollbar
    canvas = tk.Canvas(frame)
    canvas.pack(side='left', fill='both', expand=True)
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')
    canvas.config(yscrollcommand=scrollbar.set)

    #embed frame inside canvas
    global imageframe
    imageframe = ttk.Frame(canvas)
    canvas.create_window((0, 0), anchor='nw', window=imageframe)
    display_command(imageframe, filenames)

    #update canvas area if resized
    def update_scrollarea(event):
        canvas.configure(scrollregion = canvas.bbox("all"))
    imageframe.bind("<Configure>", update_scrollarea)

    # link touchpad and moushwheel activity with scrollbar
    def on_mousewheel(event):
        delta = event.delta if event.delta else -1
        canvas.yview_scroll(-1 * (delta // abs(delta)), "units")  # use sign only, ignore magnitude


    canvas.bind_all("<MouseWheel>", on_mousewheel)  
    canvas.bind_all("<Button-4>", on_mousewheel)   
    canvas.bind_all("<Button-5>", on_mousewheel)   
    # canvas.bind_all("<Command-MouseWheel>", on_mousewheel)

