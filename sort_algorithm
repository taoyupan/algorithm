#冒泡排序
#循环，两两向后比较。具体方法是针对循环中的每一元素，都对它后面的元素循环比较，交换大小值，
#每次循环“冒”一个最小值放在里层循环初始的地方

def bubbleSort(num):
    n = len(num)
    if n <= 1:
        return num
    for i in range(n):
        for j in range(n-1-i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j + 1]
                num[j+1] = temp
    return num
    
    
    # 选择排序
    # 选择排序的思路是固定位置，选择排序，即：先从序列中，找到最小的元素，放到第一个位置
    # 然后找到第二小的元素，放到第二个位置，以此类推，直到排好所有的值。
    
 def selectSort(num):
    n = len(num)
    if n <= 1:
        return num
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if num[min_index] > num[j]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num
  

 
