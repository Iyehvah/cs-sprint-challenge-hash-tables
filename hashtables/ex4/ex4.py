def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    myDictionary = {}
    positives = []
    
    for num in a:
        myDictionary[num] = 1
        if num != 0 and -num in myDictionary:
            positives.append(abs(num))
    return positives

my_array = [-3,-2,-1,0,1,2,3]

print(has_negatives(my_array))

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
