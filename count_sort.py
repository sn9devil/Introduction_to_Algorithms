# 计数排序

#
# def countSort(array):
#     # 得到数列的最大值和最小值，并算出差值 d
#     max = array[0]
#     min = array[0]
#     for i in array:
#         if i > max:
#             max = i
#         if i < min:
#             min = i
#     d = max - min
#     # 初始化countList
#     countList = [0] * (d+1)
#     # 统计数组对应元素个数
#     for i in array:
#         countList[i - min] = countList[i-min] + 1
#     # 还原，排序
#     sortedArray = []
#     for num, i in enumerate(countList):
#         while(i>0):
#             sortedArray.append(num + min)
#             i = i - 1
#     return sortedArray



def countSort(array):
    # 得到数列的最大值和最小值，并算出差值 d
    max = array[0]
    min = array[0]
    for i in array:
        if i > max:
            max = i
        if i < min:
            min = i
    d = max - min
    # 初始化countList
    countList = [0] * (d+1)
    # 统计数组对应元素个数
    for i in array:
        countList[i - min] = countList[i-min] + 1

    # 统计数组做变形，后面的元素等于前面的元素之和
    sum = 0
    for num, i in enumerate(countList):
        sum += i
        countList[num] = sum

    # 倒序遍历原始数列，从统计数组找到正确位置，输出到结果数组
    array_len = len(array)
    sortedArray = [0] * array_len
    for i in array[::-1]:
        array_len -= 1
        sortedArray[countList[i-min]-1] = i
        countList[i-min] -= 1

    return sortedArray



A = [20,28,25,30,24,32,35,32,40,31,34]
countList = countSort(A)
print(countList)