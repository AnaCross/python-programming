import Living_places.Property as Property


class Flat(Property.Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'{self.area} {self.rooms} {self.price} {self.address} {self.floor}'
