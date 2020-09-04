def has_negatives(a):
    cache = {}
    result = []
 
    # for number in a:
    #     cache[number] = 1
    #     if number != 0 and -number in cache:
    #         result.append(abs(number))
   
#    Refactored to make better use of the hash table.  
    cache['negative'] = []
    cache['positive'] = []
    
    for number in a:
        if number > 0:
            cache['positive'].append(number)

        elif number < 0:
                cache['negative'].append(number) 

 
    for number in cache['negative']:
        if -number in cache['positive']:
            result.append(-number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
