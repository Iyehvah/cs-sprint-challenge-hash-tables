# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    #store files here
    cached_files = {}
    #store results
    result = []
    #loop through each path available in files
    for path in files:
        #add a /after each path
        split_path = path.split("/")
        #before each file put a /
        file_name = split_path[-1]
        if file_name not in cached_files:
            #if our file isnt already in our cache add it with its path
            cached_files.setdefault(file_name, [path])
        else:
            #add a path to an existing file
            cached_files[file_name].append(path)

    for query in queries:
        if query in cached_files:
            for path in cached_files[query]:
                #if our search is in our cached files then return our path
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
