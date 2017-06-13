class DigitalDelivery:

    def __init__(self):
        pass

    def deliver(self, email, animation_ref):
        pass

from mailer import send_mail


class EmailDelivery(DigitalDelivery):
    def deliver(self, email, animation_ref):
        variables = {}
        variables['download_url'] = animation_ref
        send_mail(to=email, variables=variables)

    def __init__(self):
        DigitalDelivery.__init__(self)
