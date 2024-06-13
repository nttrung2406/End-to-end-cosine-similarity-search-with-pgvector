import sys
sys.path.append("C:/Users/flori/OneDrive/Máy tính/end_to_end_near_dupl_img_search")
from lib import *

def connect():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="0982666066"
    )

    return connection

def setup_device():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    return device

def setup_model():
    model = SentenceTransformer('clip-ViT-B-32')
    return model

def data_file():
    image_folder = "C:/Users/flori/OneDrive/Máy tính/Tai-lieu/end_to_end_near_dupl_img_search/image"
    return os.path.join(image_folder)