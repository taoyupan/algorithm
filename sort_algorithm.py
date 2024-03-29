#冒泡排序  （稳定）
#循环，两两向后比较。具体方法是针对循环中的每一元素，都对它后面的元素循环比较，交换大小值，
#每次循环“冒”一个最小值放在里层循环初始的地方
def bubbleSort(num):
    n = len(num)
    if n <= 1:
        return num
    for i in range(n):
        for j in range(n-1-i):
            if num[j] > num[j+1]:
              num[j], num[j+1] = num[j+1], num[j]  
    return num

#  改进的冒泡排序 （若一趟中没有值交换位置，说明已经有序了可以结束）
def bulleSort(num):
    if len(num) <= 1:
        return num
    for i in range(len(num)-1):
        state = False   # 假设本次循环状态没有改变
        for j in range(len(num)-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                state = True   #  有数值交换，那么状态就为真
        if not state:   # 遍历一次没有数值交换，则说明已经排好序
            break
    return num
    
    
# 选择排序 （不稳定）
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
  
    
#  插入排序 （稳定）
#  从第二个位置开始，与其前面的每个元素相比较，直到找到没有数比他大的位置
def insertSort(num):
    if len(num) <= 1:
        return num
    for i in range(1,len(num)):
        x = num[i]  #  第i个元素
        j = i   #  第i个位置
        while j > 0 and num[j-1] > x:
            num[j] = num[j-1]
            j -= 1
        num[j] = x
    return num

# 优化插入排序，由于左边的是已经排好序的部分，可以用二分查找法找到第i个元素应该插入的位置
def insertSort(num):
    if len(num) <= 1:
        return num
    for i in range(1, len(num)):
        tem = num[i]   #  待插入的值
        left = 0
        right = i-1
        # 待插入的值与已排序区域的中间值比较，不断缩小区域范围，直到left和right相遇
        while left <= right:
            mid = (left + right) // 2
            if num[i] < num[mid]:
                right = mid-1
            else:
                left = mid+1
        # 当left和right相遇时,待插入值的位置其实就是left位置，此时要将left
        # 到有序序列的最后一个元素都向后移动一个位置
        for j in range(i-1, left-1, -1):
            num[j+1] = num[j]
        #  插入元素
        num[left] = tem
    return num


# 快速排序 (不稳定稳定)

def quick_sort(arr, start, end):
    if start >= end:
        return
    cmp_index = start
    for i in range(start+1, end):
        if arr[i] < arr[cmp_index]:
            temp = arr[i]
            del arr[i]
            arr.insert(cmp_index, temp)
    quick_sort(arr, start=start, end=cmp_index-1)
    quick_sort(arr, start=cmp_index+1, end=len(arr))

num=[4,7,1,-2,6,3,2,3]
quick_sort(num,0,len(num))
print(num)


# 归并排序 （稳定）

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    # 分 分成左右两部分
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 合并
    def merge(arr1, arr2):
        res = []  # # 用来存最终排序好的序列
        h, j = 0, 0
        while h < len(arr1) and j < len(arr2):
            if arr1[h] < arr2[j]:
                res.append(arr1[h])
                h += 1
            else:
                res.append(arr2[j])
                j += 1
        if h == len(arr1):
            for i in arr2[j:]:
                res.append(i)
        else:
            for j in arr1[h:]:
                res.append(j)
        return res
    return merge(left, right)

a = [4, 7, 8, 3, 5, 9]
print(merge_sort(a))

 
