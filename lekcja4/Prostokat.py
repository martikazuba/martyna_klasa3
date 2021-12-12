class Prostokat:

    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by

    @property
    def dlugosc_x(self):
        return abs(self.ax - self.bx)

    @property
    def dlugosc_y(self):
        return abs(self.ay - self.by)

    @property
    def pole(self):
        return self.dlugosc_x * self.dlugosc_y

    @property
    def obwod(self):
        return 2 * self.dlugosc_x + 2 * self.dlugosc_y
