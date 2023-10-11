#################################################################################################
# # 클래스
# # 구현하고자 하는 대상을 모듈(파트, 코드블럭) 별로 나누어서
# # 미리 설계(작성, 프로그래밍)하여 프로그램 구현시 필요한 부분에서 호출(인스턴스 화)하여 사용하는 기능
#################################################################################################
# # 캡슐화
# # 연관있는 기능들을 클래스에 등록하여 두고 클래스 인스턴스가 호출하여 사용할 수 있는 클래스 내부에 필요한 기능들을 구성하는 단계
# # 인스턴스 변수
# # 인스턴스화 된 객체에서 단독으로 사용할 수 있는 변수

# # 클래스 생성과 캡슐화, 클래스의 인스턴스화 예제
# class Account: # 클래스 이름 및 클래스 생성 선언
#     # 클래스 생성자 멤버(클래스가 인스턴스화 될 때 자동으로 호출)
#     def __init__(self, blance, bankname):
#         # 생성자는 클래스 인스턴스 변수 초기화
#         self.blance = blance # self.blance :
#                              # - Account 클래스의 인스턴스 변수
#                              # - 객체가 소멸되기 전까지 계속 객체 별로 값을 유지한다
#         self.bankname = bankname

#     # 클래스의 메서드 멤버
#     # 개발자가 클래스를 사용하기 위하여 필요한 로직을 임의로 작성해 두는 곳
#     # 예금 관련 메서드
#     def deposit(self, money):
#         # 객체의 잔액을 증가
#         self.blance += money

#     def withdraw(self, money):
#         # 객제의 잔액을 차감
#         self.blance = self.blance - money

#     def inquire(self):
#         # 은행별 잔액을 확인
#         return self.bankname, self.blance
    
# # Account 클래스의 인스턴스화 및 객체화
# # 인스턴스화 : 클래스를 heap 메모리 영역에 등록
# # 객체화 : stack에 등록해 둔 객체의 이름에 클래스 인스턴스 주소를 전달하는 과정

# # sinhan 이라는 객체에 Account 클래스를 인스턴스화하여 주소를 전달(객체화)
# sinhan = Account(8000, "신한은행")
# sinhan.deposit(10000)
# # sinhan 객체의 이름과 잔고를 알고 싶을 때
# info = sinhan.inquire()
# print("%s 은행의 잔고는 %d입니다" %(info[0], info[1]))

# nonghyup = Account(10000, "농협은행")
# nonghyup.withdraw(2000) # 농협 계좌에서 2000원을 인출
# info = nonghyup.inquire()
# print("%s 은행의 잔고는 %d입니다" %(info[0], info[1]))
# balace라는 민감한 정보를 외부에 노출하지 않고 주어진 기능으로만 은행의 업무를 수행하는 프로그래밍을 구현할 수 있다




###########################################################################################################
# # 클래스 상속
# # 공통 기능을 구현하는 클래스(부모클래스)를 구현해 두고 부모 클래스를 상속받은 자식 클래스는 각각 특징적인 기능을 구현하게 한다
# # 공통 기능을 하나로 만들어 두고 호출하는 방식으로 재사용성과 유지 보수성을 향상시킬 수 있다

# # 다른 클래스에 상속을 할 부모 Human 클래스
# class Human:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

#     def intro(self):
#         print(f"저는 {self.age}살 {self.name}입니다")


# class Student(Human):
#     def __init__(self, age, name, ID):
#         self.age = age # 부모 클래스의 age 인스턴스 변수
#         self.name = name # 부모 클래스의 name 인스턴스 변수
#         self.stuId = ID # Student 클래스만의 인스턴스 변수

#     def intro(self):
#         super().intro() # 나이와 이름을 소개하는 기능
#         print(f"학번은 {self.stuId}입니다")

# man = Human(25, "이상혁")
# man.intro()

# stu = Student(23, "유지민", 20191092)
# stu.intro() # student 클래스의 intro를 호출




# # 부모 클래스의 인스턴스 변수의 이름이 변경될 경우
# # 자식 클래스에서 지칭한 age와 name은 더 이상 부모 클래스의 인스턴스 변수를 바라보지 않는다
# # 부모 클래스의 intro()를 호출시 초기화 오류가 발생한다
# class Human:
#     def __init__(self, age, name):
#         # 
#         self.age_F = age
#         self.name_F = name

#     def intro(self):
#         print(f"저는 {self.age_F}살 {self.name_F}입니다")


# class Student(Human):
#     def __init__(self, age, name, ID):
#         super().__init__(age, name) # 부모 클래스의 init 메서드에 age와 name을 전달하고 부모클래스의 init에서 전달받은 age와 name을 각각 부모 클래스만의 인스턴스 변수에 담기 때문에 부모 클래스의 내용이 변경되어도 자식클래스의 로직에는 영향을 미치지 않는다
        
#         self.stuId = ID  # Student 클래스만의 인스턴스 변수

