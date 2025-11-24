class Retangulo:
    def __init__(self, b, h):
        self.base = b
        self.altura = h
    def __str__(self):
        return f"Base = {self.base}, Altura = {self.altura}"
    def area(self):
        return self.base *self.altura
    def diagonal(self):
        return (self.base**2 * self.altura**2)**0.5