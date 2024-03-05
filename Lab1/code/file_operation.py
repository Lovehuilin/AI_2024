class StuData():
    def __init__(self, filename):
        self.data = []
        temp = 0
        with open(filename) as file_object:
            for line in file_object.readlines():
                    for item in line.split():
                        self.data[temp] = []
                        self.data[temp].append(item)
                    temp += 1
me = StuData("student_data.txt")
print(me.data)