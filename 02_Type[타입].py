#########################################################
# # 정수형 타입
# # 파이썬의 정수는 크기에 구애없이 모든 숫자를 담을 수 있다
# # 정수의 크기에 따라서 가변적으로 데이터 형식이 변형된다
#########################################################
# # 정수 타입의 변수 a에 2의 100승 결과를 할당 후 출력

# # 다회성
# a = 2 ** 100
# print(a)

# # 일회성
# print(2**100)

# # 음수도 표현 가능
# a = 2 ** 1000 * -1
# print(a)



###############
# # 진법의 표현
###############
# print(0b11) # 2진수 11을 10진수로 표현
# print(0o10) # 8진수 10을 10진수로 표현
# print(0xb)  # 16진수 b를 10진수로 표현

# # # 다른 진법으로 숫자 표현
# print(bin(3)) # 10진수 3을 2진수으로
# print(oct(8)) # 10진수 8을 8진수으로
# print(hex(11)) # 10진수 11을 16진수로



#################################
# # 실수형
# # 소수점 이하의 숫자 데이터 유형
#################################
# light = 10 # 정수형
# light = 10.1223 # 실수형

# # # 실수형의 다른 표현(부동소수점)
# light = 9.46e12 # e12 : 10의 12승
# print(light)
# light = 9.42 * 10**12
# print(light)



############################################
# # 문자열
# # 일련의 문자를 따옴표로 감싸 나열해 둔 형식
# # 쌍따옴표, 홑따옴표
############################################
# # 확장열
# # 문자열을 나타내는 따옴표 내의 프로그래밍 동작 기능
# # ' \ ' 역슬래쉬로 표현
# print("안녕하세요 \"파이썬\" 문법 중 \n 확장렬에 관한 예시입니다")

# # \\를 많이 사용하는 문자열(파일의 경로)
# # r"문자열\"을 사용하면 \를 여러 번 사용하지 않고 표현
# print("C:\\Python\\Source") # 경로를 나타내는 문자열은 r을 통해 \를 한 번만 쓸 수 있다
# print(r"C:\Python\Source") # 경로 r 사용 예시

# # 장문의 문자열 표현
# # 삼겹따옴표 [ """ """ ] 또는 [ ''' ''' ]를 통하여 장문의 문자열을 관리할 수 있다~
# Message = '''안녕하세요
# 안동대학교
# 스마트팩토리 파이썬 수업입니다.
# '''
# print(Message)

# # 다른 표현법1
# Message = "안녕하세요"
# message2 = "안동대학교"
# message3 = "파이썬입니다"
# print(Message)
# print(message2)
# print(message3)

# # 다른 표현법2
# print(Message + '\n' + message2 + '\n' + message3)

# # 삼겹따옴표 [ """ """ ] 내의 \는 개행을 막아준다
# Message = '''안녕하세요 \
# 안동대학교 \
# 스마트팩토리 파이썬 수업입니다. \
# '''
# print(Message)



#############################################################################
# # 문자코드와 문자
# # ord()와 chr()
# # ord() : 문자를 아스키코드로
# # chr() : 아스키코드를 문자로
# # 이기종(기종이 다른 환경)간의 통신에서 사용하는 진법 또는 코드 규칙을 통일하여
# # 처리된 값과 결과를 일치시키기 위해 변형하는 문법
#############################################################################
# a = ord('a') # 문자 'a'의 코드 값을 a 변수에 할당 a의 아스키코드 출력
# b = chr(97) # 10진 코드값 97을 문자로 반환하여 표현 아스키코드 97의 문자값 출력
# print(a)
# print(b)

# c = chr(0x61)
# print(c)

# d = chr(0b1100001) # 2진수를 변환해서 97
# print(d)



##########################################################################################
# # 진위형 True/False
# # 참과 거짓을 1과 0으로 표현, 가독성이 좋은 코드를 수현하도록 True/False로 표현하기 위해 발생
# # True/False 첫 문자는 대문자로 표현
##########################################################################################
# # 진위 데이터의 할당
# a = True
# b = False

# # 진위형의 활용
# a = 5      # a는 5라는 값을 할당받는다
# b = a == 5 # a가 5라는 값을 가지고 있으므로 b는 True를 할당받는다



#####################################################################
# # None
# # 아무런 값이 할당되지 않은 생타 타언어에서는 null
# # 아파트 계약을 해서 세대주가 되었는데 실제 아파트는 건축되지 않은 상태
# # null과 차이점 알아두기 / 나중에 꼭 잘 봐야함
#####################################################################
# a = None
# print(a == None)
# print(a)

# a = '' # ''은 값이 없는 데이터가 할당된 상태. 메모리에 정상적으로 등록이 된 상태



#####################################################################
# # 컬렉션(다양한 컬렉션은 추후에 확인)
# #   - 데이터의 집합(데이터가 등록된 메모리 주소를 관리하는 객체)

# # 리스트
# #   - 동일한 데이터 유형의 값을 하나의 집합으로 묶어 특정 변수에 할당하는 형태
# #   - 데이터를 변경할 수 있다
#####################################################################
# # 리스트의 생성과 사용
# valuse = ["값1", "값2", "값3", "값4"]
# print(valuse[1])
# valuse[0] = "가앖1"
# print(valuse[0])

# # # 튜플의 생성과 값의 변경
# valuse = ("값1", "값2", "값3", "값4")
# print(valuse[0])
# valuse[0] = "가앖2"



#################################################################################
# # 실습
# # 문자 리스트 1, 2, 3, 4, 5를 만들고 첫번째 값[0]과 3번째[2] 값의 합을 나타내보세요
#################################################################################
list = ['1', '2', '3', '4', '5']
print(int(list[0]) + int(list[2]))