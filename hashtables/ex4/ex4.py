def has_negatives(a):
    cache = {}
    result = []
 
    for number in a:
        cache[number] = 1
        if number != 0 and -number in cache:
            result.append(abs(number))
   
#    Attempt at refactoring to make better use of the hash table.  Ran out of time to complete.
    # for number in a:
    #     if number > 0:
    #         cache[number] = 1
    #     elif number < 0:
    #         cache[number] = 2
    #         # negatives.append(number)
    
    # positives = list(cache.keys())[list(cache.values()).index(1)]
 
    # for number in positives:
    #     if -number in cache:
    #         result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
