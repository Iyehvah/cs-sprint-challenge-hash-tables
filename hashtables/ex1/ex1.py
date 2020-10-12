def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cached_weights = {}
    for i in range(length):
        difference = limit - weights[i]
        if difference in cached_weights:
            return (i, cached_weights[difference])
        cached_weights[weights[i]] = i
    return None
