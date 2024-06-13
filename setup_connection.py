import sys
sys.path.append("Directory_path")
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
    image_folder = "folder_path"
    return os.path.join(image_folder)
