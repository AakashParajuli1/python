class Car:
    wheels = 4     # These are called class variables( declared inside class and outside the constructor)
    # These are fixed in value  but can be changed or modified too.

    def __init__(self, make, model, year, color):       # (special method)a constructor that makes objects for us
        self.make = make                  # Attributes that the car might have.
        self.model = model                # Here,'self' is an argument referring to the object  using this method.
        self.year = year                     # And self argument does not need to be passed by us its done automatically
        self.color = color                   # All these variables declared are called 'Instance variables'.

    def drive(self):                             # Methods being used
        print("This " + self.make + " is driving.")  # We can use self to use the object we have given in other program

    def stop(self):
        print("This car is stopped.")
