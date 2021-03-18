import logging
from datetime import datetime
# logging.DEBUG 는 DEBUG 이상 에러 다 나옴  loggin.error - error 이상 문제 표시
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# debug -> info -> ....
# logging.debug(" 누가 짠거야~~~~~~")
# logging.info("자동화 수행 준비")
# logging.warning("실행상 문제가 있을 수 있습니다.")
# logging.error("에러가 발생했습니다.")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다.")

# 터미널과 파일 로그 함께 남기기
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

#스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일에 저장
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남기는 테스트 진행중")