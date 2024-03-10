def MatrixAdd(A, B):
    """
    实现两个矩阵的加法
    :param A: list[list[int]] 第一个矩阵
    :param B: list[list[int]] 第二个矩阵
    :return: list[list[int]] 矩阵加法的结果
    """
    n = len(A)  
    C = [] 
    for cnt in range(n): 
        # 对每一行的对应元素进行加法操作，并添加到结果矩阵中
        C.append([i + j for i, j in zip(A[cnt], B[cnt])])
    return C  # 返回矩阵加法的结果

def MatrixMul(A, B):
    """
    实现两个矩阵的乘法
    :param A: list[list[int]] 第一个矩阵
    :param B: list[list[int]] 第二个矩阵
    :return: list[list[int]] 矩阵乘法的结果
    """
    C = []  
    tmp = [] 
    value = 0 
    n = len(A)  
    for i in range(n): 
        tmp = [] 
        for j in range(n):  # 遍历结果矩阵的每一列
            value = 0 
            for cnt in range(n):  # 进行点乘计算
                value += A[i][cnt] * B[cnt][j]
            tmp.append(value)  # 将点乘结果添加到临时列表中
        C.append(tmp)  # 将临时列表添加到结果矩阵中
    return C

#以下为测试代码，随机生成两个矩阵检测计算结果是否正确
import numpy as np
A = np.random.randint(0, 11, size=(3, 3))
B = np.random.randint(0, 11, size=(3, 3))
Mul = MatrixMul(A, B)
Add = MatrixAdd(A, B)
print(f"matrix A:\n{A}\n")
print(f"matrix B:\n{B}\n")
print(f"matrix A * B:\n")
print(f"{Mul}\n")
print(f"matrix A + B:\n")
print(f"{Add}\n")