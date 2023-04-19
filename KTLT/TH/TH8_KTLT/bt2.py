class Employee:
    def __init__(self, name, age, address, workinghours, cash) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.workinghours = workinghours
        self.cash = cash

    def show_info(self):
        print(f"Employee's name: {self.name}")
        print(f"Employee's age: {self.age}")
        print(f"Employee's address: {self.address}")
        print(f"Employee's hours working: {self.workinghours}")

    def Cash(self):
        if self.workinghours>=200:
            self.cash *= 120/100
            return self.cash
        elif(self.workinghours<200 and self.workinghours>=100):
            self.cash *= 110/100
            return self.cash
        else:
            return self.cash

if __name__ == "__main__":

    
    name = input("Employee's name: ")
    age = input("Employee's age: ")
    address = input("Employee's address: ")
    workinghours = int(input("Employee's workinghours: "))
    cash = float(input("Employee's cash: "))
    call = Employee(name, age, address, workinghours, cash)


    print("-----Output-----")
    call.show_info()
    print(f"Total {call.name}'s cash: {call.Cash()}")
