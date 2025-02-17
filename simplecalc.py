import json

def lambda_handler(event, context):
    try:
        print(event)

        # Validate HTTP method
        if event.get('httpMethod', '').lower() != 'post':
            return {
                'statusCode': 400,
                'body': json.dumps('Unexpected method. Use POST.')
            }

        # Parse JSON body
        payload = json.loads(event.get('body', '{}'))
        first = payload.get('first')
        second = payload.get('second')
        operation = payload.get('operation')

        # Validate input data
        if first is None or second is None or operation is None:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing required parameters: first, second, operation')
            }

        try:
            first = float(first)
            second = float(second)
        except ValueError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid number format')
            }

        # Perform the requested operation
        if operation == 'addition':
            result = first + second
        elif operation == 'subtraction':
            result = first - second
        elif operation == 'multiplication':
            result = first * second
        elif operation == 'division':
            if second == 0:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Error: Division by zero')
                }
            result = first / second
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Unknown operation. Use: addition, subtraction, multiplication, division')
            }

        return {
            'statusCode': 200,
            'body': json.dumps(f'{operation} result is {result}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Internal Server Error: {str(e)}')
        }
