class Polygon:

    def __init__ (self):
        pass

    def set_coords (self, coords):
        self.__coords = coords

    def get_coords (self):
        coords = []
        for i in range(4):
            coords.append(list(map(int, input())))
        return coords

    def mult_x_on_y (coords):
        out = 0
        for x in range(0, len(coords)-1):
            out += coords[x][0] * coords[x+1][1]

        return out

    def mult_y_on_x (coords):
        out = 0
        for y in range(0, len(coords)-1):
            out += coords[y+1][0] * coords[y][1]

        return out

    def calculate_square (self):
        return (Polygon.mult_x_on_y(self.__coords) - Polygon.mult_y_on_x(self.__coords))/2

    def compare_squares (polygon1, polygon2):
        print(polygon1.calculate_square()>polygon2.calculate_square())

    def in_polygon (self, dot):
        pass


polygon1 = Polygon()
coords = [[-3,-2], [-1,4], [6,1], [3,10], [-4,9], [-3,-2]]
polygon1.set_coords(coords)
polygon2 = Polygon()
coords2 = [[2,5], [6,7], [2,5], [-5, -12], [15, 7]]
polygon2.set_coords(coords2)
print(polygon1.calculate_square())
print(polygon2.calculate_square())
Polygon.compare_squares(polygon1, polygon2)