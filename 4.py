class Product():
    pass


class Car(Product):
    def __init__(self, volume, price):
        self.volume = volume
        if not isinstance(self.volume, list) or len(volume) != 3:
            raise ValueError("invalid first argument!")
        try:
            self.price = float('{:.2f}'.format(price))
            if self.price <= 0:
                raise Exception('Invalid second argument')
        except (ValueError, TypeError):
            print("invalid second argument!")
            self.price = None

    def __str__(self):
        return f"Product's volume is: {self.volume}, and price is: {self.price}"


x = Car([12,123,123], 99)

print(x)