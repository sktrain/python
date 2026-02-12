class Person:
    def __init__(self, name, gender, alter):
        self.name = name
        self.gender = gender
        self.__alter = alter


    def getAlter(self):
        return self.__alter

    def setAlter(self, alter):
        self.__alter = alter

    def print_beschreibung(self):
        print("Name: " + self.name + "\nGender: " + self.gender + "\nAlter: " + str(self.__alter))


class Pensionierter(Person):
    def __init__(self, name, gender, alter, rente):
        self.__rente = rente
        super().__init__(name, gender, alter)

    def getRente(self):
        return self.__rente

    def setRente(self, rente):
        self.__rente = rente



########################### Test
person = Pensionierter("Rentner", "male", 70, 2000)
person.print_beschreibung()

