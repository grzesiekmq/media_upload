from uuid import uuid4

def generate_name(file_name):
    destination_filename = "medias/%s/%s" % (uuid4().hex, file_name)
    return destination_filename


def generate_animation_name(file_name):
    destination_filename = "animations/%s/%s" % (uuid4().hex, file_name)
    return destination_filename