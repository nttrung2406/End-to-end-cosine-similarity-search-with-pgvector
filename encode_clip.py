import sys
sys.path.append("Directory_path")
from lib import *
from setup_connection import setup_device, setup_model, data_file

model = setup_model()
device = setup_device()

def encode_images_to_tensors(image_folder):
    image_tensors = []
    image_names = []
    print("Encoding images...")
    for file_path in glob.glob(os.path.join(image_folder, '*')):
        if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            with torch.no_grad():
                image_names.append(file_path)
                encoded_image = model.encode([Image.open(filepath) for filepath in image_names], batch_size=128, convert_to_tensor=True, show_progress_bar=True, device=device)
                image_features = encoded_image.tolist()
                image_tensors.append(image_features[0])
                
    
    return image_names, image_tensors

# image_folder = data_file()
# image_names, image_tensors = encode_images_to_tensors(image_folder)
# print("Image names", image_names)
# print("Image tensors: ", image_tensors)
