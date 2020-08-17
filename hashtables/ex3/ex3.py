def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # store all numbers here
    cache = {}
    # store all the lists here
    lists = len(arrays)
    print(lists)
    # creates a place to store our duplicate or intersection values here
    duplicates = []

    # loop over our lists
    for i in arrays:
        # loop over every number in each list
        for num in i:
            # if the number is not already in our cache put it there now
            if num not in cache:
                cache[num] = True
            else:
                cache[num] += 1
                if cache[num] == lists:
                    duplicates.append(num)
    return duplicates


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
