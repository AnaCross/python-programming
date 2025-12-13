import Living_places.Property as Property


class House(Property.Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'{self.area} {self.rooms} {self.price} {self.address} {self.plot}'