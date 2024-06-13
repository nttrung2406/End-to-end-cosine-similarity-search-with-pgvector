import sys
sys.path.append("C:/Users/flori/OneDrive/Máy tính/end_to_end_near_dupl_img_search")
from lib import *
from encode_clip import encode_images_to_tensors
from setup_connection import connect, data_file, setup_device, setup_model

image_folder = data_file()
image_names, image_tensors = encode_images_to_tensors(image_folder)
model = setup_model()
device = setup_device()
threshold=0.999999

def insert_tensors_to_db(image_names, image_tensors):
    conn = connect()
    cursor = conn.cursor()
    for name, tensor in zip(image_names, image_tensors):
        tensor = np.array(tensor).tolist()
        cursor.execute(
            "INSERT INTO image_tensors (name, tensor) VALUES (%s, %s)",
            (name, tensor)
        )
    
    conn.commit()
    cursor.close()
    conn.close()


def query_similar_images(query_name, query_tensor, threshold):
    conn = connect()
    cursor = conn.cursor()
    
    flattened_query_tensor = np.array(query_tensor).flatten().tolist()
    cursor.execute(
        "SELECT name, ROUND((1 - (tensor <-> %s::vector))::numeric, 7) AS similarity "
        "FROM image_tensors "
        "WHERE name != %s AND ROUND((1 - (tensor <-> %s::vector))::numeric, 7) > %s "
        "ORDER BY similarity DESC",
        (flattened_query_tensor, query_name, flattened_query_tensor, threshold)
    )
    
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


insert_tensors_to_db(image_names, image_tensors)

for image_name, query_tensor in zip(image_names, image_tensors):
    print(f"Querying for similar images to: {image_name}")
    similar_images = query_similar_images(image_name, query_tensor, threshold)
    
    for similar_image_name, similarity in similar_images:
        print(f"Image Name: {similar_image_name}, Similarity: {similarity:.2f}")
    print("-----")
