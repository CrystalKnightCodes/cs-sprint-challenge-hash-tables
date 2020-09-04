def has_negatives(a):
    cache = {}
    result = []

    for number in a:
        cache[number] = 1
        if number != 0 and -number in cache:
            result.append(abs(number))
    
    print(f"The numbers with negatives are: {result}")        
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
