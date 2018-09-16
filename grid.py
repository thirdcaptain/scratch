#!/usr/bin/python3

def grid_check(n, lamp):
    if lamp[0] > n or lamp[1] > n:
        return False
    else:
        return True

def diagonal(item, lamp):
    if abs(item[0] - lamp[0]) == abs(item[1] - lamp[1]):
        return True
    else:
        return False

def adjancent_rem(lamp):
    try:
        

if __name__ == "__main__":
    size = 5
    queries = [[0,0], [1,1], [-1, -1], [6,2]]
    coordinate = [[2, 2], [2, 3]]

    for item in coordinate:
        coordinate_cpy = coordinate
        for lamp in queries:
            if grid_check(size, lamp) is True:
                print("{} is within grid of size {}".format(lamp, size))
            elif grid_check(size, lamp) is False:
                print("{} is OUT OF of grid of size {}".format(lamp, size))
            if diagonal(item, lamp) is True:
                print("{} and {} are diagonal".format(item, lamp))
            elif diagonal(item, lamp) is False:
                print("{} and {} are NOT diagonal".format(item, lamp))
