import unittest
from order_delivery.digital_delivery import EmailDelivery
import re


class TestNaming(unittest.TestCase):

    def test_send_email_with_download_url(self):
        delivery = EmailDelivery()
        delivery.deliver(email='jakub.kanclerz@gmail.com', animation_ref='http://video.url')

if __name__ == '__main__':
    unittest.main()