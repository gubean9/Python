###########################################
# # 파일을 다루는데 사용되는 모듈 shutil. os
# # 파일을 이동, 복사
###########################################
# # 파일 복사의 예제
# import shutil

# shutil.copy("word.txt", "word2.txt")

##################################################################
# # 절대 경로 : 루트부터 파일의 이름까지를 나타낸 경로(C:\User\a.exe)
# # 상대 경로 : 특정 파일의 이름만 나타낸 것(a.exe)


# 파일의 절대 경로를 문자열로 만들기
# import os

# # 현재 스크립트의 파일 경로
# script_path = os.path.abspath(__file__)

# # 현재 스크립트 파일이 위치한 디렉토리 이름까지만 걸러내기
# script_dir = os.path.dirname(script_path)

# # 파일의 절대 경로를 표현할 파일 상대 경로
# file_abs = "word.txt"

# # 절대 파일 경로 만들어주는 함수
# # 운영 체제에 따라 파일 경로를 지정하는 표현식이 다르다
# # window : \, mac, unix : /
# # join시 절대 경로의 표현식을 운영체제에 맞게 표현해준다
# file_full_path = os.path.join(script_dir, file_abs)

# print("특정 파일의 {0}의 절대경로{1}".format(file_abs,file_full_path))




#########################
# # 파일 검색 및 출력하기
# # 1. 폴더 내의 항목 검색
# import os
# filelist = os.listdir("C:\Python\MP3")
# for file in filelist:
#     print(file)


# # 2. 함수의 재귀 호출을 통해 폴더에 존재하는(n개의 폴더 포함) 모든 mp3 파일 찾기
# import os

# # 폴더를 검색하는 함수
# def searchDir(dirpath):
#     # 해당 폴더에 있는 모든 파일의 리스트 작성
#     filelist = os.listdir(dirpath)
#     for file in filelist:
#         fullpath = os.path.join(dirpath, file) # C:\Python\MP3\2022
#         if os.path.isdir(fullpath) : # fillpath
#             print("[" + fullpath, "]")
#             searchDir(fullpath) # 재귀함수 호출 : 더 이상 폴더가 없을때까지
#         else: # 절대 경로가 폴더 유형이 아닐 경우
#             print("\t" + fullpath) # C:\Python\MP3\2022\a.mp3

# # 검색하기 위한 폴더 명칭을 인수로 전달
# searchDir(r"C:\Python\MP3")



##################################################################################
# # 실습
# # 위의 예제를 이용하여 메인 폴더의 항목은 들여쓰기가 되지 않은 상태로 출력되도록 수정
##################################################################################
import os

def searchDir(dirpath):
    filelist = os.listdir(dirpath)
    for file in filelist:
        fullpath = os.path.join(dirpath, file)
        if os.path.isdir(fullpath) :
            print("[" + fullpath, "]")
            searchDir(fullpath)
        # elif os.path.isdir()
        else:
            print("\t" + fullpath)

searchDir(r"C:\Python\MP3")










##########################
# # 추후 받은 코드 추가하기
##########################



