class animal:
    def __init__(self,name, age):
        self.name=name
        self.age=age


    def eat(self):
        print(f"{self.name} їсть ")


    def sleep(self):
        print(f"{self.name} спить")



class dog(animal):
    def bark(self):
        print(f"{self.name} гавкає: Гав-гав!")


class cat(animal):
    def mew(self):
        print(f"{self.name} нявкає: Няв-няв!")



sobaka = dog("Бобік", 3)
kit = cat("Мурчик", 2)

sobaka.eat()
sobaka.sleep()
sobaka.bark()

print()

kit.eat()
kit.sleep()
kit.mew()