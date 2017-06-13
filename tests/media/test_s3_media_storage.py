import unittest
import boto3
import os
from botocore.client import Config
from media.s3_storage import S3MediaStorage
import uuid
import requests

class TestS3MediaStorage(unittest.TestCase):
  def test_upload_file_to_s3(self):
    to_upld_path = os.path.join(os.path.dirname(__file__), 'test.txt')
    to_upl_file = open(to_upld_path, 'rb')
    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
    media_storage = S3MediaStorage(s3=s3, bucket_name='kanclerj')
    media_storage.store(key='upl_name.txt', media=to_upl_file)

  def test_download_file_to_s3(self):
    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
    media_storage = S3MediaStorage(s3=s3, bucket_name='kanclerj')
    media = media_storage.get(key='upl_name.txt')
    assert media.read(10000) == 'alfa omega\n'  
  
  def test_public_access_to_s3(self):
    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
    to_upld_path = os.path.join(os.path.dirname(__file__), 'test.txt')
    media_storage = S3MediaStorage(s3=s3, bucket_name='kanclerj')
    name = str(uuid.uuid4())
    to_upl_file = open(to_upld_path, 'rb')
    media_storage.store_public(key=name, media=to_upl_file)
    url = "https://s3.eu-central-1.amazonaws.com/kanclerj/%s" % name
    r = requests.head(url)
    assert r.status_code == 200

if __name__ == '__main__':
  unittest.main()
