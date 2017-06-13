from helpers import media_pairs

class CreateAnimationHandler:

    def __init__(self, tmp_storage, media_storage, transformation):
        self.media_storage = media_storage
        self.tmp_storage = tmp_storage
        self.transformation = transformation

    def handle(self, command):
        photos = command['photos']

        self.load_to_tmp_storage(photos)

        self.create_video_for_each(photos)

        self.create_transition_for_each(photos)

        video_name = command['video'].replace('/', '_')
        self.create_animation(video_name, photos)

        video_media = open(
            self.tmp_storage.absolute_path(command['video'].replace('/', '_')),
            'r'
        )

        self.media_storage.store_public(command['video'], video_media)

    def create_animation(self, video_name, photos):
        animation = [self.tmp_storage.absolute_path(self.single_name(photos[0]))]
        for current, next in media_pairs(photos):
            animation.append(
                self.tmp_storage.absolute_path(self.transition_name(current, next))
            )
            animation.append(
                self.tmp_storage.absolute_path(self.single_name(next))
            )

        self.transformation.concat_videos(
            animation,
            self.tmp_storage.absolute_path(video_name)
        )


    def create_transition_for_each(self, photos):
        for photo_pair in media_pairs(photos):
            current, next = photo_pair
            self.transformation.create_transition(
                self.tmp_storage.absolute_path(self.escape_photo_name(current)),
                self.tmp_storage.absolute_path(self.escape_photo_name(next)),
                self.tmp_storage.absolute_path(self.transition_name(current, next))
            )

    def create_video_for_each(self, photos):
        for photo in photos:
            self.transformation.transform(
                self.tmp_storage.absolute_path(self.escape_photo_name(photo)),
                self.tmp_storage.absolute_path(self.single_name(photo))
            )

    def load_to_tmp_storage(self, photos):
        for photo in photos:
            self.tmp_storage.store(self.escape_photo_name(photo), self.media_storage.get(photo))

    def escape_photo_name(self, photo):
        return photo.replace('/', '_')

    def single_name(self, photo):
        return ('%s.mov' % photo).replace('/', '_')

    def transition_name(self, photo1, photo2):
        return ('%s_%s.mov' % (photo1, photo2)).replace('/', '_')

    def video_output(self, name):
        return '%s.mov' % name
