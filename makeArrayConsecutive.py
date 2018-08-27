#!/usr/bin/python3
def makeArrayConsecutive(statues):
    diff = 0;
    list = sorted(statues)
    print(list)
    for idx in range(len(list) - 1):
        if list[idx] != (list[idx + 1] + 1):
            print("idx:{} diff:{}".format(idx, diff))
            diff += ((list[idx + 1] - list[idx]) - 1)
    return diff

if __name__ == "__main__":
    list = [6, 2, 3, 8]
    print(makeArrayConsecutive(list))
