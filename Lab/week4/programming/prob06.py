# 작성자: 윤종하
# 작성일: 20261003
# 문제: Person 이라는 클래스를 작성해보자
# 해결하기 위한 설계 (클래스, 함수, 자료구조 등): 클래스를 제작한다.

class Person:
    def __init__(self, n, m="없음", o="없음", e="없음"):
        self.n = n
        self.m = m
        self.o = o
        self.e = e

    def getN(self):
        print(self.n)

    def setN(self, n):
        self.n = n

    def getM(self):
        print(self.m)

    def setM(self, m):
        self.m = m

    def getO(self):
        print(self.o)

    def setO(self, o):
        self.o = o

    def getE(self):
        print(self.e)

    def setE(self, e):
        self.e = e

    def __str__(self):
        return f"Name: {self.n}, mobile: {self.m}, office: {self.o}, email: {self.e}"


def test_prob5():
    p = Person("김철수")
    print(p)

    p.setN("윤종하")
    p.setM("010-1234-5678")
    p.setO("02-123-4567")
    p.setE("yjs893355@gmail.com")
    p.getN()
    p.getM()
    p.getO()
    p.getE()


if __name__ == "__main__":
    test_prob5()
