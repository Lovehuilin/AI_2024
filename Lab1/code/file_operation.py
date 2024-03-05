def take_stu_num(elem):
    return elem[1]
def take_stu_age(elem):
    return elem[3]

class StuData():
    # 类的初始化方法
    def __init__(self, filename):
        self.data = []  # 初始化一个空列表来存储数据
        # 打开指定文件进行读取
        with open(filename) as file_object:
            # 逐行读取文件内容
            for line in file_object.readlines():
                line_data = [] 
                # 将当前行按空格分割，遍历其中的每个元素
                line_data.append(line.split()[0])
                line_data.append(line.split()[1])
                line_data.append(line.split()[2])
                line_data.append(int(line.split()[3]))
                self.data.append(line_data)  # 将整行数据作为一个元素添加到self.data中
    
    # 类的AddData方法，用于向类中添加学生信息
    def AddData(self, name, stu_num, gender, age):
        line_data = []
        line_data.append(name)
        line_data.append(stu_num)
        line_data.append(gender)
        line_data.append(age)
        self.data.append(line_data)

    
    def SortData(self, attr):
        if attr == 'stu_num':
            self.data.sort(key=take_stu_num)
        elif attr == 'age':
            self.data.sort(key=take_stu_age)
        

# 实例化StuData类，读取"student_data.txt"文件，以下是测试用例

me = StuData("student_data.txt")
me.SortData('stu_num')
print(me.data)  # 打印出处理后的数据列表
