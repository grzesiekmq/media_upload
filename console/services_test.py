from request_queue.memory_queue import RequestQueue
import os


def get_full_path(file_name):
    path = os.path.join(
        os.path.dirname(__file__),
        file_name
    )
    return path

requests = [
    {
        'photos': [
            'medias/00eaa79ad68046e28fd7039f67552828/2.jpeg',
            'medias/1e000f25c0e94ed3b4b84fcdbe94d388/1.jpeg'
        ],
        'email': 'jakub.kanclerz@gmail.com'
    }
]

queue = RequestQueue(requests=requests)

from video_animation.create_animation import CreateAnimationHandler
from media.local_storage import LocalMediaStorage
from media.transformation.image_to_video import ImageToVideoConverter
from video_animation.tmp_storage import TmpStorage


handler = CreateAnimationHandler(
    tmp_storage=TmpStorage(get_full_path('../var/tmp')),
    media_storage=LocalMediaStorage(get_full_path('../var/media')),
    transformation=ImageToVideoConverter()
)
