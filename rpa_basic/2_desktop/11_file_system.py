import os

# print(os.getcwd())  # current working directory
# os.chdir("code") # 작업공간 이동
# os.chdir("..") # 상위폴더
# os.chdir("../..") # 조부모 폴더로 이동
# os.chdir("c:/") # 절대 경로로 이동

# 파일 절대경로
# filepath = os.path.join(os.getcwd(), "my_file.txt")

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"G:\code\rpa\my_file.txt")) # r 은 문자를 있는 그대로 찍어준다( \ 역슬래쉬 등등도 그대로)

# 파일 정보 가져오기
# import time
# import datetime

# print(os.getcwd())
# file_path = "rpa_basic/2_desktop/11_file_system.py"
# # 파일 생성 날짜
# ctime = os.path.getctime(file_path)
# # print(ctime)
# # 날짜 정보를 strftime 통해 형식을 바꾼다.
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))

# # 파일 수정 날짜
# mtime = os.path.getmtime("sample.xlsx")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S"))

# # 파일 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y-%m-%d %H:%M:%S"))

# # 파일 크기 
# size = os.path.getsize(file_path)
# print(size) # 바이트 단위

# 파일 목록 가져 오기
# print(os.listdir())  # 모든 폴더, 파일 목록
# print(os.listdir("rpa_basic"))  # 디렉토리만 가져옴
# result = os.walk("rpa_basic") # 하위 폴더 포함 모두 가져옴
# # print(result)

# for root, dirs, files in result:
#   print(root, dirs, files)

# 폴더내 파일 찾기
# name = "10_log.py"
# result = []
# for root, dirs, files in os.walk("."):
#   if name in files:
#     result.append(os.path.join(root, name))

# print(result)

# 폴더내 특정 패턴을 가진 파일들을 찾으려면
# import fnmatch
# pattern = "*mouse*.py"
# result = []
# for root, dirs, files in os.walk("."):
#   for name in files:
#     if fnmatch.fnmatch(name, pattern):
#       result.append(os.path.join(root, name))

# print(result)

# 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic"))

# 주어진 경로 또는 파일이 존재하는가?
# if os.path.exists("rpa_basic"):
#   print("파일 또는 폴더 존재")
# else:
#   print("존재하진 않습니다.")

# 파일생성
# open("new_file.txt", "a").close()  # 빈 파일 생성

# 파일명 변경
# os.rename("new_file.txt", "new2_file.txt")

# Delete
# os.remove("new2_file.txt")

# 폴더 생성
# os.mkdir("new_folder")
# os.makedirs("new_folder/a/b/c")  하위 폴더들 생성

# 폴더 삭제
# os.rmdir("new_folder") 폴더 비어 있을 때만 삭제
import shutil
# shutil.rmtree("new_foler") 폴더 안의 모든 것을 삭제
# shutil.copy("rpa_basic/2_desktop/test.py", "rpa_basic/2_desktop/test_folder") #메타정보 복사 : x
# shutil.copy2("rpa_basic/2_desktop/test.py", "rpa_basic/2_desktop/test_folder") #메타정보 복사 : o

# 폴더 복사
# shutil.copytree("rpa_basic/2_desktop/test_folder", "rpa_basic/2_desktop/new2_folder")

# 폴더 이동
# shutil.move("rpa_basic/2_desktop/new2_folder", "rpa_basic/new2_folder")