import mandrill

from jinja2 import Environment, FileSystemLoader
import os


def print_html_doc(variables):
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    j2_env = Environment(
        loader=FileSystemLoader(THIS_DIR),
        trim_blocks=True
    )
    return j2_env.get_template('order_email.html').render(
        variables=variables
    )

mandrill_api_key = os.getenv('MANDRILL_KEY')
mandrill_client = mandrill.Mandrill(mandrill_api_key)

def send_mail(to, variables):
  try:
    message = {
      'auto_html': None,
      'auto_text': None,
      'from_email': 'jakub@jkan.pl',
      'from_name': '',
      'html': print_html_doc(variables),
      'text': 'See it in html mode',
      'subject': "Your animation",
      'to': [
         {
           'email': to,
           'name': 'Recipient Name',
           'type': 'to'
         }
      ]
    }
    result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')

  except mandrill.Error, e:
      print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
      raise
