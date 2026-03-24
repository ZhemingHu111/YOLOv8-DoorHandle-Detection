import os

def get_opts():
    image_dir = r"C:\Users\Boom\Desktop\door_handle\AI project image 2"
    label_dir = r"C:\Users\Boom\Desktop\door_handle\obj_train_data"
    
    opts = {
        "image_dir": image_dir,
        "label_dir": label_dir,
        "yaml_path": "data.yaml",
        "model_type": "yolov8n.pt",
        "epochs": 50,
        "imgsz": 640,
        "nc": 1,
        "names": ['door_handle']
    }
    return opts