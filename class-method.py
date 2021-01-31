class Car():

    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        # get("k", "d") : k는 key, d는 default를 가리킴
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "2000")

    # method는 class안에 있는 function을 말함
    # method의 첫번째 argument는 method를 호출하는 instance 자기 자신 - 정해져있는 규칙
    def carMethod(self):
        print("method")

    # __str__ : 호출될 때마다 class의 instance를 출력
    # 기본적은 내장 method인 __str__을 override
    def __str__(self):
        return "__str__ override"

# inherit(상속)
class Convertible(Car):

    def __init__(self, **kwargs):
        # super() : 부모 class를 호출함
        # 부모의 init을 호출함으로써 부모의 init과 자식만의 init을 둘다 가지게 됨
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "take off"

porche = Car(color = "blue", price = "5000")
porche.carMethod()

# dir : class안에 있는 모든 properties를 보여줌
print(dir(Car))

print(porche.__str__())
print(porche.color, porche.price)

benz = Car()
print(benz.color, benz.price)

bmw = Convertible()
print(bmw.take_off())