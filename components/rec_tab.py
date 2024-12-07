import random
from tkinter import ttk
from clothDecison import get_outfit
from display import display_images
from weather import get_weather
from class_def import filter 

rec_message, image_frame = None, None

def city_input(entry):
    city = entry.get()
    if city.strip():
        real_time, temp_c, temp_f , description = get_weather(city)
        return real_time, temp_c, temp_f, description

def rec_command(temp_f, clothes):
    outfit = get_outfit(temp_f)
    image_filenames = []
    for item in outfit:
        filtered = filter(clothes, item)
        if filtered:
            random_item = random.choice(filtered)
            image_filenames.append(random_item.filename)
    return image_filenames

def update_image(entry, clothes):
    real_time, temp_c, temp_f, description = city_input(entry)
    image_filenames = rec_command(temp_f, clothes)
    rec_message.config(text=f'Right now is {real_time}, with temperature is {temp_f}°F/{temp_c}°C, and {description}.')

    for widget in image_frame.winfo_children():
        widget.destroy()
    
    if image_filenames:
        images = display_images(image_filenames) ##only supporting png format
        for elm in images:
            label = ttk.Label(image_frame, image=elm)
            label.image = elm
            label.pack(padx=5, side='left')    

    

def rec(frame, clothes):
    #questframe for input
    quest_frame = ttk.Frame(frame)
    quest_frame.pack(pady=40)
    ttk.Label(quest_frame, text="where are you currently at?").pack(side='left')
    entry = ttk.Entry(quest_frame)
    entry.pack(side='left', padx=5)
    ttk.Button(quest_frame, text="Enter", command= lambda: update_image(entry, clothes)).pack(side='left')

    #recframe to display rec
    global rec_message, image_frame
    rec_frame = ttk.Frame(frame)
    rec_frame.pack(pady=10)
    rec_message = ttk.Label(rec_frame, text="")
    rec_message.pack(padx=30, side='top')
    #image frame to display mutiple images
    image_frame = ttk.Frame(rec_frame)
    image_frame.pack(pady=60)


