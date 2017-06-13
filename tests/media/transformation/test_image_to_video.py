import unittest
import os

from media.transformation.image_to_video import ImageToVideoConverter

class TestImageToVideoTransformation(unittest.TestCase):

    def setUp(self):
        files = [
            self.get_full_path('ws/photos/2.mov'),
            self.get_full_path('ws/photos/1_to_2.mov'),
            self.get_full_path('ws/output_animation.mov')
        ]

        for tmp_file in files:
            if os.path.isfile(tmp_file):
                os.remove(tmp_file)

    def test_image_to_video_transformation(self):
        image_path = self.get_full_path('ws/photos/2.jpeg')
        video_path = self.get_full_path('ws/photos/2.mov')

        converter = ImageToVideoConverter()
        converter.transform(image_path, video_path)

        assert os.path.isfile(video_path)

    def test_image_transition(self):
        image_1_path = self.get_full_path('ws/photos/1.jpeg')
        image_2_path = self.get_full_path('ws/photos/2.jpeg')
        video_path = self.get_full_path('ws/photos/1_to_2.mov')

        converter = ImageToVideoConverter()
        converter.create_transition(image_1_path, image_2_path, video_path)

        assert os.path.isfile(video_path)

    def test_video_concatenation(self):
        video_path = self.get_full_path('ws/output_animation.mov')
        video_parts = [
            self.get_full_path('ws/video/1.mov'),
            self.get_full_path('ws/video/1_to_2.mov'),
            self.get_full_path('ws/video/2.mov'),
        ]
        converter = ImageToVideoConverter()
        converter.concat_videos(video_parts, video_path)

        assert os.path.isfile(video_path)

    def get_full_path(self, file_name):
        path = os.path.join(
            os.path.dirname(__file__),
            file_name
        )
        return path


if __name__ == '__main__':
    unittest.main()