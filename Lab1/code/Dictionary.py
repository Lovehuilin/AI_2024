def ReverseKeyValue(dict1):
    """
    实现一个字典中键和值的反转
    :param dict1: dict 输入的原始字典
    :return: dict 反转键和值后的新字典
    """
    res = {}  # 初始化一个空字典，用于存储反转后的键值对
    for k, v in dict1.items():  # 遍历输入字典的键值对
        res[v] = k  # 将原字典的值作为键，键作为值，添加到新字典中
    return res  # 返回反转键和值后的字典
