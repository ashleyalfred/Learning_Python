class Dog():

    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age
        self.hours_exercised = 0

    def age_in_months(self):
        return self.age * 12

    def update_age(self, new_age):
        self.age = new_age

    def add_exercise(self, hours):
        self.hours_exercised = self.hours_exercised + hours 
        if self.had_enough_exercise(): 
            print(f"{self.name} has had enough exercise!")
        else:
            print("Not enough exercise today! Keep going!")
            print(f"you need {5- self.hours_exercised} hours more exercise today!")

    def had_enough_exercise(self):
        return True if self.hours_exercised > 5 else False


pet1 = Dog("M", "Taco", 0.5)
pet2 = Dog("F", "Luna", 0.5)
pet1.add_exercise(.5)
pet2.add_exercise(.5)