#     def intro(self):
#         super().intro() # 나이와 이름을 소개하는 기능
#         print(f"학번은 {self.stuId}입니다")

# # man = Human(25, "이상혁")
# # man.intro()

# stu = Student(23, "유지민", 20191092)
# stu.intro() # student 클래스의 intro를 호출
# # 부모 클래스의 age_F와 name_F가 자식 클래스에서 초기화하는 로직이 수정되지 않았다
# # 자식 클래스의 age와 name은 자식클래스만의 인스턴스 변수가 되었다
# # 부모 클래스의 Intro()를 호출할 때 초기화되지 않은 age_F, name__F를 호출하여 오류가 발생한다



# # 클래스간의 상호 의존성
# # 하나의 클래스를 상속받거나 객체화하여 사용할 경우
# # 상위 클래스 또는 대상 클래스의 로직이 변경될 때 



################################################################################
# # 파이썬 클래스의 멤버(필드, 생성자, 메서드) 외부에서 누구나 쉽게 엑세스 할 수 있다
# # 클래스 내부의 민감한 데이터를 보호하는 패턴
################################################################################

# # 1. 일정한 규칙을 마련해두고 외부의 요인으로부터의 변질 막기
# class Data:
#     def __init__(self, month):
#         self.inner_month = month # inner_month 클래스에서 보호해야 할 값이 담긴 변수

# dt = Data(10)
# dt.inner_month = 100 # inner_month는 1월부터 12월까지를 나타낼 수 있지만 외부에서 직접 접근할 수 있는 구조 때문에 변질될 수 있다



# # 2. 민감한 내용을 담은 변수 자체를 공개하지 않고 관리할 수 있는 기법
# class Data:
#     def __init__(self, month):
#         self.inner_month = month # inner_month 클래스에서 보호해야 할 값이 담긴 변수
#     def getmonth(self):
#         """월을 호출받았을 때 표현할 함수"""
#         return self.inner_month
#     def setmonth(self, month):
#         """월을 입력받았을 때 세팅하는 함수
#         월은 1~12만 받을 수 있으므로 잘못된 월을 입력하였을 경우 변질을 막는 로직을 구현해 둘 수 있다"""
#         if 1 <= month <= 12:
#             self.inner_month = month
#         else:
#             print("월은 1부터 12까지만 입력할 수 있습니다")

# dt = Data(10)

# # # 월을 세팅할 때
# dt.setmonth(15) # inner_month 인스턴스 변수에 직접 접근하지 않고 외부에서 변경
# print(dt.getmonth())


# # 3. 프로퍼티를 통한 Get, Set 기능의 통합
# # getmonth() 메서드와 setmonth() 메서드가 inner_month 변수를 관리하는 메서드임을 표현하고 외부에서 접근 가능한 객체를 제공함으로서 inner_month 변수를 대신하는 역할을 하는 기능을 구현할 수 있다

# class Data:
#     def __init__(self, month):
#         self.inner_month = month # inner_month 클래스에서 보호해야 할 값이 담긴 변수
#     def getmonth(self):
#         """월을 호출받았을 때 표현할 함수"""
#         return self.inner_month
#     def setmonth(self, month):
#         """월을 입력받았을 때 세팅하는 함수
#         월은 1~12만 받을 수 있으므로 잘못된 월을 입력하였을 경우 변질을 막는 로직을 구현해 둘 수 있다"""
#         if 1 <= month <= 12:
#             self.inner_month = month
#         else:
#             print("월은 1부터 12까지만 입력할 수 있습니다")

#     month = property(getmonth, setmonth)
#     # # getmonth()와 setmonth() 메서드 자체도 공개하지 않는다

# dt = Data(10)
# # # 월을 세팅할 때
# dt.setmonth = 10
# print(dt.month)




# # 4. 프로퍼티를 데코레이터로 구현
# # 외부에 공개할 프로퍼티 이름으로 get과 set에 관련된 메서드를 작성해두고 데코레이터를 통해 getter와 setter 역할을 하는 것임을 나타낸다
class Data:
    def __init__(self, month):
        self.inner_month = month # inner_month 클래스에서 보호해야 할 값이 담긴 변수

    @property # month의 getter 메서드 기능을 적용하는 데코
    def month(self):
        """월을 호출받았을 때 표현할 함수"""
        return self.inner_month
    
    @month.setter # month 프로퍼티의 setter 메서드 기능을 적용하는 데코
    def month(self, month):
        """월을 입력받았을 때 세팅하는 함수
        월은 1~12만 받을 수 있으므로 잘못된 월을 입력하였을 경우 변질을 막는 로직을 구현해 둘 수 있다"""
        if 1 <= month <= 12:
            self.inner_month = month
        else:
            print("월은 1부터 12까지만 입력할 수 있습니다")

    month = property(month, month)
    # # getmonth()와 setmonth() 메서드 자체도 공개하지 않는다

dt = Data(10)
# # 월을 세팅할 때
dt.setmonth = 10
print(dt.month)