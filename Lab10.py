class Insect(object):

    __name, __type_of_insect, __size, __sex, __number_of_legs, total_number_of_legs = "", "", 0, "", 0, 0

    def set_number_of_legs(self, number_of_legs):
        self.__number_of_legs = number_of_legs
        Insect.total_number_of_legs += number_of_legs

    def __init__(self, name="", type_of_insect="", size=0, sex="", number_of_legs=0):
        self.__name = name
        self.__type_of_insect = type_of_insect
        self.__size = size
        self.__sex = sex
        self.set_number_of_legs(number_of_legs)

    def reset_values(self, name, type_of_insect, size, sex, number_of_legs):
        self.__name = name
        self.__type_of_insect = type_of_insect
        self.__size = size
        self.__sex = sex
        self.set_number_of_legs(number_of_legs)

    def to_string(self):
        print("Name: " + self.__name + ", type_of_insect: " + self.__type_of_insect +
              ", size: " + str(self.__size) + ", sex: " + str(self.__sex) +
              ", number_of_legs: " + str(self.__number_of_legs))

    def print_number_of_legs(self):
        print("The total number of legs " + self.__name + " is " + str(self.__number_of_legs))

    @staticmethod
    def print_static_number_of_legs():
        print("The total number of legs is " + str(Insect.total_number_of_legs))


if __name__ == "__main__":
    kostia = Insect("Kostia", "mosquito", 10, "male")
    misha = Insect("Misha", "fly", 11, "female", 4)
    olena = Insect("Olena", "wasp", 12, "male", 2)

    print("Objects:")
    kostia.to_string()
    misha.to_string()
    olena.to_string()
    print("")

    misha.print_number_of_legs()
    olena.print_number_of_legs()
    Insect.print_static_number_of_legs()

    print("")
    kostia.reset_values("Kostia", "mosquito", 10, "male", 5)

    kostia.to_string()
    kostia.print_number_of_legs()
    Insect.print_static_number_of_legs()