#!/usr/bin/python3

input_list = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

def smallest(array):
    miny = -10000
    minx = -10000
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            for k in range(0, len(array)):
                for l in range(0, len(array[k])):
#                    print("[{}, {}]".format(array[i][j], array[k][l]), end=", ")
                    min_num = min(array[i][j], array[k][l])
                    max_num = max(array[i][j], array[k][l])
                    for m in range(len(array)):
                        for n in range(len(array[m])):
                            if (array[m][n] >= min_num and array[m][n] <= max_num):
                                break
                        if (n == len(array[m])):
                            break
                    if (m == len(array)):
                        miny = max_num
                        minx = min_num
    return miny

                    

print(smallest(input_list))

