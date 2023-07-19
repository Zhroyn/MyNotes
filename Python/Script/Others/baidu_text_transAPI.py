import requests
import random
import json
from hashlib import md5

# 可用`auto`, `zh`, `en`, `jp`, `cht`(繁体中文), `wyw`(文言文)
# 更多可见 `https://api.fanyi.baidu.com/doc/21`
appid = "20230719001749754"
appkey = "SYtqB3EZRD3QPL2kah0S"
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def translate(url, query, from_lang, to_lang):
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # 建立请求
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # 发送请求
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result

query = "Hello World! This is 1st paragraph.\nThis is 2nd paragraph."
result = translate(url, query, "en", "zh")

print(json.dumps(result, indent=4, ensure_ascii=False))
for trans in result["trans_result"]:
    print(trans["dst"])
