from ultralytics import YOLO

def get_model(model_name):
    return YOLO(model_name)