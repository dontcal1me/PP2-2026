# 작성자: 윤종하
# 작성일: 20261003
# 문제: BOX 클래스를 작성해보자 BOX는 박스의 가로,세로,높이를 나타내는 인스턴스 변수를 가진다.
# 해결하기 위한 설계 (클래스, 함수, 자료구조 등): 클래스를 제작한다

class Box:
    def __init__(self, l, h, d):
        self.l = l
        self.h = h
        self.d = d

    def setLength(self, l = 1):
        self.l = l

    def getLength(self):
        print(f"Length : {self.l}")

    def setHeight(self, h = 1):
        self.h = h

    def getHeight(self):
        print(f"Height : {self.h}")

    def setDepth(self, d = 1):
        self.d = d

    def getDepth(self):
        print(f"Depth : {self.d}")

    def __str__(self):
        return f"Length : {self.l}, Height : {self.h}, Depth : {self.d}"

    def getVolume(self):
        return self.l * self.h * self.d

def test_prob3():
    b1 = Box(100, 100, 100)
    print(b1)
    print("상자의 부피는:", b1.getVolume())

if __name__ == "__main__":
    test_prob3()
