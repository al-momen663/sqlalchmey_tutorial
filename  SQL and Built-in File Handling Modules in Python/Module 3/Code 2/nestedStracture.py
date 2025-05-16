# Extract nested values from API responses 
import jsonpath_ng  # pip install jsonpath-ng 
 
data = json.load(open("api_response.json")) 
expr = jsonpath_ng.parse("$.metrics[*].daily_stats[?(@.date > '2023-01-01')].value") 
matches = [match.value for match in expr.find(data)] 
