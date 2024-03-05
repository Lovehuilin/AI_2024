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
