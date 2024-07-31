# End to end cosine similarity search with pgvector

Upload images to Postgres, save images with tensors format and query the near duplicate images with pgvector.

INSTALL PGVECTOR EXTENSIONS ON POSTGRES

**Requirement**:

Docker

Python > 3.9

Library: psycopg2

**Insall**:

Step 1: pull pgvector from PostgreSQL Docekr image

>> docker pull pgvector/pgvector:pg16 

Step 2: Create a Docker volume

>> docker volume create pgvector-data

Step 3: Create a pgvector PostgreSQL container

>> docker run --name pgvector-container -e POSTGRES_PASSWORD=<password> \
 -p 5432:5432 -v pgvector-data:/var/lib/postgresql/data \
 -d pgvector/pgvector:pg16 

Step 4: Create a new database, connect to the database, new table, etc.

Step 5: Run the command successively:

>> python setup_connection.py

>> python encode_clip.py

>> python similar_search.py

**Note**:

If you want to query directly on PostgreSQL, follow this instructions:

>> docker exec -it pgvector-container psql -U postgres

>> CREATE DATABASE <databasename>;

>> CREATE EXTENSION vector;

Check the extension is added:

>> \dx 

Create and add data into the database as same as above (remember to convert into tensor format)

Use this query to find the cosine similarity between two vectors:

>>  1 - (t1.tensor <-> t2.tensor) AS similarity

**Directory structure:**

your_project/

│
├── Dockerfile

├── requirements.txt

├── your_script.py

├── lib/

│   ├── __init__.py

│   └── other_files.py

└── encode_clip.py

└── setup_connection.py
