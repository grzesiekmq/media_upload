def media_pairs(photos):
    paired = []
    for i in range(len(photos) - 1):
        current_item, next_item = photos[i], photos[i + 1]
        paired.append((current_item, next_item))

    return paired