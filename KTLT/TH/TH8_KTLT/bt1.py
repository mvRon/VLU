class Math:
    def __init__(self,number_1, number_2) -> None:
        self.number_1 = number_1
        self.number_2 = number_2
    
    def info(self):
        print(f"Number 1: {self.number_1}")
        print(f"Number 2: {self.number_2}")
    
    def addition(self):
        return self.number_1 + self.number_2

    def substract(self):
        return self.number_1 - self.number_2
    
    def multiply(self):
        return self.number_1 * self.number_2
    
    def divide(self):
        return self.number_1 / self.number_2
    
if __name__ == "__main__":
    number_1 = float(input("Number 1:"))
    number_2 = float(input("Number 2:"))
    call = Math(number_1, number_2)
    print("=============================")
    call.info()
    print(f"{number_1} + {number_2} = {call.addition()}")
    print(f"{number_1} - {number_2} = {call.substract()}")
    print(f"{number_1} * {number_2} = {call.multiply()}")
    print(f"{number_1} / {number_2} = {call.divide()}")




    
        
    

