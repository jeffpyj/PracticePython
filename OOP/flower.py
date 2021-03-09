class Flower:

    def __init__(self, name, petal_count, price):
        if type(name) is not str:
            raise TypeError("name must be a string")
        if type(petal_count) is not int:
            raise TypeError("petal count must be an int")
        if type(price) is not int and type(price) is not float:
            raise TypeError("price must be a number")
        self._name = name
        self._petal_count = petal_count
        self._price = price

    def get_name(self):
        return self._name
    
    def get_petal_count(self):
        return self._petal_count
    
    def get_price(self):
        return self._price

    def set_name(self, name):
        if type(name) is not str:
            raise TypeError("name must be a string")
        self._name = name
        return True
    
    def set_petal_count(self, petal_count):
        if type(petal_count) is not int:
            raise TypeError("petal count must be an int")
        self._petal_count = petal_count
        return True

    def set_price(self, price):
        if type(price) is not int and type(price) is not float:
            raise TypeError("price must be a number")
        self._price = price
        return True