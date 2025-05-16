import boto3 
 
client = boto3.client("secretsmanager") 
response = client.get_secret_value(SecretId="prod/analytics/postgres") 
credentials = json.loads(response["SecretString"])