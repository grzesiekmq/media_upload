import unittest
import os

from video_animation.create_animation import CreateAnimationHandler
from media.local_storage import LocalMediaStorage
from media.transformation.image_to_video import ImageToVideoConverter
from video_animation.tmp_storage import TmpStorage

class TestCreateAnimationHandler(unittest.TestCase):
    def setUp(self):
        files = [
            self.get_full_path('ws/tmp/photos_1.jpeg.mov'),
            self.get_full_path('ws/tmp/photos_2.jpeg.mov'),
            self.get_full_path('ws/tmp/photos_3.jpeg.mov'),
            self.get_full_path('ws/tmp/photos_5.jpeg.mov'),
            self.get_full_path('ws/tmp/photos_1.jpeg_photos_2.jpeg.mov'),
            self.get_full_path('ws/tmp/photos_2.jpeg_photos_3.jpeg.mov'),
            self.get_full_path('ws/tmp/photos_3.jpeg_photos_5.jpeg.mov'),
            self.get_full_path('ws/tmp/video_out.mov')
        ]

        for tmp_file in files:
            if os.path.isfile(tmp_file):
                os.remove(tmp_file)

    def get_full_path(self, file_name):
        path = os.path.join(
            os.path.dirname(__file__),
            file_name
        )
        return path

    def test_create_animation_base_on_files(self):
        photos = [
            'photos/1.jpeg',
            'photos/2.jpeg',
            'photos/3.jpeg',
            'photos/5.jpeg',
        ]

        video = 'video_out.mov'

        handler = CreateAnimationHandler(
            tmp_storage = TmpStorage(self.get_full_path('ws/tmp')),
            media_storage = LocalMediaStorage(self.get_full_path('ws')),
            transformation = ImageToVideoConverter()
        )

        handler.handle({
            'photos': photos,
            'video': video
        })

        assert os.path.isfile(self.get_full_path('ws/video_out.mov'))
