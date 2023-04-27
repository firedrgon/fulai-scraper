import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    token = os.environ["TOKEN"]
except KeyError:
    logger.info("Token not available!")

if __name__ == "__main__":
    headers = {
        'Host': 'api.fulaizhitou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) '
                      'WindowsWechat(0x63090217) XWEB/6763 Flue',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh',
        'token': token
    }
    r = requests.get('https://api.fulaizhitou.com/tools/task/sign', headers=headers)
    if r.status_code == 200:
        data = r.json()
        code = data["code"]
        dou = data["dou"]
        logger.info(f'code: {code}, dou: {dou}')
