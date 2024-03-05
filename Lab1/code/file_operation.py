def take_stu_num(elem):
    return elem[1]  # 获取学生学号

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