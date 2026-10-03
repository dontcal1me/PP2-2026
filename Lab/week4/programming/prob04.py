# 작성자: 윤종하
# 작성일: 20261003
# 문제: 사각형을 나타내는 Rectangle 클래스를 작성해보자. Rectangle 클래스는 다음과 같은 인스턴스 변수와
#메소드를 가진다
# 해결하기 위한 설계 (클래스, 함수, 자료구조 등): 클래스를 제작한다.

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__ (self):
        return f"x: {self.x}, y: {self.y}, w: {self.w}, h: {self.h}"

    def setX(self, x = 0):
        self.x = x

    def getX(self):
        print(f"x : {self.x}")

    def setY(self, y = 0):
        self.y = y

    def getY(self):
        print(f"y : {self.y}")

    def setW(self, w = 1):
        self.w = w

    def getW(self):
        print(f"w : {self.w}")

    def setH(self, h = 1):
        self.h = h

    def getH(self):
        print(f"h : {self.h}")

    def getArea(self):
        return self.w * self.h

    def overlap(self, otherRe):
        return (self.x < otherRe.x + otherRe.w and
                otherRe.x < self.x + self.w and
                self.y < otherRe.y + otherRe.h and
                otherRe.y < self.y + self.h)

def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)
    print(r1.overlap(r2))

if __name__ == "__main__":
    test_prob4()