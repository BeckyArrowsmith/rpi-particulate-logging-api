import os
import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

LOGS_TABLE = os.environ['LOGS_TABLE']
IS_OFFLINE = os.environ.get('IS_OFFLINE')

if IS_OFFLINE:
    client = boto3.client(
        'dynamodb',
        region_name='localhost',
        endpoint_url='http://localhost:8000'
    )
else:
    client = boto3.client('dynamodb')


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/logs/<string:log_id>")
def get_log(log_id):
    resp = client.get_item(
        TableName=LOGS_TABLE,
        Key={

            'logId': { 'S': log_id }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'Log does not exist'}), 404

    return jsonify({
        'logId': item.get('logId').get('S'),
        'data': item.get('data').get('S')
    })

@app.route("/logs", methods=["POST"])
def create_log():
    log_id = request.json.get('logId')
    data = request.json.get('data')
    if not log_id or not data:
        return jsonify({'error': 'Please provide logId and data'}), 400
    
    resp = client.put_item(
        TableName=LOGS_TABLE,
        Item={
            'logId': {'S': log_id },
            'data': {'S': data }
        }
    )

    return jsonify({
        'logId': log_id,
        'data': data
    })