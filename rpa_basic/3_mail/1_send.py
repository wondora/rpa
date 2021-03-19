import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
  smtp.ehlo() # 연결 수립 확인
  smtp.starttls() # 모든 내용 암호화 전송
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  subject = "test mail"
  body = "mail body"

  msg = f"Subject: {subject}\n{body}"
  smtp.sendmail(EMAIL_ADDRESS, "wondora@gmail.com", msg) # 발신자, 수신자, 정해진 형식의 메시지





