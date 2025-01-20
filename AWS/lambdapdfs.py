import boto3
import base64

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Parameters from the event
    bucket_name = 'your-s3-bucket-name'
    file_name = event['file_name']  # Expecting a file name from the event
    file_content = base64.b64decode(event['file_content'])  # File content should be base64 encoded in the event
    
    # Upload the file to the S3 bucket
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
    
    return {
        'statusCode': 200,
        'body': f'File {file_name} successfully uploaded to {bucket_name}'
    }
