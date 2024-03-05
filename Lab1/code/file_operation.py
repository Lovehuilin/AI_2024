# 定义一个名为StuData的类
class StuData():
    # 类的初始化方法
    def __init__(self, filename):
        self.data = []  # 初始化一个空列表来存储数据
        # 打开指定文件进行读取
        with open(filename) as file_object:
            # 逐行读取文件内容
            for line in file_object.readlines():
                line_data = []  # 为当前行创建一个空列表来存储数据
                # 将当前行按空格分割，遍历其中的每个元素
                for item in line.split():
                    line_data.append(item)  # 将元素添加到当前行的列表中
                self.data.append(line_data)  # 将整行数据作为一个元素添加到self.data中
# 实例化StuData类，读取"student_data.txt"文件，以下是测试用例
"""
me = StuData("student_data.txt")
print(me.data)  # 打印出处理后的数据列表
"""