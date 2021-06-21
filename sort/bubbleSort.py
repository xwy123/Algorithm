'''
冒泡排序
时间复杂度：O(n²), 每次冒出最大最小的元素到顶或者末端
空间复杂度：O(1)
'''

def bubbleS(array):
    length = len(array)
    for i in range(length):
        for j in range(length-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == '__main__':
    array = [5, 9, 1, 9, 5, 3, 7, 6, 1]
    res = bubbleS(array)
    print(res)
