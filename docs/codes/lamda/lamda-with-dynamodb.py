import boto3
import uuid
import os
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('USERS_TABLE', 'Users')  # Default to 'Users' if not set

def add_user(name, age, mail):
    table = dynamodb.Table(TABLE_NAME)
    user_id = str(uuid.uuid4())
    item = {
        'ID': user_id,
        'name': name,
        'age': int(age),
        'mail': mail
    }
    table.put_item(Item=item)
    return user_id

def fetch_user_by_id(user_id):
    table = dynamodb.Table(TABLE_NAME)
    response = table.query(
        KeyConditionExpression=Key('ID').eq(user_id)
    )
    items = response.get('Items', [])
    item = items[0] if items else None
    user = {
        'ID': item['ID'],
        'name': item['name'],
        'age': int(item['age']),
        'mail': item['mail']
    } if item else None
    return user

def make_response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }

def handle_create_user(event):
    body = json.loads(event['body'])
    name = body.get('name')
    age = body.get('age')
    mail = body.get('mail')
    if not all([name, age, mail]):
        return make_response(400, {'error': 'Missing required fields'})
    user_id = add_user(name, age, mail)
    return make_response(200, {'user_id': user_id})

def handle_get_user(event):
    path = event.get('path')
    user_id = path.split('/')[-1]
    print(f'Fetching user with ID: {user_id}')
    if not user_id:
        return make_response(400, {'error': 'Missing user_id'})
    user = fetch_user_by_id(user_id)
    if user:
        return make_response(200, user)
    else:
        return make_response(404, {'error': 'User not found'})

def handle_get_users(event):
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    users = response.get('Items', [])
    users = [{'ID': user['ID'], 'name': user['name'], 'age': int(user['age']), 'mail': user['mail']} for user in users]
    return make_response(200, users)

def lambda_handler(event, context):
    print('Request event: ', event)
    print('Context: ', context)
    http_method, path = extract_from_event(event)
    print('Path:', path, '| HTTP Method:', http_method)

    try:
        if http_method == 'GET' and path == '/':
            return make_response(200, {'msg': "Hello world!"})
        elif http_method == 'POST' and path == '/users':
            return handle_create_user(event)
        elif http_method == 'GET' and path == '/users':
            return handle_get_users(event)
        elif http_method == 'GET' and path.startswith('/users/'):
            return handle_get_user(event)
        else:
            return make_response(400, {'error': 'Invalid action'})
    except Exception as e:
        print('Error: ', str(e))
        return make_response(500, {'error': 'Internal server error'})

def extract_from_event(event):
    http_method = None
    path = None
    if event.get("version") == "2.0":
        # For HTTP API Gateway v2.0
        http_method = event.get('requestContext', {}).get('http', {}).get('method')
        path = event.get('requestContext', {}).get('http', {}).get('path')
    else:
        http_method = event.get('httpMethod')
        path = event.get('path')
    return http_method, path
