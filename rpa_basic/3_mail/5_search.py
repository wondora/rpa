from imap_tools import MailBox
from account import *

# mailbox.logout() 할 필요 가 없다.
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
  # for msg in mailbox.fetch():
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 읽지않은 메일 가져오기
  # for msg in mailbox.fetch('(UNSEEN)'):
  #   print("[{}] {}".format(msg.from_, msg.subject))

  # 특정인이 보낸 메일
  # for msg in mailbox.fetch('(FROM wondora@gmail.com)', limit=2, reverse=True):
  #   print("[{}] {}".format(msg.from_, msg.subject))


  # 어떤 글자를 포함하는 메일 
  # for msg in mailbox.fetch('(TEXT "test mail")'):  # 제목만 -> SUBJECT "제목들...."
  #   print("[{}] {}".format(msg.from_, msg.subject)) 
  
  # 한글 검색시...
  for msg in mailbox.fetch(limit=2, reverse=True):
    if "테스트" in msg.subject:  
      print("[{}] {}".format(msg.from_, msg.subject)) 

# 특정 날짜 이후로
# for msg in mailbox.fetch('(SENTSINCE 07-Nove-2020)', reverse=True, limit=4):
#   print("[{}] {}".format(msg.from_, msg.subject)) 


# 특정 날짜 
for msg in mailbox.fetch('(ON 07-Nove-2020)', reverse=True, limit=4):
  print("[{}] {}".format(msg.from_, msg.subject)) 

import time 
print(time.strftime('%d-%a-%Y'))

import datetime
dt = datetime.datetime.strptime("2021-03-12", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%b-%Y'))