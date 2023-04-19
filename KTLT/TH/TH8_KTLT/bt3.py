class Student:
    def __init__(self,ID, avrmark, age, grade) -> None:
        self.ID = ID
        self.avrmark = avrmark
        self.age = age
        self.grade = grade

    def showInfo(self):
        print(f"Student's ID: {self.ID}")
        print(f"Student's average mark: {self.avrmark}")
        print(f"Student's age: {self.age}")
        print(f"Student's grade: {self.grade}")

    def Inform(self):
        if self.avrmark>8.0:
            return "Yes!"
        return "No!"
    
if __name__ == "__main__":
    flag1 = flag2 = flag3 = flag4 = False
    while True:
        ID = input("Student's ID: ")
        avrmark = int(input("Student's avrmark: "))
        age = int(input("Student's age: "))
        grade = input("Student's grade: ")
        if len(ID)!=8:
            print("Your ID is not Identified!")
        if avrmark>10 and avrmark<0:
            print("Your average mark is not correct!")
        if age<18:
            print("You entered wrong age!")
        if grade[0] not in ["A","C"]:
            print("Wrong Grade!")
        if ():
            break
    
    print("-----output-----")
    call = Student(ID, avrmark, age, grade)
    call.showInfo()
    print(f"Grant holder: {call.Inform()}")