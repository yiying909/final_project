import tkinter as tk
from tkinter import ttk
from core.display import display_images

imageframe = None

def display_command(frame, image_filenames):

    # #dynamically dsiplay images based on window size
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

# 思路：1 把事件绑定在frame上，当frame大小改变时，触发update_display函数
# 2 在update_display函数中，根据frame的宽度计算每行显示的图片数量
# 3 在update_display函数中，根据计算出的图片数量，更新frame上的图片显示 
# 拓展：debounced函数的作用是为了防止频繁触发事件，导致加载卡顿
# debounced的作用是当事件触发时，设置一个定时器，在定时器结束前，如果事件再次触发，则重新设置定时器，直到定时器结束，事件处理函数被执行
# 那也就是说，当用户一直频繁改动窗口的时候，事件函数不会被执行，只有当用户停下来到延迟的时间的时候，事件函数才会被执行
# def display_command(frame, image_filenames):
#     # 防抖定时器
#     resize_timer = None
#     DEBOUNCE_TIME = 150  # 防抖延迟时间（毫秒）
    
#     def update_display(event=None):
#         for widget in frame.winfo_children():
#             widget.destroy()
            
#         # 获取真实的canvas宽度
#         canvas = frame.master
#         canvas_width = canvas.winfo_width()
#         image_width = 200
#         padding = 20
        
#         # 确保宽度计算正确
#         available_width = canvas_width - padding
#         image_perrow = max(1, available_width // image_width)
        
#         # 重新布局图片
#         cln, row = 0, 0
#         if image_filenames:
#             if not hasattr(frame, 'cached_images'):
#                 frame.cached_images = display_images(image_filenames)
            
#             for elm in frame.cached_images:
#                 label = ttk.Label(frame, image=elm)
#                 label.grid(column=cln, row=row, padx=1, pady=5)
#                 label.image = elm

#                 cln += 1
#                 if cln >= image_perrow:
#                     cln = 0
#                     row += 1

#     def debounced_update(event=None):
#         nonlocal resize_timer
#         # 如果已经有定时器在运行，取消它
#         if resize_timer is not None:
#             frame.after_cancel(resize_timer)
#         # 设置新的定时器
#         resize_timer = frame.after(DEBOUNCE_TIME, lambda: update_display(event))

#     # 绑定窗口大小改变事件
#     frame.bind("<Configure>", debounced_update)
#     frame.master.bind("<Configure>", debounced_update)
    
#     # 初始显示
#     frame.update_idletasks()
#     update_display()



def refresh_display(filenames):
    if imageframe:
        for widget in imageframe.winfo_children():
            widget.destroy()
        display_command(imageframe, filenames)


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
    #why bind with imageframe

    # link touchpad and moushwheel activity with scrollbar
    def on_mousewheel(event):
        delta = event.delta if event.delta else -1 # Normalize for Button-4/5
        canvas.yview_scroll(-1 * (delta // abs(delta)), "units")  # Use sign only, ignore magnitude


    canvas.bind_all("<MouseWheel>", on_mousewheel)  
    canvas.bind_all("<Button-4>", on_mousewheel)   
    canvas.bind_all("<Button-5>", on_mousewheel)   
    # canvas.bind_all("<Command-MouseWheel>", on_mousewheel)

