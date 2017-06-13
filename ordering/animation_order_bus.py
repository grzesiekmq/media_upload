import json


class SQSAnimationOrderBus:

    def __init__(self, sqs_queue):
        self.sqs_queue = sqs_queue

    def handle_order(self, order):
        body = json.dumps({
            'email': order.email,
            'photos': order.photos
        })
        self.sqs_queue.send_message(MessageBody=body)

class MemoryAnimationOrderBus:
    def handle_order(self, order):
        body = json.dumps({
            'email': order.email,
            'photos': order.photos
        })

        print 'Queue retrieved message %s' % body
