# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



#  方法1：
# 把每一列看成有序递增的数组，
# 利用二分查找，通过遍历每一列得到答案，时间复杂度是nlogn

class Solution:
    # array 二维列表
    def Find(self, target, array):
        low = 0
        high = len(array) - 1
        cloum = len(array[0]) - 1
        for i in range(cloum+1):
            while low <= high:
                mid = (low+high)//2
                if target > array[mid][i]:
                    low = mid + 1
                elif target < array[mid][i]:
                    high = mid - 1
                else:
                    return True
        return False
        
 


#  方法2：
#利用二维数组由上到下，由左到右递增的规律，那么选取右上角或者左下角的元素a[row][col]与target进行比较，
#当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,即col--；
# 当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,即row++；

class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array) - 1
        high = len(array) - 1
        cloum = len(array[0]) - 1
        i, j = row, 0
        while i >= 0 and j <= cloum:
            if target > array[i][j]:
                j += 1
            elif target < array[i][j]:
                i -= 1
            else:
                return True
        return False
