import unittest
import os

from video_animation.helpers import media_pairs

class TestStructureManipulators(unittest.TestCase):

    def test_create_media_pairs(self):
        medias = ['1', '2', '3', '4']

        pairs = media_pairs(medias)

        assert [('1', '2'), ('2', '3'), ('3', '4')] == pairs
