# 작성자: 윤종하
# 작성일: 20261003
# 문제: 삼각형을 나타내는  클래스 Triangle를 작성해보자.
# 해결하기 위한 설계 (클래스, 함수, 자료구조 등): 클래스를 제작한다.

class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def getAngle1(self):
        return self.angle1

    def setAngle1(self, angle1):
        self.angle1 = angle1

    def getAngle2(self):
        return self.angle2

    def setAngle2(self, angle2):
        self.angle2 = angle2

    def getAngle3(self):
        return self.angle3

    def setAngle3(self, angle3):
        self.angle3 = angle3

    def checkAngle(self):
        return self.angle1 + self.angle2 + self.angle3 == 180

    def __str__(self):
        return f"Triangle(angle1={self.angle1}, angle2={self.angle2}, angle3={self.angle3})"


def test_prod5():
    t = Triangle(60, 60, 60)
    print(t)
    print("내각의 합이 180인가?", t.checkAngle())

    t.setAngle1(90)
    t.setAngle2(45)
    t.setAngle3(45)
    print(t.getAngle1(), t.getAngle2(), t.getAngle3())
    print("내각의 합이 180인가?", t.checkAngle())

    t.setAngle3(50)
    print(t)
    print("내각의 합이 180인가?", t.checkAngle())


if __name__ == "__main__":
    test_prod5()
