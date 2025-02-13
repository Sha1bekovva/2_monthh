class Person:
   def __init__(self, fullname, age, is_married):
       self.fullname = fullname
       self.age = age
       self.is_married = is_married
   def introduce_myself(self):
       marital_status = "married" if self.is_married else "single"
       print(f"Fullname: {self.fullname}, Age: {self.age}, Marital Status: {marital_status}")
class Student(Person):
   def __init__(self, fullname, age, is_married, marks):
       super().__init__(fullname, age, is_married)
       self.marks = marks
   def average_marks(self):
       if self.marks:
           return sum(self.marks.values()) / len(self.marks)
       return 0
class Teacher(Person):
   def __init__(self, fullname, age, is_married, experience):
       super().__init__(fullname, age, is_married)
       self.experience = experience
   base_salary = 50000
   def calculate_salary(self):
       bonus = 0.05 * (self.experience - 5) * self.base_salary if self.experience > 5 else 0
       return self.base_salary + bonus
teacher = Teacher("Nooruz", 35, True, 7)
teacher.introduce_myself()
print(f"Salary: {teacher.calculate_salary()}")
def create_students():
   student1 = Student("Jumagul", 20, False, {"Math": 85, "English": 90, "History": 88})
   student2 = Student("Maksat", 22, True, {"Math": 78, "English": 82, "History": 80})
   student3 = Student("Ayzat", 21, False, {"Math": 92, "English": 89, "History": 85})
   return [student1, student2, student3]
students = create_students()
for student in students:
   student.introduce_myself()
   print(f"Average Marks: {student.average_marks()}")


