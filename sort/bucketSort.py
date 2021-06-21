'''
桶排序：装箱排序
特点：所有排序算法中最快、最简单的
时间复杂度：O(m+n), n:遍历数据装箱，m:遍历箱子取值
空间复杂度：O(m), m:箱子的个数
'''

def bucketS(array):
    array_max = max(array)
    array_min = min(array)
    bucket = [0] * ((array_max - array_min) + 1)
    for i in range(len(array)):
        bucket[array[i] - array_min] += 1
    
    res = []
    for i in range(len(bucket)):
        res += [i + array_min]*bucket[i]
    
    return res

if __name__ == '__main__':
    array = [5, 9, 1, 9, 5, 3, 7, 6, 1]
    res = bucketS(array)
    print(res)