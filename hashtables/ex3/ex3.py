def intersection(arrays):
    cache = {}

    # get shortest array in arrays
    shortest_array = []
    if len(arrays) > 0:
        shortest_array = arrays[0]

    for array in arrays:
        if len(array) < len(shortest_array):
            shortest_array = array
   
    # populate cache, based on the shortest array
    for number in shortest_array:
        cache[number] = 1

    # find repeating numbers
    for array in arrays:
        if array is not shortest_array:
            new_cache = {}
            for number in array:
                if number in cache:
                    new_cache[number] = 1
            
            cache = new_cache
            
    result = list(cache.keys())

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
