import hvac  # HashiCorp Vault client 
 
client = hvac.Client(url="https://vault.example.com", token="s.123456") 
secret = client.secrets.kv.v2.read_secret_version(path="analytics/prod")["data"]["data"] 
db_password = secret["DB_PASSWORD"] 
