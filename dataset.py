import os

def prepare_data(opts):
    
    image_path = opts['image_dir']
    

    content = f"""
train: {image_path}
val: {image_path}

nc: {opts.get('nc', 1)}
names: {opts.get('names', ['door_handle'])}
"""
    

    with open(opts['yaml_path'], 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"--- Down：data.yaml  ---")
    print(f"--- direction to ：{image_path} ---")