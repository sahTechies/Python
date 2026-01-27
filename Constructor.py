class AB:
    def __init__(self, x=None):
        if x is None:
            print("Constructor called!")
        else:
            self.a = x
    
    def data(self):
        print(f"Value of a is: {self.a}")


if __name__ == "__main__":
    o1 = AB()  # Creating an object of class AB to invoke the constructor
    o2 = AB(10)  # Creating an object with parametric constructor
    o2.data()


    //constructor 
// what are different constructor