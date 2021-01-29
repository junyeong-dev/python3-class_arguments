class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    # method는 class안에 있는 function을 말함
    # method의 첫번째 argument는 method를 호출하는 instance 자기 자신 - 정해져있는 규칙
    def carMethod(self):
        print("method")

porche = Car()
porche.carMethod()