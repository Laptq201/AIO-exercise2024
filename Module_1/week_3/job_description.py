from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: int):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject
    
    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialty = specialist
    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialty: {self._specialty}")



class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__list_people = list()  
    
    def add_person(self, person: Person):
        self.__list_people.append(person)
    
    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__list_people:
            person.describe()
    
    def count_doctor(self):
        count = 0
        for person in self.__list_people:
            if isinstance(person, Doctor):
                count += 1
        print(count)
    
def main():
    student1 = Student(name='studentZ2023', yob=2011, grade=6)
    assert student1._yob == 2011
    student1.describe()

    teacher1 = Teacher(name='teacherZ2023', yob=1991, subject='History')
    assert teacher1._yob == 1991
    teacher1.describe()

    doctor1 = Doctor(name='doctorZ2023', yob=1981, specialist='Endocrinologists')
    assert doctor1._yob == 1981
    doctor1.describe()

    student1 = Student(name='studentA', yob=2010, grade='7')
    teacher1 = Teacher(name='teacherA', yob=1969, subject="Math")
    teacher2 = Teacher(name='teacherB', yob=1995, subject="History")
    doctor1 = Doctor(name='doctorA', yob=1945, specialist='Endocrinologists')
    doctor2 = Doctor(name='doctorB', yob=1975, specialist='Cardiologists')

    ward1 = Ward(name='Ward1')
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.count_doctor()


if __name__ == '__main__':
    main()