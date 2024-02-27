def MatrixAdd(A, B):
    """
    :param A: list[list[int]]
    :param B: list[list[int]]
    :return: list[list[int]]
    """
    n = len(A)
    C = []
    for cnt in range(n):
        C.append([i + j for i, j in zip(A[cnt], B[cnt])])
    return C

def MatrixMul(A, B):
    """
    :param A: list[list[int]]
    :param B: list[list[int]]
    :return: list[list[int]]
    """
    C = []
    tmp = []
    value = 0
    n = len(A)
    for i in range(n):
        tmp = []
        for j in range(n):
            value = 0
            for cnt in range(n):
                value += A[i][cnt] * B[cnt][j]
            tmp.append(value)
        C.append(tmp)
    return C