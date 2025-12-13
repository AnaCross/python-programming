class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'{self.area} {self.rooms} {self.price} {self.address}'

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'{self.area} {self.rooms} {self.price} {self.address} {self.plot}'

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'{self.area} {self.rooms} {self.price} {self.address} {self.floor}'

house = House(100, 2, 400000000, 'ala ma kota 3', 50)
print(house.__str__())
flat = Flat(20, 1, 600000000, 'ala ma kota 2', 4)
print(flat.__str__())