import os, torch, cv2
from ultralytics import YOLO

class YOLODetect:
    def __init__(self, yolov5_path:str, weights:str, color=(0,0,255)):
        self.model = torch.hub.load(yolov5_path, 'custom', path=weights, source='local')
        self.color = color

    def infer(self, img, confidence=0.2, thickness=1):
        result = self.model(img)
        # result = result.filter(conf=confidence)
        for det in result.pred[0]:
            det = det.cpu()
            if det[4] > confidence:
                xmin, ymin, xmax, ymax, conf, cls = det.numpy().astype(int)
                img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), self.color, thickness)
        return img

class RoadConditionDetect:
    def __init__(self, weights:str):
        self.model = YOLO(weights)

    # 0 - Dry, 1 - Wet
    def infer(self, img):
        pred_results = self.model.predict(source=img)
        result = [0]*2
        for strs in pred_results:
            weath = strs.probs.cpu().numpy().top1
            conf = strs.probs.cpu().numpy().top1conf
            result[weath] = conf
            result[abs(weath-1)] = 1-conf
        return result

if __name__ == "__main__":
    img_dir = "infer_test"
    imgs = os.listdir(img_dir)
    pot = YOLODetect("/home/gokul/yolov5/", "models/pothole_model/weights/best.pt", (0,0,255))
    hump = YOLODetect("/home/gokul/yolov5/", "models/speed_bump_model/weights/best.pt", (0,255,0))

    for imgpath in imgs:
        img = cv2.imread(f"{img_dir}/{imgpath}")
        pot.infer(img, thickness=2)
        hump.infer(img, thickness=2)
        cv2.imshow('Bounding Box', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
            