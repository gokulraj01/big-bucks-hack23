from ultralytics import YOLO
def inferweather(input_img):
  #input_img(string) is the path to the image
  model=YOLO('<path to best.pt>')
  results=model.predict(source=input_img)
  #0-Dry 1-Wet
  result=[0]*2
  for strs in results:
    weath=strs.probs.cpu().numpy().top1
    conf=strs.probs.cpu().numpy().top1conf
    result[weath]=conf
    result[abs(weath-1)]=1-conf
    return result