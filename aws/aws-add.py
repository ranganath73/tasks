import json

def lambda_handler(event, context):
    # Extract the numbers from the event (assuming the numbers are passed in the event)
    num1 = event.get('num1')
    num2 = event.get('num2')
    
    # Check if the numbers are provided
    if num1 is None or num2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Missing numbers in input.')
        }
    
    # Perform the addition
    result = num1 + num2
    
    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
