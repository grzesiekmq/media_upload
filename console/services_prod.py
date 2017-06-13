from request_queue.sqs_queue import RequestQueue
import os
import boto3
from video_animation.create_animation import CreateAnimationHandler
from media.local_storage import LocalMediaStorage
from media.transformation.image_to_video import ImageToVideoConverter
from video_animation.tmp_storage import TmpStorage
import boto3
from botocore.client import Config
from media.s3_storage import S3MediaStorage

def get_full_path(file_name):
    path = os.path.join(
        os.path.dirname(__file__),
        file_name
    )
    return path


sqs = boto3.resource('sqs', region_name=os.getenv('QUEUE_REGION'))
orders = sqs.get_queue_by_name(QueueName=os.getenv('QUEUE_NAME'))
queue = RequestQueue(sqs_queue=orders)

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
media_storage = S3MediaStorage(s3=s3, bucket_name=os.getenv('BUCKET_NAME'))


handler = CreateAnimationHandler(
    tmp_storage=TmpStorage(get_full_path('../var/tmp')),
    media_storage=media_storage,
    transformation=ImageToVideoConverter()
)

from order_delivery.digital_delivery import EmailDelivery

delivery = EmailDelivery()