class Dog():
    #Public / Private attributes
    def __init__(self, dogName, myColour):
        self.__name = dogName
        self.__colour = myColour

    def bark(self, barkTimes):
        for n in range(barkTimes):
            print(self.__name + " says Woof!")


    def setColour(self, mycolour):
        self.__colour = myColour

    def getColour(self):
        return self.__myColour

    def getName(self):
        return self.__myName

    def printDogDetails(self):
        print(self.__name, self.__myColour)
        
    def get_colour(self):
        return self.colour


class Puppy(Dog):
    def __init__(self, dogName, myColour, dateOfBirth):
        super().__init__(dogName, myColour) # Dog Constructor
        self.__shoesChewed = 0


    #public procedure chewShoe (myShoesChewed)
    def chewShoe(self, myShoesChewed):
        self.__shoeschewed = self.__shoesChewed + myShoesChewed

    def getShoesChewed(self):
        return self.__shoesChewed

    def getDofB(self):
        return self.__dateofBirth
    
    def bark(self, barkTimes):
        super().bark(1)
        for n in range (barkTimes):
            print("Yap!")

        
myDog1 = Dog('Fido', 'Black', '21st of March')
myDog2 = Dog('Bonie', 'Golden')
myDog3 = Dog('James','Pink')
myDog4 = Dog('John','Blue')
myDog5 = Dog('Jack','Brown')
puppy1 = Puppy('Malla', 'light brown')
puppy2 = Puppy('J', 'Black')
puppy1.bark(2)
myDog3.bark(3)





print("Polymorphism in action:")
my_animal_list = [myDog1,myDog2,puppy1,myDog3,myDog4,puppy2]
for animal in my_animal_list:
    animal.bark(3)
    print(myDog1.getDofB)


#my_dog1.name = 'Fido'
#my_dog2.name = 'Rex'

##my_dog1.set_colour('Brown')
##my_dog1.set_colour('XYZ')
##my_dog2.set_colour('Black')
##
##print(my_dog1.name)
##print(my_dog1.get_colour())
##
##print(my_dog2.name)
##print(my_dog2.get_colour())
