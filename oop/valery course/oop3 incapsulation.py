class Auto:
    
    def __init__(self, brand, model, color):
        self.__brand = "Reno"
        self.__model = "logan"
        self.__color = color

    def __del__(self):
        print(self.__brand, self.__model, "удален")

    def disp_info(self):
        print(f"automobile: {self.__brand}, {self.__model}, {self.__color}")



auto = Auto("Metalic")
auto.disp_info()



del auto
