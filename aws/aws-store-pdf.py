import json
import base64
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Extract information from the event (assumes a JSON body with base64-encoded file data)
    try:
        # Get the base64 encoded file data, file name, and bucket name from the event
        file_data = event.get('body')
        file_name = event.get('headers').get('file-name')  # Get the file name from headers
        bucket_name = event.get('headers').get('bucket-name')  # Get the bucket name from headers
        
        if not file_data or not file_name or not bucket_name:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing required parameters: file_data, file_name, or bucket_name.')
            }

        # Decode the base64 file data
        decoded_file_data = base64.b64decode(file_data)

        # Upload the file to S3
        try:
            response = s3_client.put_object(
                Bucket=bucket_name,
                Key=file_name,
                Body=decoded_file_data,
                ContentType='application/pdf'  # Change this if the file type is different
            )

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'File uploaded successfully!',
                    's3_response': response
                })
            }

        except ClientError as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error uploading file: {e}')
            }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error processing request: {e}')
        }
