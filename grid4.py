#!/usr/bin/python3

def grid_check(n, query):
    """check if query is in grid"""
    if query[0] > n or query[1] > n:
        return False
    elif query[0] < 1 or query[1] < 1:
        return False
    else:
        return True

def diagonal(item, query):
    """check if query is in diagonal path"""
    if abs(item[0] - query[0]) == abs(item[1] - query[1]):
        return True
    else:
        return False

def row_cols(item, query):
    """check if query is in row or column path"""
    if item[0] == query[0]:
        return True
    if item[1] == query[1]:
        return True
    else:
        return False

def adjacent(lamp_list, query):
    """removes adjacent lamps from list of lamps"""
    new_list = []
    for lamp in lamp_list:
        if lamp[0] == (query[0] - 1) and lamp[1] == (query[1] - 1):
            continue
        if lamp[0] == (query[0] - 1) and lamp[1] == (query[1]):
            continue
        if lamp[0] == (query[0] - 1) and lamp[1] == (query[1] + 1):
            continue
        if lamp[0] == (query[0]) and lamp[1] == (query[1] - 1):
            continue
        if lamp[0] == (query[0]) and lamp[1] == (query[1]):
            continue
        if lamp[0] == (query[0]) and lamp[1] == (query[1] + 1):
            continue
        if lamp[0] == (query[0] + 1) and lamp[1] == (query[1] - 1):
            continue
        if lamp[0] == (query[0] + 1) and lamp[1] == (query[1]):
            continue
        if lamp[0] == (query[0] + 1) and lamp[1] == (query[1] + 1):
            continue
        new_list.append(lamp)
    return new_list

# Complete the checkIllumination function below.
def checkIllumination(N, lamps, queries):
    lux = []
    for query in queries:
        lamp_list = lamps
        flag = False
        if grid_check(N, query) is False:
            lux.append("DARK")
            continue
        lamp_list = adjacent(lamps, query)
        for item in lamp_list:
            if diagonal(item, query) is True or row_cols(item, query) is True:
                flag = True
                break
        if flag == True:
            lux.append("LIGHT")
        else:
            lux.append("DARK")
    return(lux)


if __name__ == "__main__":
    size = 8
    #queries = [[0,0], [11,1], [1,1], [2,2], [-1, -1], [6,2]]
    queries = [[4, 4], [6, 6], [8,1], [3,2], [2, 3]]
    lamps = [[1, 6], [5, 6], [7,3], [3,2]]
    lux_list = []

    lux_list = checkIllumination(size, lamps, queries)
    print(lux_list)
