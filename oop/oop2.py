class Auto:
    
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __del__(self):
        print(self.brand, self.model, "удален")

    def disp_info(self):
        print(f"automobile: {self.brand}, {self.model}, {self.color}")

auto = Auto("Reno", "logan", "Metalic")
auto.model = "Megane"
print(auto.brand)
auto.disp_info()

del auto