import os

"""
parameters:
    --output       The folder where the results will be saved (default: outputs).
    --extension    The extension of the images to segment (default: jpg).
    --images       Folder containing the images to segment.
    --model        Path to the trained model.
    --mode         Mode to be used, choose either `multiscale` or `sliding` for inference (multiscale is the default behaviour).
    --config       The config file used for training the model.
"""

if __name__ == "__main__" :
    
    config = "--config ./inference_data/config.json"
    model = "--model ./inference_data/best_model.pth"
    images = "--images ./inference_data/img"
    output = "--output ./inference_data/inference_output"

    os.system(f"python inference.py {config} {model} {images} {output}")
    
    print("[INFO] done!")