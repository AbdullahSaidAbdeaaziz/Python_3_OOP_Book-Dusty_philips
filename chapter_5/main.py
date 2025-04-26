import math
from urllib.request import urlopen  # noqa: E402


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)

    def __str__(self):
        return f"{self.x, self.y}" # (1, 0)


class Polygon:
    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        print(points, len(points), self.vertices[0])
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i + 1])
            print(i, i + 1)
        return perimeter


class WebPage: # _WebPage__content
    def __init__(self, url):
        self.url = url
        self.__content = None

    @property
    def content(self):
        if not self._content:
            print("Reteriving New page...")
            self._content = urlopen(self.url).read()
        return self._content

# def main():
#     from time import time
    
    
#     page = WebPage('https://google.com/')
    
#     start = time()
    
#     content1 = page.content
    
#     end = time()

#     print(f"times taken: {end - start}")


# main()
points = [(1, 2), (1, 1), (2, 3)]

