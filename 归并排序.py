#!/usr/bin/python
# --coding:utf-8 --

# 使用递归算法，来把数组从len(arr)/2分割为两个数组，再把两个子数组再分割达到每个数组两个数就行

def guibingSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        num = int(len(arr)/2)
        # 递归
        firstArr = guibingSort(arr[ :num])
        sectondArr = guibingSort(arr[num: ])
        return mergeLeftRight(firstArr, sectondArr)

# 两个数组排序，组成一个新的数组
def mergeLeftRight(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result .append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result

if __name__ == '__main__':
    arr1 = [23, 34, 12, 55, 22, 6, 44, 67, 24]
    print(guibingSort(arr1))