from media.local_storage import LocalMediaStorage

class TmpStorage(LocalMediaStorage):
    def absolute_path(self, key):
        return self.get_path(key)