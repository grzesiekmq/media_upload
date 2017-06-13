import unittest
from media.naming import generate_name
import re


class TestNaming(unittest.TestCase):

    def test_generate_name_with_prefix(self):
        name = generate_name('foo.jpg')
        regexp = re.compile(r'^medias\/[0-9a-f]{32}\/foo.jpg$')

        assert regexp.search(name)


if __name__ == '__main__':
    unittest.main()