class Auto:
    brand = "Lada"
    model = "Kalina"
    color = "White"

    def disp_info(self):
        print(f"automobile: {self.brand}, {self.model}, {self.color}")

auto = Auto()
auto.model = "Priora"
print(auto.brand)
auto.disp_info()

