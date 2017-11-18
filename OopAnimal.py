class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def displayHealth(self):
        print 'My name is: ' + self.name
        print 'Your health level is' + str(self.health)
    
animal = Animal('Garfield')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

dog = Dog('Blackie')
dog.walk().walk().walk().run().run().displayHealth()
    
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon,self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        print 'I am a dragon'
        super(Dragon,self).displayHealth()

dragon = Dragon('Fire Breather')
dragon.fly().displayHealth()