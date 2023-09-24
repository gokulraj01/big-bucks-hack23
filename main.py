import tkinter as tk
from PIL import Image, ImageTk
import cv2, sys, threading
import cv_pipeline

class CameraADAS:
    def __init__(self, vid):
        self.vid = vid
        self.fps = vid.get(cv2.CAP_PROP_FPS)
        self.frate = int(1000/self.fps)
        self.max_w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.max_h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.ratio_hw = self.max_h/self.max_w
        self.ndims = (self.max_w, self.max_h)
        self.running = True
        self.pot = cv_pipeline.YOLODetect("/home/gokul/yolov5/", "models/pothole_model/weights/best.pt", (0,0,255))
        self.hump = cv_pipeline.YOLODetect("/home/gokul/yolov5/", "models/speed_bump_model/weights/best.pt", (0,255,0))
        self.condn = cv_pipeline.RoadConditionDetect("models/road_condn_model/best.pt")
        self.condn_res = None

    def resizeVideoDims(self, nw, nh):
        ndim = min(self.max_w, nw), min(self.max_h, int(self.ratio_hw*nh))
        if not ndim[0] or not ndim[1]: self.ndims = (1,1)
        else: self.ndims = ndim

    def nextFrame(self):
        while self.vid.isOpened():
            ret, frame = self.vid.read()
            condn_res = self.condn.infer(frame)
            frame = self.pot.infer(frame)
            frame = self.hump.infer(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            return frame
        else:
            self.running = False
            return None
    
    def toImageTk(self, img):
        return ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, self.ndims)))

def windowConfig(event):
    adas.resizeVideoDims(event.width, event.height)

def process(adas, label):
    print("Thread started")
    while adas.running:
        tkimg = adas.toImageTk(adas.nextFrame())
        label.config(image=tkimg)
        label.photo = tkimg
        # Delay to maintain framerate of source video
        if cv2.waitKey(adas.frate) & 0xFF == ord('q'):
            exit(0)

# Driver Code
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERR] No video file provided!!")
        exit(0)
    
    # Configure the window
    root = tk.Tk()
    root.title("Camera ADAS")
    root.geometry("1920x1080")

    # Initialize Video Source and ADAS class
    vid = cv2.VideoCapture(sys.argv[1])
    adas = CameraADAS(vid)
    root.bind("<Configure>", windowConfig)
    tkimg = adas.toImageTk(adas.nextFrame())
    label = tk.Label(root, image=tkimg)
    label.photo = tkimg
    label.pack(side="left", fill="y")
    t = threading.Thread(target=process, args=(adas, label))
    t.daemon = 1
    t.start()
    root.mainloop()