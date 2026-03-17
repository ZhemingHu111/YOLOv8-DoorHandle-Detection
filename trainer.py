import os

def run_train(model, opts):

    yaml_abs_path = os.path.abspath(opts['yaml_path'])
    
    print(f"--- Starting training from the following configuration file: {yaml_abs_path} ---")
    
    model.train(
        data=yaml_abs_path, 
        epochs=opts['epochs'],
        imgsz=opts['imgsz'],
        device='0'
    )