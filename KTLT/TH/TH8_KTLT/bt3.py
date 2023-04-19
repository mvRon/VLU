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
    while True:
        flag1 = flag2 = flag3 = flag4 = False
        ID = input("Student's ID (8 characters): ")
        avrmark = int(input("Student's avrmark (0 - 10): "))
        age = int(input("Student's age (>=18): "))
        grade = input("Student's grade (A or C): ")
        
        
        if len(ID)!=8:
            print("Your ID is not Identified!")
            flag1 = True
        if avrmark>10 or avrmark<0:
            print("Your average mark is not correct!")
            flag2 = True
        if age<18:
            print("You entered wrong age!")
            flag3 = True  
        if grade[0] not in ["A","C"]:
            print("Wrong Grade!")
            flag4 = True  
        if (flag1 == False and flag2 == False and flag3 == False and flag4 == False):
            break 
        print(f"flag1 = {flag1}")
        print(f"flag2 = {flag2}")
        print(f"flag3 = {flag3}")
        print(f"flag4 = {flag4}")

    
    print("-----output-----")
    call = Student(ID, avrmark, age, grade)
    call.showInfo()
    print(f"Grant holder: {call.Inform()}")