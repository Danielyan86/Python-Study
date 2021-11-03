# 1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
# 2、创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出.
# - 创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息.
# - 重写__str__方法，返回student的信息。
# 3、创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。
# - 创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序
# 4、创建三个学生对象，分别打印其详细信息
# 5、创建一个老师对象，打印其详细信息
# 6、学生对象调用learn方法
# 7、将三个学员添加至列表中，通过循环将列表中的对象打印出来，print(Student对象)。
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def person_info(self):
        print(self.name, self.gender, self.age)


class Student(Person):
    def __init__(self, name: str, gender: str, age: str, college: str, class_stu: str):
        super().__init__(name, gender, age)
        self.college = college
        self.class_stu = class_stu

    def person_info(self):
        super().person_info()
        print(self.college, self.class_stu)

    def study(self, teacher):
        print(teacher.teach())
        print("学会了")

    def __str__(self):
        return f"name: {self.name}, gender:{self.gender}, age:{self.age}, college: {self.college}" \
               f" class: {self.class_stu}"


class Teacher(Person):
    def __init__(self, name: str, gender: str, age: str, college: str, professional: str):
        super().__init__(name, gender, age)
        self.college = college
        self.professional = professional

    def person_info(self):
        super().person_info()
        print(self.college, self.professional)

    def teach(self):
        return ("今天讲了如何用面向对象设计程序")

    def __str__(self):
        return f"name: {self.name}, gender:{self.gender}, age:{self.age}, college: {self.college}, professional: {self.professional}"


class Teach:
    def __init__(self, student: Student, teacher: Teacher):
        self.student = student
        self.teacher = teacher


if __name__ == '__main__':
    xiaohong = Student("xiaohong", "female", "18", "engineer", "1")
    xiaohong.person_info()
    mr_liu = Teacher("liu", "male", "33", "engineer", "electronic technology")
    xiaohong.study(mr_liu)
    print(xiaohong)
    print(mr_liu)
