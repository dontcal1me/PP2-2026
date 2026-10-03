# 작성자: 윤종하
# 작성일: 20261003
# 문제: 고양이 클레스를 정의하고 몇개의 인스턴스를 생성해보자, 접근자와 설정자를
#사용해보자
# 해결하기 위한 설계: 고양이 클래스를 제작한다

class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def setName(self ,name):
        self.name = name

    def getName(self):
         print(f"Name: {self.name}")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

def test_prob1():
        cat1 = Cat("Nori", 9)
        print(cat1)
        cat1.setName("뭉이")
        print(cat1)
        cat1.getName()

if __name__ == "__main__":
     test_prob1()





    