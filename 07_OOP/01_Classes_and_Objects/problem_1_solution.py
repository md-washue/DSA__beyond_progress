
class Student:
    def __init__(self, name, student_ID, mark_List):
        self.name = name



        self.student_ID = student_ID
        self.mark_List = mark_List

    def add_mark(self, mark):


        self.mark_List.append(mark)

    def calculate_average(self):

        if len(self.mark_List) == 0:
            return 0

        aveg = sum(self.mark_List) / len(self.mark_List)
        return aveg

    def display_info(self):
        print("Student Information")
        print("Name:", self.name)
        print("Student ID:", self.student_ID)

        
        print("Marks:", self.mark_List)
        print("Average:", self.calculate_average())
        print("Result:", self.check_result())

    def check_result(self):
        aveg = self.calculate_average()

        if aveg >= 50:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Ali", "S001", [80, 75, 90])

student1.add_mark(85)

student1.display_info()
