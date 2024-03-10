def BinarySearch(nums, target):
    """
    使用二分查找在已排序的数组中查找特定元素
    :param nums: list[int] 已排序的整数数组
    :param target: int 需要查找的目标元素
    :return: int 目标元素在数组中的索引，如果未找到则返回-1
    """
    l = 0 
    r = len(nums) - 1 
    
    # 当左边界小于右边界时，循环继续
    while l < r:
        mid = (l + r + 1) // 2  # 计算中间索引。使用(l + r + 1)确保mid向上取整，避免死循环
        
        # 如果中间元素小于等于目标值，则将左边界移动到中间位置
        if nums[mid] <= target:
            l = mid
        # 如果中间元素大于目标值，则将右边界移动到中间位置的前一个位置
        else:
            r = mid - 1
    
    # 循环结束后，检查右边界所指元素是否为目标值
    if nums[r] == target:
        return r  # 如果是，返回其索引
    else:
        return -1  # 如果不是，返回-1表示未找到

# 以下为测试程序
array = [1, 3, 8, 12, 15, 17, 22]
target_1 = 12 # 测试target在array中间的情况
target_2 = 1 # 测试target在array左边界的情况
target_3 = 22 # 测试target在array右边界的情况
target_4 = 0 # 测试target超出array左边界的情况
target_5 = 25 # 测试target超出array右边界的情况
index_1 = BinarySearch(array, target_1)
index_2 = BinarySearch(array, target_2)
index_3 = BinarySearch(array, target_3)
index_4 = BinarySearch(array, target_4)
index_5 = BinarySearch(array, target_5)
print("index of target_1 is %d\nindex of target_2 is %d\nindex of target_3 is %d\nindex of target_4 is %d\nindex of target_5 is %d\n" % (index_1, index_2, index_3, index_4, index_5))