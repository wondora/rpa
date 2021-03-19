import smtplib
from account import *
from email.message import EmailMessage  # 메시지 쉽게 보낸다(정해진 양식 사용안해도 됨)

msg = EmailMessage()
msg["Subject"] = "테스트 메일 입니다."
msg["From"] = EMAIL_ADDRESS
msg["To"] = "wondora@gmail.com"

# 여러명에게 보낼때
# msg["To"] = "wondora@gmail.com","nado@gmail.com", .....
# to_list = ["wondora@gmail.com", "nado@gmail.com", .....]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "wondora@gmail.com"

# # 비밀 참조
# msg["Bcc"] = "wondora@gmail.com"

msg.set_content("테스트 본문입니다.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
  smtp.send_message(msg)