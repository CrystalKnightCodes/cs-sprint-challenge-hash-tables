def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for weight in range(length):
        current_weight = weights[weight]
        remaining_weight = limit - current_weight

        if remaining_weight in cache:
            if cache[remaining_weight] > weight:
                return[cache[remaining_weight], weight]
            else:
                return [weight, cache[remaining_weight]]
        else:
            cache[current_weight] = weight

    return None
