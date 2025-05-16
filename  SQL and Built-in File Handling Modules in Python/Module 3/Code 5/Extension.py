# Query nested JSON stored in SQLite 
cursor.execute(""" 
    SELECT json_extract(metadata, '$.sensor_id') 
    FROM devices 
    WHERE json_extract(metadata, '$.last_reading.value') > 100 
""") 
  