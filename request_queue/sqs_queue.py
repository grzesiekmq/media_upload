import json, time

class Request:
    def __init__(self, photos, message, email):
        self.email = email
        self.message = message
        self.photos = photos

    def confirm(self):
        self.message.delete()

class RequestQueue:
    def __init__(self, sqs_queue):
        self.sqs_queue = sqs_queue

    def requests(self):
        while True:
            for message in self.sqs_queue.receive_messages():
                data = json.loads(message.body)
                request = Request(photos=data['photos'], email=data['email'], message=message)
                yield request
            time.sleep(1)
