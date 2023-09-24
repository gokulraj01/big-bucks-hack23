# import tkinter as tk
# from tkinter import filedialog
# # from tkVideoPlayer import TkinterVideo 
# from tkvideo import tkvideo
# import numpy as np
# import cv2 as cv
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()


# # Code to add widgets will go here...
# window=App()
# window.title("hey")
# window.geometry("11000x2300") 

# file_path="video.mp4"


# frame=tk.Frame(window)
# frame.grid(row=0, column=0)

# # vidplayer = TkinterVideo(window,scaled=True)
# # if (file_path):
# #     vidplayer.load(file_path)

# videoPlayer = tk.Label(window)
# videoPlayer.grid(row=0,column=0)
# video = tkvideo("video"+ ".mp4", videoPlayer, loop=0, size=(1500,1080))
# video.play()


# window.mainloop()





import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import cv2 as cv
import random as ran
# Function to open a video file
def open_video():
    file_path="video2.mp4"
    if file_path:
        cap = cv.VideoCapture(file_path)
        play_video(cap)

# Function to play the video with an OpenCV effect
def play_video(cap):
    print(cap.get(cv.CAP_PROP_FPS))
    while cap.isOpened():
        a=ran.random()
        ret, frame=cap.read()
        org=(00,185)
        # Red color in BGR
        color = (0, 0, 255)
        font = cv.FONT_HERSHEY_SIMPLEX
        # cv.setWindowTitle(	cap, 'New'	)
        cv.putText(frame, f"Required Speed: {a} ", org, font, 1, color,2)
        cv.putText(frame, f"Type Of Terrain: {a} ", (00,285), font, 1, color,2)
        cv.rectangle(frame,(00,100),(300,300),(88,16,13))
        # Apply an OpenCV effect (e.g., grayscale)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow('Testing', frame)

        # Check for key presses and exit on 'q'
        key = cv.waitKey(1)
        if key == ord('q') or cv.getWindowProperty('Testing', cv.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv.destroyAllWindows()

# Create the main window
root = tk.Tk()
root.title("Video Editor")
root.geometry("10700x1020")
# style = ttk.Style()
# style.configure("Custom.TFrame", background="lightblue")  # Define your color theme
# frame1=ttk.Frame(root,style="Custom.TFrame", width=1300, height=1400, relief=tk.RAISED, borderwidth=1)

# frame1.config(width=1300, height=1400)
# frame1.pack(side="left")
# # Create a button to open a video file
# open_button = ttk.Button(frame1, text="Play Demo Video", command=open_video)
# open_button.pack(padx=500, pady=0)

# Create a frame for the left side (50% of the screen)
left_frame = tk.Frame(root, width=root.winfo_width() // 2, bg="lightblue")
left_frame.pack_propagate(False)  # Prevent the frame from shrinking
left_frame.pack(side="left", fill="both", expand=True)

# Create a button in the center of the left frame
button = tk.Button(left_frame, text="Centered Button", command=open_video)
button.pack(expand=True, padx=20, pady=20)  # Add padding for centeri

###########

# Create a frame for the right side (50% of the screen)
right_frame = tk.Frame(root, bg="lightgray")
right_frame.pack(side="left", fill="both", expand=True)
speed=0
# Add components to the right frame (stacked vertically)
label1 = tk.Label(right_frame, text=f"Recommended Speed: {speed}", font=("Helvetica", 21), background='lightblue')
label1.pack(pady=10)

label2 = tk.Label(right_frame, text=f"Recommended Speed: {speed}", font=("Helvetica", 21), background='lightblue')
label2.pack(pady=10)

entry = tk.Entry(right_frame)
entry.pack(pady=10)
entry.config(width=50)
# entry.config()3




# Run the Tkinter main loop
root.mainloop()
