import os

def get_opts():

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "door_handle")
    
    opts = {

        "image_dir": os.path.join(desktop_path, "AI project image 2"),
        

        "label_dir": os.path.join(desktop_path, "obj_train_data"),
        

        "yaml_path": "./data.yaml",
        
        "model_type": "yolov8n.pt", 
        "epochs": 50,
        "imgsz": 640
    }
    return opts