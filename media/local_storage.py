import distutils.dir_util
import os

class LocalMediaStorage:
  def __init__(self, path):
    self.path = path

  def store(self, key, media):
    distutils.dir_util.mkpath(os.path.dirname(self.get_path(key)))

    output = open(self.get_path(key), 'w+')
    input = media
    while True:
      data = input.read(100000)
      if data == '':
        break
      output.write(data)

  def get(self, key):
    return open(self.get_path(key), 'r')

  def get_path(self, key):
    return '%s/%s' % (self.path, key)