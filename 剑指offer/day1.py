
#   滑动窗口的最大值
#   窗口大小 k
#  array = [2,3,4,2,6,2,5,1]  窗口个数 len(array)-k + 1  [4,4,6,6,6,5]
'''
建立一个列表存储最大值的变化，列表首位为目前最大值的坐标，之后为次大值等。
当新来一个数时，首先判断原来老大是否还管的到这里，管不到则弹出。新来的逐个与前面的值比较，比他小的就没有话语权了，直接弹出。若全都比过，弹出了，新来的就是老大。
若中间存在比不过的就存在队尾端，等待前面的人老去，管不到后边。或者本来就有空位，或者老大老去，所以新来的总是有位置的
'''

def maxslidingwindow(nums,k):
    '''
    nums 给定的数组
     k 窗口的大小
    '''
    if not nums:
        return []
    if k > len(nums) or k < 1:
        return []
    if k == 1:
        return nums
    res = [] #存储每个滑动窗口的最大值
    q = [0]  # 队列
    for i in range(len(nums)):
        if i-q[0] > k-1:
            q.pop(0)
        while len(q) > 0 and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
        if i+1 >= k:
            res.append(nums[q[0]])
    return res
