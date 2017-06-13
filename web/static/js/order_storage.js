;
var OrderStorage = function(storage) {

    if (!storage.getItem('photos')) {
        storage.setItem('photos', JSON.stringify([]))
    }

    return {
        addItem: function(media) {
            var photos = JSON.parse(storage.getItem('photos'));
            photos.push(media);
            storage.setItem('photos', JSON.stringify(photos))
        },
        getAllMedias: function() {
            return JSON.parse(storage.getItem('photos'));
        },
        reset: function() {
            storage.setItem('photos', JSON.stringify([]))
        }
    }
}
