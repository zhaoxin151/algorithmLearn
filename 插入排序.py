#!/usr/bin/python
# --coding:utf-8 --

# 插入排序原理：当一个乱序数组，从第二个索引开始循环，跟左边的数组的元素相比较

# 从小到大排序
def insertSortFun(arr):
    # 从 1开始到arr.length的循环
    for firstNum in range(1, len(arr)):
        # 从第一个元素开始比较
        for secondNum in range(0, firstNum):
            if arr[firstNum] < arr[secondNum]:
                temp = arr[firstNum]
                arr[firstNum] = arr[secondNum]
                arr[secondNum] = temp
    return arr


# 逆序排序
def reverseInsert(arr):
   # 从1开始
   for firstNum in range(1, len(arr)):
       for secondNum in range(0, firstNum):
           if arr[firstNum] > arr[secondNum]:
               temp = arr[firstNum]
               arr[firstNum] = arr[secondNum]
               arr[secondNum] = temp
   return arr

if __name__ == '__main__':
    arr1 = [3, 2, 45, 53,21, 23, 45, 66, 22]
    print(insertSortFun(arr1))
    print()
    print(reverseInsert(arr1))