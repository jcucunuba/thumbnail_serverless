import os
import json
import boto3
from PIL import Image

s3 = boto3.client('s3')

def generate_thumbnail(image_path, thumbnail_path):
    with Image.open(image_path) as img:
        img.thumbnail((100, 100))  
        img.save(thumbnail_path)

def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
   
    image_path = '/tmp/original.jpg'
    thumbnail_path = '/tmp/thumbnail.jpg'
   
    s3.download_file(bucket, key, image_path)
   
    generate_thumbnail(image_path, thumbnail_path)
   
    thumbnail_key = os.path.splitext(key)[0] + '_thumbnail.jpg'
    s3.upload_file(thumbnail_path, bucket, thumbnail_key)
   
    return {
        'statusCode': 200,
        'body': 'Thumbnail generated'
    }