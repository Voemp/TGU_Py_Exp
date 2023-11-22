"""面向对象编程"""


class SchoolMember:
    '''代表任何学校里的成员'''

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get(self):
        print("姓名：{}, 性别：{}, 年龄：{}".format(self.name, self.sex, self.age), end=", ")


class Student(SchoolMember):
    """代表一位学生"""

    def __init__(self, name, sex, age, classroom, sno, mark):
        super().__init__(name, sex, age)
        self.classroom = classroom
        self.sno = sno
        self.mark = mark

    def printInfo(self):
        super().get()
        print("班级：{}, 学号：{}, 成绩：{}".format(self.classroom, self.sno, self.mark))


class Teacher(SchoolMember):

    def __init__(self, name, sex, age, office, jno, wages):
        super().__init__(name, sex, age)
        self.office = office
        self.jno = jno
        self.wages = wages

    def printInfo(self):
        super().get()
        print("科室：{}, 工号：{}, 工资：{}".format(self.office, self.jno, self.wages))


# 示例用法
t = Teacher("张三", "男", 30, "计算机科学与技术", "001", 10000)
t.printInfo()
