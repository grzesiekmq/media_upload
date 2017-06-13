from ordering.animation_order_bus import MemoryAnimationOrderBus
from media.local_storage import LocalMediaStorage
import os

def get_full_path(file_name):
    path = os.path.join(
        os.path.dirname(__file__),
        file_name
    )
    return path

media_storage = LocalMediaStorage(path=get_full_path('../var/media'))

animation_order_bus = MemoryAnimationOrderBus()