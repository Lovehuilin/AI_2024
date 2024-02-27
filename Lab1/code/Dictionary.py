def ReverseKeyValue(dict1):
    """
    :param dict1: dict
    :return: dict
    """
    res = {}
    list1 = []
    for k, v in dict1.items():
        res[v] = k
    return res
