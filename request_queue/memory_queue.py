import json, time

class Request:
    def __init__(self, photos):
        self.photos = photos

    def confirm(self):
        return

class RequestQueue:
    def __init__(self, requests):
        self.initial_requests = requests

    def requests(self):
        while True:
            for data in self.initial_requests:
                request = Request(photos=data['photos'])
                yield request
            time.sleep(5)
