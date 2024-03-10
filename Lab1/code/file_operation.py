def take_stu_num(elem):
    return int(elem[1])  # 获取学生学号

def take_stu_age(elem):
    return elem[3]  # 获取学生年龄

class StuData():
    def __init__(self, filename):
        self.data = []  # 初始化存储数据的列表
        # 读取文件
        with open(filename) as file_object:
            for line in file_object.readlines():
                line_data = []  # 临时存储解析的每行数据
                # 分割每行数据并转换类型，最后加入到self.data中
                line_data.append(line.split()[0])  # 姓名
                line_data.append(line.split()[1])  # 学号
                line_data.append(line.split()[2])  # 性别
                line_data.append(int(line.split()[3]))  # 年龄
                self.data.append(line_data)
    
    def AddData(self, name, stu_num, gender, age):
        self.data.append([name, stu_num, gender, age])  # 添加新的学生信息

    def SortData(self, attr):
        # 根据指定属性对数据进行排序
        if attr == 'stu_num':
            self.data.sort(key=take_stu_num)
        elif attr == 'age':
            self.data.sort(key=take_stu_age)
        
    def ExportFile(self, filename):
        with open(filename, 'w') as file_object:
            for line in self.data:
                file_object.write(line[0])
                file_object.write(' ')
                file_object.write(line[1])
                file_object.write(' ')
                file_object.write(line[2])
                file_object.write(' ')
                file_object.write(str(line[3]))
                file_object.write('\n')
        file_object.close()

# 以下是测试代码，用于测试类的各个方法是否能正确执行

test_filename = "student_data.txt"

# 实例化StuData类并测试方法
def test_class_methods():
    # 初始化StuData类
    student_data = StuData(test_filename)
    print(student_data.data)

    # 添加新的学生信息
    student_data.AddData("John", "1004", "Male", 23)
    print(student_data.data)

    # 根据学号排序
    student_data.SortData('stu_num')
    print(student_data.data)

    # 根据年龄排序
    student_data.SortData('age')
    print(student_data.data)

    # 导出数据到文件
    student_data.ExportFile('exported_data.txt')

# 运行测试
if __name__ == "__main__":
    test_class_methods()