-- docker exec -it pgvector-container psql -U postgres
 CREATE TABLE image_tensors (
     name TEXT PRIMARY KEY,
     tensor VECTOR(512)  
 );

 select * from image_tensors
 -- drop table image_tensors

 SELECT 
     t1.name AS image1_name, 
     t2.name AS image2_name, 
     1 - (t1.tensor <-> t2.tensor) AS similarity
 FROM 
     image_tensors t1 
 JOIN 
     image_tensors t2 ON t1.name != t2.name
 ORDER BY 
     similarity DESC;
