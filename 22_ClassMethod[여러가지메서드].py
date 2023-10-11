###################################################################
# # 클래스 변수
# # 클래스 자체로 데이터를 관리하는 변수
# # 인스턴스화 하지 않아도 곧바로 외부에서 접근하여 관리할 수 있는 변수


# class car:
#     totalcount = 0 # 클래스 변수

#     def __init__(self, year):
#         self.year = year
#         car.totalcount += 1
    
#     totalcount = 0 # 클래스 변수

# print(car.totalcount) # 0
# pride = car(2023)
# print(pride.totalcount) # 1
# print(car.totalcount) # 1

# sm = car(2022)
# print(sm.totalcount) # 2
# print(car.totalcount) # 2

# sm.totalcount = 100
# print(sm.totalcount) # 100
# print(car.totalcount) # 20

# car.totalcount = 50
# print(sm.totalcount) # 50
# print(car.totalcount) # 50


###########################################################################
# # 클래스 메서드
# # 클래스 변수를 관리할 수 있도록 클래스 자체를 인자로 전달받을 수 있는 클래스
# # 클래스 변수를 관리할 수 있도록 Data 영역에 메서드를 등록해두는 메서드
# # 클래스 변수 자체를 외부에 공개하지 않을 수 있다(데이터보호, 접근성, 캡슐화)


# class car:
#     totalcount = 0 # 클래스 변수

#     def __init__(self, year):
#         self.year = year
#         car.totalcount += 1

#     @classmethod
#     def setcount(cls, countvolum):
#         cls.totalcount += countvolum
#         print(cls.totalcount)

# # 클래스 메서드를 호출
# car.setcount(10)


##################################################################################################################
# # 정적 메서드
# # 프로그램 전반적으로 사용하는 변수나 값, 메서드가 있을 경우 인스턴스화 하지 않고 편리하게 사용할 수 있도록 data 영역에 등록해두는 method
# # classmethod와 같은 원리이지만 클래스 변수를 관리하지 않는다



class car:
    totalcount = 0 # 클래스 변수

    def __init__(self, year):
        self.year = year
        car.totalcount += 1

    @staticmethod
    def setcount():
        return "차량 판매 수량"

# 클래스 메서드를 호출
car.setcount()