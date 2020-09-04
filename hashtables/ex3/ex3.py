def intersection(arrays):
    cache = {}
    result = []



    for array in arrays:
        for number in array:
            if number in cache:
                cache[number] += 1
                if number not in result:
                    result.append(number)
            else:
                cache[number] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
