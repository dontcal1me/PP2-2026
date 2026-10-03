# 작성자: 윤종하
# 작성일: 20261003
# 문제: 로켓을 나타내는 Rocket 클래스를 작성해보자 
# 해결하기 위한 설계 (클래스, 함수, 자료구조 등): 클래스를 제작한다

class Rocket():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"로켓의 X 좌표: {self.x}, 로켓의 Y 좌표: {self.y}\n"

    def moveUp(self, incr:int = 1 ):
        self.y += incr

def test_prob2():
    rk1 = Rocket(10 , 0)
    print(rk1)
    rk1.moveUp()
    print(rk1)
    rk1.moveUp(11)
    print(rk1)
    

if __name__ == "__main__":
    test_prob2()