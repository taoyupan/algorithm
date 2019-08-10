#  零钱凑整问题
'''
样例： coins = [1,2,5]
思路： 动态规划。用dp[i] 表示组成i元所需最少硬币数
显然，对于coins数组里面的所有元素j，都有dp[j] = 1
以样例输入为例：  对于其它的dp[i] = 1 + min{dp[i-1], dp[i-2], dp[i-5]}

（注： 不规定零钱的数量！）
'''

def coinChange(coins, amount):
    '''
    :type coins: List[int]
    :type amount: int
    :return: int
    '''
    if amount == 0:
        return -1
    dp = []
    max_int= amount+1  #  表示组成amount元的数量不可能为 amount+1
    for i in range(amount+1):
        if i not in coins:
            dp.append(max_int)
        else:
            dp.append(1)
    for i in range(amount+1):
        for j in coins:
            if i > j:
                dp[i] = min(dp[i], dp[i-j] + 1)
    return dp[amount] if dp[amount] != max_int else -1
    
    
    
# 找零钱问题（给定要找零钱的数目，求最少的硬币数） 贪婪算法
import sys
def main():
    d = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]  # 存储每种硬币的值
    temp = sys.stdin.readline().strip().split(' ')   # 输入每种硬币的数量
    d_num = list(map(int, temp))# 存储每种硬币的数量
    s = 0
    for i in range(len(d)):
        s += d[i]*d_num[i]   # 计算已有零钱的总数
    targe = float(sys.stdin.readline())  # 输入需要找的零钱
    if targe > s:
        return -1
    # 要想用的钱币数量最少，那么需要利用所有面值大的钱币，因此从数组的面值大的元素开始遍历
    res = {}  # 其中key是硬币值，value 是该值的个数
    for i in range(len(d)-1, -1, -1):
        if targe >= d[i]:
            n = targe//d[i]
            if n >= d_num[i]:
                n = d_num[i]
            targe -= n*d[i]
            res[d[i]] = n
    return sum(res.values())

print(main())
    
    
