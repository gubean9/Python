#########################################################################
# # 프로그램의 연산자
# # 컴퓨터가 처리해야 할 명령어(연산)의 프로세스를 수학적인 키워드로 표현한 것
#########################################################################
# # 대입 연산자
# ivalue = 2

# # # 대입 연산 이전에 변수를 사용할 수 없다
# print(value2)
# value2 = 10

# # 변수 사용 시 반드시 초기화 해야 한다
# # 초기화 : 데이터가 최초 1회 할당된 상태(변수의 위치 정보가 메모리에 등록된 상태)
# print(ivalues)

# # 산술 연산자
# print(1 + 2)
# print(2 - 1)
# print(3 * 3)
# print(5 / 2) # 나누기 결과(몫과 나머지를 함께 표현) / 파이썬만 몫과 나머지가 함께 나오고 다른 언어는 몫만 출력
# print(5 // 2) # 나누기 결과(몫)
# print(5 % 2) # 나눈 나머지 값 출력


# # 복합대입 연산자
# # 기존의 값에 새로운 값을 누적하여 연산시 사용
# value = 100
# value = value + 10
# print(value)

# # 기존의 값에 10을 더한 누적 연산자 적용
# value += 10
# print(value)

# value -= 10
# print(value)

# value /= 10
# print(value)

# value //= 10
# print(value)

# value %= 10
# print(value)



###############
# # 타입의 변환
###############
# # # 두 문자열 간의 +
# print('안녕하세요' + '반갑습니다')

# # # 두 문자열 간의 *
# print('5번 나오게 하세요' * 5)

# # # 문자열과 정수의 합은 형변환을 해야 한다
# print('123' + str(456)) # 문자열로 나열하고 싶을 때는 문자 형변환이 필요
# print(int('123') + 456) # 값의 합을 표현하고 싶을 때는 정수형 변환이 필요

# # # 숫자로 표현 가능한 진법의 코드는 해당 진수를 표현하여 10진수로 변환한다
# print(int("1a", 16)) # 16진수 1a를 10진수로 변환하여 표현
# print(int("15", 8)) # 8진수 15를 10진수로 변환하여 표현
# print(int("100", 10)) # 10진수 100을 10진수로 표현


# # 실수 문자열의 변환
# # 실수가 포함된 문자열을 실수 형식으로 변환할 때는 flaot()함수를 사용한다
# print(float("23.2"))
# print(float("23.2e+2"))
# print(float("23.2e-3"))

# # # 실수를 정수형으로 변환할 때는 소수 이하는 버림 처리
# print(int(22.5))

# # # 문자열이 실수일 경우 곧바로 정수형으로 변환하여 표현할 수 없다
# # print(int("22.5")) # 불가능
# print(int(float("22.5"))) # 가능

# f = float("22.5")
# i = int(f)
# print(i)

# # 소수점 자르기
# # Round는 실수를 지정한 위치에서 반올림하여 표현한다
# # 0의 위치는 소수점 첫째 자리
# print(round(12.834)) # 0의 위치(소수점 첫번째자리)에서 반올림 = 13 출력
# print(round(12.834, 1)) # 소수점 두번째 자리에서 반올림 12.8
# print(round(12112.934, -3)) #


