from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
mail_list = ["leehalim990@daum.net", "ns@tcp-ip.co.kr"]
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
  for mail_l in mail_list:
    for msg in mailbox.fetch(f'(FROM {mail_l}, UNSEEN)', reverse=True):
      print("[{}] {}".format(msg.from_, msg.subject))
      print("-" * 90)
      for att in msg.attachments:
        print("첨부파일 : ", att.filename)
        print("타입 : ", att.content_type)
        print("크기 : ", att.size)
        # 파일 다운로드 
        with open(att.filename, "wb") as f:
          f.write(att.payload)
          print("첨부파일 {} 다운로드 완료".format(att.filename))
          print("=" * 90)