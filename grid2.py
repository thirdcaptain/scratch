#!/usr/bin/python3

def grid_check(n, lamp):
    if lamp[0] > n or lamp[1] > n:
        return False
    elif lamp[0] < 0 or lamp[1] < 0:
        return False
    else:
        return True

def diagonal(item, lamp):
    if abs(item[0] - lamp[0]) == abs(item[1] - lamp[1]):
        return True
    else:
        return False

def row_cols(item, lamp):
    if item[0] == lamp[0]:
        return True
    if item[1] == lamp[1]:
        return True
    else:
        return False

def adjacent(coord_list, query):
    new_list = []
    for coord in coord_list:
        if coord[0] == (query[0] - 1) and coord[1] == (query[1] - 1):
            continue
        if coord[0] == (query[0] - 1) and coord[1] == (query[1]):
            continue
        if coord[0] == (query[0] - 1) and coord[1] == (query[1] + 1):
            continue
        if coord[0] == (query[0]) and coord[1] == (query[1] - 1):
            continue
        if coord[0] == (query[0]) and coord[1] == (query[1]):
            continue
        if coord[0] == (query[0]) and coord[1] == (query[1] + 1):
            continue
        if coord[0] == (query[0] + 1) and coord[1] == (query[1] - 1):
            continue
        if coord[0] == (query[0] + 1) and coord[1] == (query[1]):
            continue
        if coord[0] == (query[0] + 1) and coord[1] == (query[1] + 1):
            continue
        new_list.append(coord)
    return new_list

def illumination(size, queries, coordinate):
    lux = []
    for query in queries:
        coord_list = coordinate
        flag = False
        print("query is {}".format(query))
        print("coordinate is {}".format(coordinate))
        if grid_check(size, query) is False:
            lux.append(False)
            continue
        coord_list = adjacent(coordinate, query)
        print("coord_list is {}".format(coord_list))
        print()
        for item in coord_list:
            if diagonal(item, query) is True or row_cols(item, query) is True:
                flag = True
                break
        if flag == True:
            lux.append(True)
        else:
            lux.append(False)
    return lux

if __name__ == "__main__":
    size = 5
    queries = [[0,0], [11,1], [1,1], [2,2], [-1, -1], [6,2]]
    coordinate = [[2, 2], [2, 3]]
    lux_list = []

    lux_list = illumination(size, queries, coordinate)
    print(lux_list)


"""
    for lamp in queries:
        coordinate_cpy = coordinate
        if grid_check(size, lamp) is True:
            print("{} is within grid of size {}".format(lamp, size))
        elif grid_check(size, lamp) is False:
            print("{} is OUT OF of grid of size {}".format(lamp, size))
        if diagonal(item, lamp) is True:
            print("{} and {} are diagonal".format(item, lamp))
        elif diagonal(item, lamp) is False:
            print("{} and {} are NOT diagonal".format(item, lamp))
"""
