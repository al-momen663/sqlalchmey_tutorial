import json
from jsonschema import validate
 
schema = { 
    "type": "object", 
    "properties": { 
        "timestamp": {"type": "string", "format": "date-time"}, 
        "sensor_readings": {"type": "array", "items": {"type": "number"}} 
    }, 
    "required": ["timestamp"] 
} 
 
validate(instance=json.load(open("sensor_data.json")), schema=schema) 
  