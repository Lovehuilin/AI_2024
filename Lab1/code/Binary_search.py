def BinarySearch(nums, target):
    """
    :param nums: list[int]
    :param target: int
    :return: int
    """
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r + 1) // 2
        if nums[mid] <= target:
            l = mid
        else:
            r = mid - 1
    if nums[r] == target:
        return r
    else:
        return -1